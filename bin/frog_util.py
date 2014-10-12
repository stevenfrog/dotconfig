#!/usr/bin/env python3
"""
This class provide many useful methods.
"""

import os
import unittest


def show_file_content(file_name):
    """
    Show the file content in console.
    """

    print('=======================================')
    with open(file_name, 'r') as f:
        for line in f:
            print(line, end='')


def camel_name(name, split_char='_'):
    """
    Change the string to camel name.
    abc_def -> abcDef

    If set split_char = ' '
    abc def -> abcDef
    """

    res = ''
    need_upper = False
    isFirstWord = True
    for c in name:
        if need_upper:
            need_upper = False
            res += c.upper()
            # isFirstWord = False
        elif c == split_char:
            need_upper = True
            isFirstWord = False
        else:
            # make sure first word is lower
            if isFirstWord:
                c = c.lower()
            res += c

    return res


def uncamel_name(name, split_char=' '):
    """
    Change the camel name to normal string
    abcDef -> abc def

    If set split_char = '_'
    abcDef -> abc_def
    """

    res = ''
    is_first = True
    num_before_char_upper = 0
    for c in name:
        if c.isupper():
            if is_first or num_before_char_upper > 0:
                res += c.lower()
            else:
                res += split_char + c.lower()
            num_before_char_upper += 1
        else:
            if num_before_char_upper > 1:
                res = res[:-1] + split_char + res[-1:]
            res += c
            num_before_char_upper = 0
        is_first = False
    return res


def word_add_s(word):
    """
    Add s for string
    word    ->  words
    family  ->  families
    potato  ->  potatoes
    class   ->  classes
    cloth   ->  clothes
    half    ->  halves

    THIS METHOD IS NOT FULLY CORRECT IN ENGLISG SYNTAX
    CHECK OUTPUT MANUALLY!!!
    """

    sound_words = 'aeiou'
    res = ''
    if word[-1] == 'y' and not word[-2] in sound_words:
        res = word[:-1] + 'ies'
    elif word[-1] == 'f':
        res = word[:-1] + 'ves'
    elif word[-2:] == 'fe':
        res = word[:-2] + 'ves'
    elif word[-1] == 'o' and not word[-2] in sound_words:
        res = word + 'es'
    elif word[-1] == 'h' and not word[-2] in sound_words:
        res = word + 'es'
    elif word[-1] == 's':
        res = word + 'es'
    else:
        res = word + 's'
    return res


def word_remove_s(word):
    """
    Remove s for string
    words     ->  word
    families  ->  family
    potatoes  ->  potato
    classes   ->  class
    knives    ->  knife
    clothes   ->  cloth

    THIS METHOD IS NOT FULLY CORRECT IN ENGLISG SYNTAX
    CHECK OUTPUT MANUALLY!!!
    """

    last_words = 'sh'
    sound_words = 'aeiou'
    res = ''
    if word.endswith('ies'):
        res = word[:-3] + 'y'
    elif word.endswith('ives'):
        res = word[:-3] + 'fe'
    elif word.endswith('ves'):
        res = word[:-3] + 'f'
    elif word.endswith('es') and word[-3] in last_words:
        res = word[:-2]
    elif word.endswith('es') and word[-3] in sound_words:
        res = word[:-2]
    else:
        # left are all XXXs
        res = word[:-1]
    return res


def str2python(file_name):
    """
    Transfer the string for python code.

    /**
     * XXX
     */
    public class Abc
    >>>>>>>>>>
    res_str = '/**' + LS
    res_str += ' * XXX' +LS
    res_str += ' */' + LS
    res_str += 'public class Abc' +LS
    """

    LS = os.linesep
    res = ''
    with open(file_name, 'r') as f:
        is_first_line = True
        indent_num = 0
        for line in f:
            if is_first_line:
                indent_num = len(line) - len(line.lstrip())
                res += "res_str = '" + line.rstrip()[indent_num:] + "' + LS" + LS
                is_first_line = False
            elif len(line.strip()) == 0:
                res += "res_str += LS" + LS
            else:
                res += "res_str += '" + line.rstrip()[indent_num:] + "' + LS" + LS
    print(res)
    return res


