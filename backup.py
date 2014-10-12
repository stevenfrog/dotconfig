#!/usr/bin/env python3

import sys
import os
import shutil
import sh

HOME = "/home/stevenfrog"
BACKUP_PATH = "/home/stevenfrog/Documents/dotconfig"

BACKUP_FILES = """
~/.bashrc
~/.vimrc
~/.Xauthority
~/.xinitrc
~/.xmodmap
/etc/bash.bashrc
"""

class BackupFiles():

    def copyFiles(input_files):
        for line in input_files.splitlines():
            line = line.strip()
            if (line == ""):
                continue

            srcFile = line
            if (line.startswith("~")):
                srcFile = HOME + line[1:]

            desFile = BACKUP_PATH + line
            if (line.startswith("~")):
                desFile = BACKUP_PATH + line[1:]

            # get des dir
            index = desFile.rfind("/")
            desPath = desFile[:index]

            if (not os.path.exists(desPath)):
                os.makedirs(desPath)

            shutil.copy2(srcFile, desFile)
            print("Backuped: "+line)


# def process_output(line):
#     print(line)



# BackupFiles.copyFiles(BACKUP_FILES)
# print(sh.ls("/home/stevenfrog"))
# sh.google_chrome("http://www.baidu.com")
sh.cd(BACKUP_PATH)
# sh.ls("-a", _out=process_output)
print(sh.ls("-a"))
print(sh.git("add", "--all"))
print(sh.git("commit", "--amend", "--no-edit"))
print(sh.git("pull"))
# print(sh.git("push", "origin", "master"))
