#!/usr/bin/env python3

import sys
import os
import shutil
import sh

# the exclude filename
extFilenames = ['.classpath', '.project']
# the exclude dirs
extDirs = ['build', '.svn', '.settings', '__pycache__']
# the exclude file's suffix
extSuffixs = ['.bak', '.class', '.jar', '.pyc']

HOME = "/home/stevenfrog"
BACKUP_PATH = "/home/stevenfrog/Documents/dotconfig"

BACKUP_FILES = """
~/.bashrc
~/.tmux.conf
~/.Xauthority
~/.xinitrc
~/.xmodmap
~/.zshrc
~/bin/*
/etc/bash.bashrc

~/.vimrc
~/.vim/bundles.vim
~/.vim/bundle/vim-monokai/colors/monokai.vim
"""

class BackupFiles():

    def backupFile(filename):
        srcFile = filename
        if filename.startswith("~"):
            srcFile = HOME + filename[1:]

        desFile = BACKUP_PATH + filename
        if filename.startswith("~"):
            desFile = BACKUP_PATH + filename[1:]

        # get des dir
        index = desFile.rfind("/")
        desPath = desFile[:index]

        if not os.path.exists(desPath):
            os.makedirs(desPath)

        shutil.copy2(srcFile, desFile)
        print("Backuped: "+filename)


    @classmethod
    def copyFiles(self, input_files):
        for line in input_files.splitlines():
            line = line.strip()
            if line == "":
                continue

            if line.endswith("*"):
                dirPath = line[:-1]

                if line.startswith("~"):
                    dirPath = HOME + line[1:-1]

                if not os.path.exists(dirPath):
                    os.makedirs(dirPath)
                for root, dirs, files in os.walk(dirPath):
                    #check path whether need exculde
                    if os.path.split(root)[1].lower() in extDirs:
                        #clear the dirs while walking
                        #if use dirs=[], it will not change the original array
                        dirs[:] = []
                        #no need add filename in current dir
                        continue
                    for filename in files:
                        if filename in extFilenames:
                            continue
                        tempname = os.path.join(root, filename)
                        if (os.path.isfile(tempname)) and os.path.splitext(filename)[1].lower() not in extSuffixs:
                            # print(tempname.replace(HOME, "~"))
                            self.backupFile(tempname.replace(HOME, "~"))
            else:
                self.backupFile(line)



ins = BackupFiles()
ins.copyFiles(BACKUP_FILES)


sh.cd(BACKUP_PATH)
print(sh.git("add", "--all"))
print(sh.git("commit", "--amend", "--no-edit"))
print(sh.git("pull"))
print(sh.git("push", "origin", "master"))
print("====== Backup finished ======")

