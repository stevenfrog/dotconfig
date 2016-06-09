#!/usr/bin/env python3

import sys
import os
import shutil
# http://amoffat.github.io/sh/index.html
import sh
import filecmp

# the exclude filename
extFilenames = ['.classpath', '.project']
# the exclude dirs
extDirs = ['build', '.svn', '.git', '.settings', '__pycache__']
# the exclude file's suffix
extSuffixs = ['.bak', '.class', '.jar', '.pyc']

HOME = "/home/stevenfrog"
BACKUP_PATH = "/media/Disk3/Backup/dotconfig"
#BACKUP_PATH2 = "/home/stevenfrog/Nutstore/dotconfig"

BACKUP_FILES = """
~/.bashrc
~/.tmux.conf
~/.Xauthority
~/.xinitrc
~/.xmodmap
~/.Xresources
~/.zshrc
~/bin/*
~/.gimp-2.8/plug-ins/*
/etc/bash.bashrc
/etc/hosts
/etc/modules

~/.gitconfig
~/.gitignore

~/.vimrc
~/.vim/bundles.vim
~/.vim/bundle/vim-monokai/colors/monokai.vim

~/.config/ranger/*
~/Documents/CodeSummary/*
"""



class BackupFiles():

    def backupFile(filename):
        srcFile = filename
        if filename.startswith("~"):
            srcFile = HOME + filename[1:]

        desFile = BACKUP_PATH + filename
        if filename.startswith("~"):
            desFile = BACKUP_PATH + filename[1:]

        #desFile2 = BACKUP_PATH2 + filename
        #if filename.startswith("~"):
        #    desFile2 = BACKUP_PATH2 + filename[1:]

        # get des dir
        index = desFile.rfind("/")
        desPath = desFile[:index]

        #index2 = desFile2.rfind("/")
        #desPath2 = desFile2[:index]

        if not os.path.exists(desPath):
            os.makedirs(desPath)

        #if not os.path.exists(desPath2):
        #    os.makedirs(desPath2)

        if os.path.exists(desFile):
            cmpFlag = filecmp.cmp(srcFile, desFile)
        else:
            cmpFlag = False

        if cmpFlag:
            print("No need backup: "+filename)
        else:
            shutil.copy2(srcFile, desFile)
            #shutil.copy2(srcFile, desFile2)
            print("===Backuped===: "+filename)


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


sh.cd(BACKUP_PATH)
print("====== git pull ======")
os.system("git pull")

ins = BackupFiles()
ins.copyFiles(BACKUP_FILES)

sh.cd(BACKUP_PATH)
print("====== git push======")
os.system("git add --all")
os.system("git commit -am 'updated by program'")
#sh.git("add", "--all")
#sh.git("commit", "--amend", "--no-edit")
#os.system("git pull")
#sh.git("pull")
os.system("git push origin master")
# I add a mirror to github, so we can backup to both github and bitbucket
os.system("git push github")
print("======== Backup finished ========")
print("=== Sync Bitbucket and Github ===")

