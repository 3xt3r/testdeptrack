2026-07-06 10:51:03 | INFO    |     checkout test @ release_5.7.0
2026-07-06 10:51:03 | INFO    |     running: git -c credential.helper= -c http.extraHeader=Authorization: Basic *** checkout -- .
2026-07-06 10:51:03 | ERROR   |     [FAIL] git checkout -- . (reset local changes): error: pathspec '.' did not match any file(s) known to git
2026-07-06 10:51:03 | INFO    |     running: git -c credential.helper= -c http.extraHeader=Authorization: Basic *** clean -fd
2026-07-06 10:51:03 | INFO    |     running: git -c credential.helper= -c http.extraHeader=Authorization: Basic *** checkout release_5.7.0
2026-07-06 10:51:03 | INFO    |     running: git -c credential.helper= -c http.extraHeader=Authorization: Basic *** reset --hard origin/release_5.7.0
2026-07-06 10:51:03 | INFO    |     running: git -c credential.helper= -c http.extraHeader=Authorization: Basic *** submodule update --init --recursive
2026-07-06 10:51:07 | INFO    |     cloning: https://git.locl/garda-bd/test/
2026-07-06 10:51:07 | INFO    |     running: git -c credential.helper= clone --no-checkout https://git.locl/garda-bd/test/ /home/testuser/jobs/test/_repos/test
2026-07-06 10:51:07 | ERROR   |     [FAIL] git clone: Cloning into '/home/testuser/jobs/test/_repos/test'...
fatal: could not read Username for 'https://git.locl': terminal prompts disabled
2026-07-06 10:51:07 | INFO    |     clone without token failed — retrying with token
2026-07-06 10:51:07 | INFO    |     running: git -c credential.helper= -c http.extraHeader=Authorization: Basic *** clone --no-checkout https://git.locl/garda-bd/test/ /home/testuser/jobs/test/_repos/test