def get_all_files(dirpath, fileExt='.java', walk_in=False):
    """
    Get all files name from one directory.

    EX:
    --  example
        --  AAA.java
        --  BBB.c
        --  D1
            --  CCC.java
            --  DDD.java

    get_all_files(example)  ->  AAA.java
    get_all_files(example, '.c')  ->  BBB.c
    get_all_files(example, '.java', True)  ->  AAA.java, CCC.java, DDD.java
    """

    # get all java files from root directory
    if not os.path.isdir(dirpath):
        print('The dir path:' + dirpath + ' is not directory')
        return False
    #dir_abs_path = os.path.abspath(dirpath)
    src_files = []

    if walk_in:
        for parent, dirnames, filenames in os.walk(dirpath):
            #if parent.find('/src/java/') != -1:
                #continue
            for name in filenames:
                if name.endswith(fileExt):
                    src_files.append(os.path.join(parent, name))
    else:
        for name in os.listdir(dirpath):
            if name.endswith(fileExt):
                src_files.append(os.path.join(dirpath, name))

    return src_files


def check_filepath_and_output(filepath, file_output, fileExt='.java'):
    # Check the file whether exists and generate the del and drop file name
    if not os.path.isfile(filepath):
        print('The file path:' + filepath + ' is not exists')
        return False
    fname, fextension = os.path.splitext(filepath)
    if fextension != fileExt:
        print("The file's extenstion must be '" + fileExt + "'")
        return False
    if os.path.isfile(file_output) and os.path.samefile(filepath, file_output):
        print("The input file can not be same as output")
        return False
    file_dir = os.path.dirname(file_output)
    if file_dir and not os.path.isdir(file_dir):
        os.makedirs(file_dir)
    return True


def file_dir_name_ext(filepath):
    """
    Get file dir, file name and file extention.

    EX: test_files/abc/AAA.java
    --> ('test_files/abc', 'AAA', '.java')
    """

    dirname = os.path.dirname(filepath)
    basename = os.path.basename(filepath)
    name, ext = basename.split('.', 1)
    return dirname, name, '.'+ext


def abbreviate(name):
    """
    Change the string to abbreviation.

    ReportDevelopment -> ReportDev
    reportDevelopment -> reportDev
    isBufferError     -> isBufErr
    ABCProgramServer  -> ABCPrgSrv
    """

    ABBR_WORS = {
        'Appliance'      : 'App',
        'Application'    : 'App',
        'Average'        : 'Avg',
        'Background'     : 'Bg',
        'Backup'         : 'Bu',
        'Backups'        : 'Bu',
        'Buffer'         : 'Buf',
        'Configuration'  : 'Conf',
        'Configure'      : 'Conf',
        'Connection'     : 'Conn',
        'Control'        : 'Ctrl',
        'Delete'         : 'Del',
        'Document'       : 'Doc',
        'Develop'        : 'Dev',
        'Development'    : 'Dev',
        'Environment'    : 'Env',
        'Error'          : 'Err',
        'Escape'         : 'Esc',
        'Implement'      : 'Impl',
        'Implementation' : 'Impl',
        'Increment'      : 'Inc',
        'Information'    : 'Info',
        'Initial'        : 'Init',
        'Image'          : 'Img',
        'Length'         : 'Len',
        'Library'        : 'Lib',
        'Libraries'      : 'Libs',
        'Management'     : 'Mgmt',
        'Manager'        : 'Mgr',
        'Message'        : 'Msg',
        'Password'       : 'Pwd',
        'Picture'        : 'Pic',
        'Point'          : 'Pt',
        'Program'        : 'Prg',
        'Server'         : 'Srv',
        'Source'         : 'Src',
        'String'         : 'Str',
        'Technology'     : 'Tech',
        'Window'         : 'Win'
    }

    res = name
    isFirstCharLow = False
    if name[0].islower():
        isFirstCharLow = True
        res = name[0].upper()+name[1:]

    sortedKeys = sorted(ABBR_WORS.keys(), reverse=True)
    for key in sortedKeys:
        res = res.replace(key, ABBR_WORS[key])

    if isFirstCharLow:
        res = res[0].lower()+res[1:]

    return res


