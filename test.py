#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from typing import Any

TARGET_ALG = "STREEBOG-256"
ID_FIELDS = ("cpe", "purl")


def remove_hash_alg(obj: Any, target_alg: str = TARGET_ALG, *, remove_empty_hashes: bool = True) -> int:
    """
    Recursively removes hash objects with {"alg": target_alg} from any "hashes" arrays.
    Returns the number of removed hash entries.
    """
    removed = 0

    if isinstance(obj, dict):
        if isinstance(obj.get("hashes"), list):
            old_hashes = obj["hashes"]
            new_hashes = [
                h for h in old_hashes
                if not (isinstance(h, dict) and h.get("alg") == target_alg)
            ]
            removed += len(old_hashes) - len(new_hashes)

            if new_hashes:
                obj["hashes"] = new_hashes
            elif remove_empty_hashes:
                obj.pop("hashes", None)
            else:
                obj["hashes"] = []

        for value in list(obj.values()):
            removed += remove_hash_alg(value, target_alg, remove_empty_hashes=remove_empty_hashes)

    elif isinstance(obj, list):
        for item in obj:
            removed += remove_hash_alg(item, target_alg, remove_empty_hashes=remove_empty_hashes)

    return removed


def add_missing_component_id_fields(sbom: dict[str, Any], *, fields: tuple[str, ...] = ID_FIELDS) -> dict[str, int]:
    """
    Adds missing identifier fields, for example "cpe": "" and/or "purl": "",
    to every object in top-level CycloneDX "components".

    Existing cpe/purl values are not changed.
    Missing fields are inserted right after "version" when possible.
    """
    stats = {field: 0 for field in fields}
    components = sbom.get("components")

    if not isinstance(components, list):
        return stats

    for component in components:
        if not isinstance(component, dict):
            continue

        missing = [field for field in fields if field not in component]
        if not missing:
            continue

        for field in missing:
            stats[field] += 1

        # Rebuild dict to place cpe/purl after version if version exists.
        rebuilt: dict[str, Any] = {}
        inserted = False

        for key, value in component.items():
            rebuilt[key] = value

            if key == "version":
                for field in fields:
                    if field not in component:
                        rebuilt[field] = ""
                inserted = True

        # If there is no version key, put missing id fields after name if possible,
        # otherwise append them to the end.
        if not inserted:
            if "name" in component:
                rebuilt = {}
                for key, value in component.items():
                    rebuilt[key] = value
                    if key == "name":
                        for field in fields:
                            if field not in component:
                                rebuilt[field] = ""
            else:
                for field in fields:
                    if field not in component:
                        rebuilt[field] = ""

        component.clear()
        component.update(rebuilt)

    return stats


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Normalize a CycloneDX SBOM JSON: remove STREEBOG-256 hashes and "
            "add empty cpe/purl fields to components where they are missing."
        )
    )
    parser.add_argument("input", help="Input SBOM JSON file")
    parser.add_argument(
        "-o", "--output",
        help="Output SBOM JSON file. Default: <input>.normalized.json"
    )
    parser.add_argument(
        "--alg",
        default=TARGET_ALG,
        help=f"Hash algorithm to remove. Default: {TARGET_ALG}"
    )
    parser.add_argument(
        "--keep-empty-hashes",
        action="store_true",
        help='Keep "hashes": [] when all hashes are removed instead of deleting the hashes field.'
    )
    parser.add_argument(
        "--skip-remove-hashes",
        action="store_true",
        help="Do not remove hashes; only add missing cpe/purl fields."
    )
    parser.add_argument(
        "--skip-add-empty-ids",
        action="store_true",
        help="Do not add missing cpe/purl fields; only remove hashes."
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path.with_suffix(".normalized.json")

    with input_path.open("r", encoding="utf-8") as f:
        sbom = json.load(f)

    removed_hashes = 0
    added_stats = {field: 0 for field in ID_FIELDS}

    if not args.skip_remove_hashes:
        removed_hashes = remove_hash_alg(
            sbom,
            target_alg=args.alg,
            remove_empty_hashes=not args.keep_empty_hashes,
        )

    if not args.skip_add_empty_ids:
        added_stats = add_missing_component_id_fields(sbom)

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(sbom, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Removed hash entries with alg={args.alg}: {removed_hashes}")
    print(f"Added empty cpe fields: {added_stats.get('cpe', 0)}")
    print(f"Added empty purl fields: {added_stats.get('purl', 0)}")
    print(f"Saved normalized SBOM to: {output_path}")


if __name__ == "__main__":
    main()
