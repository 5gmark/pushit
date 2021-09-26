# pushit
Automating a git push with Python

This is a Python script to perform the following:
* Run four (4) Linux commands:
  * cd ~/mycode
  * git add *
  * git commit -m "Some comment..."
  * git push origin
* Incorporate the following command line arguments:
  * -c, --comment
    * Optional.
    * The commit comment.
    * If not used, "Commit Comment: " prompt runs.
  * -h, --help
  * -m, --man-page
    * Installs pushit man page.
  * -s, --symbolic-link
    * Creates a symbolic link from /usr/local/bin to pushit.
  * -v, --version

Notes
---
* shebang:
  * The primary environment for this script envokes Python with `python3`.
  * Modify the shebang line, `#!/usr/bin/env python3`, and/or add symbolic links as needed to accommodate the target environment.
