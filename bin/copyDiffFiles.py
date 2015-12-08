#!/usr/bin/env python3

import filecmp
import sys
import os
import shutil
from os.path import join

# the exclude filename
extFilenames = ['.classpath', '.project', '.gitignore']
# the exclude dirs
extDirs = ['build', '.svn', '.git', '.settings', 'bin', 'target']
# the exclude file's suffix
#extSuffixs = ['.bak', '.png', '.gif', '.jpg', '.class', '.jar']
extSuffixs = ['.bak', '.class', '.jar']


class CopyDiffFiles():

    # Print the help message
    @staticmethod
    def usage():
        print()
        print('This is used to compare two directories.')
        print('It will show different and copy updated files to new dir.')
        print('The sample usage:')
        print('    copyDiffFiles.py dir1 dir2 dir3')
        print('    dir1 is newer dir')
        print('    dir2 is older dir')
        print('    dir3 is dir to store updated files. if not provide, just show differents')
        print('The sample output:')
        print('    >   filename1    -- file need add')
        print('    !=  filename2    -- file need update')
        print('    <   filename3    -- file need remove')

    # retrive file names to compare
    def retriveFilenames(directory):
        dirLen = len(directory) + 1
        resFilenames = []
        for root, dirs, files in os.walk(directory):
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
                tempname = join(root, filename)
                if (os.path.isfile(tempname)) and os.path.splitext(filename)[1].lower() not in extSuffixs:
                    resFilenames.append(tempname[dirLen:])
        resFilenames.sort()
        return resFilenames

    # create directory if it does not exist
    def createDir(filename):
        path = os.path.dirname(filename)
        if not os.path.exists(path):
            os.makedirs(path)

    # get files that have same dir and name
    def getCommonFiles(files1, files2):
        common = []
        i = 0
        length = len(files1)
        while i < length:
            f = files1[i]
            try:
                t = files2.index(f)
            except:
                t = -1
            if t >= 0:
                common.append(f)
                del files1[i]
                del files2[t]
                length -= 1
            else:
                i += 1
        return common

    # compare files in dir1 and dir2
    # if dir3 is not None, copy different files into it
    @classmethod
    def copydifffiles(self, dir1, dir2, dir3=None):
        files1 = self.retriveFilenames(dir1)
        files2 = self.retriveFilenames(dir2)
        # retrive same files both in dir1 and dir2
        common = self.getCommonFiles(files1, files2)

        match, mismatch, error = filecmp.cmpfiles(dir1, dir2, common)

        print('%s VS %s' % (dir1, dir2))
        print('stat       filename')
        print('——–– —–—–—–—–—–—–—–—–—–————')
        for f in files1:
            print(' >   %s' % f)
        #for f in match:
            #print('  =   %s' % f)
        for f in mismatch:
            print(' !=  %s' % f)
        if len(files2) != 0:
            print('================  IMPORTANT !!!  ================')
            print('======== The files maybe need be deleted ========')
            for f in files2:
                print(' <   %s' % f)

        # copy the diff files into expect path
        if dir3 is not None:
            # clear dist dir first
            if os.path.exists(dir3):
                shutil.rmtree(dir3)

            for f in files1:
                destFilename = join(dir3, f)
                self.createDir(destFilename)
                shutil.copy2(join(dir1, f), destFilename)
            for f in mismatch:
                destFilename = join(dir3, f)
                self.createDir(destFilename)
                shutil.copy2(join(dir1, f), destFilename)


## ---------------main------------------------
if len(sys.argv) < 3:
    CopyDiffFiles.usage()
    sys.exit()
dir1 = os.path.normpath(sys.argv[1])
dir2 = os.path.normpath(sys.argv[2])
dir3 = None
if len(sys.argv) >= 4:
    dir3 = os.path.normpath(sys.argv[3])
#dir1='/home/stevenfrog/temp/temp_dif1'
#dir2='/home/stevenfrog/temp/temp_dif2'
#dir3='/home/stevenfrog/temp/temp_dif3'
ins = CopyDiffFiles()
ins.copydifffiles(dir1, dir2, dir3)
