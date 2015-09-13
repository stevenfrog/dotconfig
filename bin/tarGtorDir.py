#!/usr/bin/env python3

import sys
import os
from os.path import join

# the movie file suffixs
MOVIE_SUFFIXS = ['.mov', '.mp4', '.mkv', '.avi']
# the exclude dirs
EXCLUDE_DIRS = ['build', '.svn', '.settings', 'bin', 'target']
# the exclude filename
EXCLUDE_FILES = []

EXPECTED_SUFFIX = '.mkv'
OUTPUT_DIR = '/home/stevenfrog/temp/output'

# avconv command
AVCONV_COMMAND = 'avconv -i "%s" -map 0:0 -map 0:1 -threads 8 -aspect 16:9 -y %s %s "%s"'
SOUND_PARAM = '-acodec ac3 -b:a 128k -ar 44100 -ac 2'
VIDEO_PARAM = '-b:v 2048k -r 23.98 -vcodec libx264 -vprofile baseline -s 1280x720'
#VIDEO_PARAM = '-b:v 1024k -r 23.98 -vcodec libx264 -vprofile baseline'



class AvconvFiles():

    @staticmethod
    # Print the help message
    def usage():
        print()
        print('This is used to call avconv tansfer movies in one directory.')
        print('The sample usage:')
        print('    tarGtorDir.py dir1')

    # retrive (dir, file_names)
    def retriveFilenames(directory):
        resFilenames = []
        for root, dirs, files in os.walk(directory):
            #check path whether need exculde
            if os.path.split(root)[1].lower() in EXCLUDE_DIRS:
                #clear the dirs while walking
                #if use dirs=[], it will not change the original array
                dirs[:] = []
                #no need add filename in current dir
                continue
            for filename in files:
                if filename in EXCLUDE_FILES:
                    continue
                tempname = join(root, filename)
                if (os.path.isfile(tempname)) and os.path.splitext(filename)[1].lower() in MOVIE_SUFFIXS:
                    resFilenames.append((root, filename))
        return resFilenames



    @classmethod
    # transfer all files in one directory
    def transferToMKV(self, dir1):
        files = self.retriveFilenames(dir1)

        for dir2, file2 in files:
            input_file = join(dir2, file2)
            ouput_file = join(OUTPUT_DIR, file2[:-4] + EXPECTED_SUFFIX)

            print("====== avconv tranfer ======")
            print("====== %s >>> %s" % (input_file, ouput_file))
            command = AVCONV_COMMAND % (input_file, SOUND_PARAM, VIDEO_PARAM, ouput_file)
            print(command)
            #os.system will call command in bash
            os.system(command)



# ---------------main------------------------
if len(sys.argv) < 2:
    AvconvFiles.usage()
    sys.exit()
dir1 = os.path.normpath(sys.argv[1])
ins = AvconvFiles()
ins.transferToMKV(dir1)
