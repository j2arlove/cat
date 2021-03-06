# Hello Cat!

This is a github repository for cats.

## Basic Git commands

1. `git clone <URL>`: Clones remote repository into local drive
2. `git pull`: Fetches the latest from remote repository
3. `git status`: Shows current status
4. `git diff`: Shows how **unstaged** files are changed
5. `git add <directory or file>`: Stages file for commit
6. `git commit`: Prepares commit from staged files
7. `git push`: Pushes the commit
8. `git rm`: Remove the file (needs commit and push)

### Branching......... 나중에....

## Install Instructions (for Windows)

1. Install Python 3: www.python.org
2. Install Atom: atom.io
3. Install Git for Windows: https://git-for-windows.github.io/
    - Use default options
4. Set $PATH
    4.1. My PC > System > Advanced PC Settings > Advanced > Environment Variables > System Variable > Path > Edit
    4.2. Add those two lines:
    4.3. `C:\Users\JR Choi\AppData\Local\Programs\Python\Python35-32\`
    4.4. `C:\Users\JR Choi\AppData\Local\Programs\Python\Python35-32\Scripts`
5. Open Git Bash
6. Type `pip install flask`
6. Type `cd ~/Documents/`
7. Type `mkdir github`
8. Type `git clone https://github.com/j2arlove/cat.git`
9. Type `cd cat`
10. Type `python app.py`

## Install Instructions (for Mac)

0. Install Python 3 by upgrading your Mac OS to the latest version
    - Type `python3` to check if Python 3 is installed on your computer
1. Open Terminal
2. Type `git clone https://github.com/j2arlove/cat.git`
3. Type `cd cat/`
4. Type `pip3 install flask`