def printAlignedArray(arraies, all_column_char='', two_column_char=''):
    """
    Print array by fixed space.

    Input:

    [('a','a1'),
     ('bb','b1'),
     ('ccc','c1'),
     ('dddd','d1'),
     ('ee','e1'),
     ('fff','f1')]

    Output:

    a     abc  a1  edf
    bb    abc  b1  edf
    ccc   abc  c1  edf
    dddd  abc  d1  edf
    ee    abc  e1  edf
    fff   abc  f1  edf

    If call printAlignedArray(arraies, all_column_char='|'), output will be:

    a     |  abc  |  a1  |  edf
    bb    |  abc  |  b1  |  edf
    ccc   |  abc  |  c1  |  edf
    dddd  |  abc  |  d1  |  edf
    ee    |  abc  |  e1  |  edf
    fff   |  abc  |  f1  |  edf

    If call printAlignedArray(arraies, two_column_char='|'), output will be:

    a     abc  |  a1  edf
    bb    abc  |  b1  edf
    ccc   abc  |  c1  edf
    dddd  abc  |  d1  edf
    ee    abc  |  e1  edf
    fff   abc  |  f1  edf
    """

    SPLIT_SPACE = 2
    max_len = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ele_len = len(arraies[0])
    two_column_num = -1
    if two_column_char:
        two_column_num = ele_len // 2
    for element in arraies:
        for i in range(ele_len):
            max_len[i] = max(max_len[i], len(element[i]))

    for element in arraies:
        for i in range(ele_len):
            if two_column_num == i:
                print(two_column_char.ljust(1+SPLIT_SPACE), end='')
            elif all_column_char and i != 0:
                print(all_column_char.ljust(1+SPLIT_SPACE), end='')
            print(element[i].ljust(max_len[i]+SPLIT_SPACE), end='')
        print()



class TestSelfFunctions(unittest.TestCase):

    def setUp(self):
        pass


    def test_camel_name(self):
        name = 'file_name'
        self.assertEqual('fileName', camel_name(name))

        name = 'file name'
        self.assertEqual('fileName', camel_name(name, ' '))

        name = 'File Name'
        self.assertEqual('fileName', camel_name(name, ' '))


    def test_uncamel_name(self):
        name = 'fileName'
        self.assertEqual('file name', uncamel_name(name))

        name = 'fileName'
        self.assertEqual('file_name', uncamel_name(name, '_'))


    def test_word_add_s(self):
        word = 'fileName'
        self.assertEqual('fileNames', word_add_s(word))

        word = 'boy'
        self.assertEqual('boys', word_add_s(word))

        word = 'tomato'
        self.assertEqual('tomatoes', word_add_s(word))

        word = 'family'
        self.assertEqual('families', word_add_s(word))

        word = 'girl'
        self.assertEqual('girls', word_add_s(word))

        word = 'cloth'
        self.assertEqual('clothes', word_add_s(word))

        word = 'half'
        self.assertEqual('halves', word_add_s(word))

        word = 'knife'
        self.assertEqual('knives', word_add_s(word))


    def test_word_remove(self):
        word = 'fileNames'
        self.assertEqual('fileName', word_remove_s(word))

        word = 'boys'
        self.assertEqual('boy', word_remove_s(word))

        word = 'tomatoes'
        self.assertEqual('tomato', word_remove_s(word))

        word = 'families'
        self.assertEqual('family', word_remove_s(word))

        word = 'girls'
        self.assertEqual('girl', word_remove_s(word))

        word = 'catches'
        self.assertEqual('catch', word_remove_s(word))

        word = 'clothes'
        self.assertEqual('cloth', word_remove_s(word))

        word = 'halves'
        self.assertEqual('half', word_remove_s(word))

        word = 'knives'
        self.assertEqual('knife', word_remove_s(word))


    def test_abbreviate(self):
        name = 'ReportDevelopment'
        self.assertEqual('ReportDev', abbreviate(name))

        name = 'reportDevelopment'
        self.assertEqual('reportDev', abbreviate(name))

        name = 'isBufferError'
        self.assertEqual('isBufErr', abbreviate(name))

        name = 'ABCProgramServer'
        self.assertEqual('ABCPrgSrv', abbreviate(name))

        name = 'implementationEnvironmentNew'
        self.assertEqual('implEnvNew', abbreviate(name))


if __name__ == '__main__':
    unittest.main()
