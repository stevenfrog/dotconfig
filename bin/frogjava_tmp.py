#! /usr/bin/python

import sys
import os
import getopt
import re
import datetime

LS = os.linesep


def transfer_tcuml_file(filepath, file_output):
    # Transfer create.sql into drop and delete tables

    # Check the file whether exists and generate the del and drop file name
    if not os.path.isfile(filepath):
        print('The file path:' + filepath + ' is not exists')
        return False
    fname, fextension = os.path.splitext(filepath)
    if fextension != '.java':
        print("The file's extenstion must be '.java'")
        return False
    if os.path.isfile(file_output) and os.path.samefile(filepath, file_output):
        print("The input file can not be same as output")
        return False
    file_dir = os.path.dirname(file_output)
    if file_dir and not os.path.isdir(file_dir):
        os.makedirs(file_dir)

    ## if del or drop file exits, ask user whether overwrite
    #if os.path.exists(file_output):
        #x = input('output file[' + file_output + '] exists, overwrite? Yes ').lower()
        #if x != '' and x != 'y' and x != 'yes':
            #return False

    # Get the tables names from input file and generate del and drop files
    #input_file = open(filepath, 'r')
    #out_file = open(file_output, 'w')

    java_structure = {}
    java_structure['fields'] = []
    java_structure['methods'] = []
    p_class = re.compile('(?:public|protected)(?:.*) class (.*) \{')
    p_field = re.compile('(?:public|protected|private)(?: static)?(?: final)? (.*);')
    p_method = re.compile('(?:public|protected|private)(?: static)? (.*)\((?:.)*\) \{')
    with open(filepath, 'r') as f1:
        is_doc = False
        for line in f1:
            striped_line = line.strip()

            m_class = p_class.match(striped_line)
            m_field = p_field.match(striped_line)
            m_method = p_method.match(striped_line)

            if m_class:
                strs = m_class.group(1).split()
                java_structure['class'] = strs[0]
            elif m_field:
                f_str = m_field.group(1)
                idx = f_str.find('>')
                if idx > 0:
                    java_structure['fields'].append((f_str[:idx+1], f_str[idx+2:]))
                else:
                    strs = m_field.group(1).split()
                    java_structure['fields'].append((strs[0], strs[1]))
            elif m_method:
                strs = m_method.group(1).split()
                if len(strs) > 1:
                    java_structure['methods'].append((strs[0], strs[1]))

    #print(java_structure)
    #print('==============================')
    #print(java_structure['class'])
    #print('==============================')
    #print(java_structure['fields'])
    #print('==============================')
    #print(java_structure['methods'])
    print('==============================')
    print(java_structure['class'])
    print(generate_tostring(java_structure['fields']))

    with open(file_output, 'a') as f2:
        f2.write('=============' + java_structure['class'])
        f2.write(LS)
        f2.write(LS)
        f2.write(generate_tostring(java_structure['fields']))


def generate_tostring(fields):
    res = '/**' + LS
    res += ' * The toString method.' + LS
    res += ' *' + LS
    res += ' * @return the string for this entity' + LS
    res += ' */' + LS
    res += '@Override' + LS
    res += 'public String toString() {' + LS
    res += '    StringBuilder sb = new StringBuilder();' + LS
    res += '    sb.append("{").append(super.toString());' + LS

    l = len(fields)
    for i in range(l):
        ftype, fname = fields[i]
        if i == l-1:
            res += '    sb.append(", ' + fname + ':").append(' + fname + ').append("}");' + LS
        else:
            res += '    sb.append(", ' + fname + ':").append(' + fname + ');' + LS
    res += '    return sb.toString();' + LS
    res += '}' + LS + LS
    return res


def generate_header():
    # create the tocpder header
    today = datetime.date.today()
    header = '/*' + LS + ' * Copyright (C) '
    header += today.strftime('%Y')
    header += ' TopCoder Inc., All Rights Reserved.' + LS + ' */' + LS
    return header


def add_last_period(line):
    # add '.' in the end of line
    if not line.endswith('.'):
        return line + '.'
    else:
        return line


def correct_invalid_char(line):
    # change '<' '>' into html string
    temp = line.replace('<', '&lt;')
    return temp.replace('>', '&gt;')


def transfer_classdoc(class_doc):
    # Transfer the java doc for class part
    result = ''
    for line in class_doc.strip().splitlines():
        changed_line = ''
        if line == '*':
            continue
        elif line.find('Thread Safety:') != -1 or line.find('Thread safety:') != -1:
            changed_line = '* </p>' + LS + '* <p>' + LS + '* <b>Thread Safety:</b>'
            if not line.endswith(':'):
                changed_line += line[(line.find(':') + 1):] + '<br>' + LS
        elif line == '/**':
            changed_line = '/**' + LS + '* <p>' + LS
        elif line == '*/':
            changed_line = '* </p>' + LS + '*' + LS + '* @author TCSDESIGNER, TCSDEVELOPER' + LS + '* @version 1.0' + LS + '*/' + LS
        else:
            temp = correct_invalid_char(line)
            changed_line = add_last_period(temp) + '<br>' + LS
        result += changed_line
    result = result.replace('<b>Thread Safety:</b>*', '<b>Thread Safety:</b>')
    result = result.replace('<br>' + LS + '* </p>', LS + '* </p>')
    return result


def transfer_fielddoc(field_doc):
    # Transfer the java doc for field part
    result = ''
    for line in field_doc.strip().splitlines():
        changed_line = ''
        if line == '*':
            continue
        elif line == '/**' or line == '*/':
            changed_line = line + LS
        else:
            temp = correct_invalid_char(line)
            changed_line = add_last_period(temp) + '<br>' + LS
        result += changed_line
    result = result.replace('<br>' + LS + '*/', LS + '*/')
    return result


def transfer_methoddoc(method_doc):
    # Transfer the java doc for method part
    result_doc = ''
    result_imp = ''
    status = 0
    p_param_exception = re.compile('\* [-:] (\w+) [-:] (.*)')
    p_doc_ok = re.compile('\* @(?:param|throw|throws|return) (?:.*)')
    p_param = re.compile('\* #param (.*)')
    p_exception = re.compile('\* ((?:\w+)Exception)(?: is thrown)? (.*)')
    p_implement = re.compile('\* (Implemene?tation|Implements? notes|Impl notes?)\:')
    for line in method_doc.strip().splitlines():
        m_param = p_param.match(line)
        if m_param:
            status = 1

        if status != 4 and (line == '*' or line == '* none'):
            continue
        elif line.startswith('/**') or line.startswith('*/'):
            status = 0
            result_doc += line + LS
        elif line.find('Parameters:') != -1:
            status = 1
            continue
        elif line.find('Returns:') != -1:
            status = 2
            continue
        elif line.find('Exceptions:') != -1 or line.find('exceptions:') != -1:
            status = 3
            continue
        elif p_implement.match(line):
            status = 4
            continue
        elif (status != 1 and status != 2) and (line.find('@param') != -1 or line.find('@return') != -1):
            status = 0
            continue
        elif status == 1:
            m_param2 = p_doc_ok.match(line)
            m_param3 = p_param_exception.match(line)
            if m_param:
                result_doc += '* @param ' + m_param.group(1) + LS
            elif m_param2:
                result_doc += line + LS
            elif m_param3:
                result_doc += '* @param ' + m_param3.group(1) + ' ' + m_param3.group(2) + LS
        elif status == 2:
            m_return = p_doc_ok.match(line)
            if m_return:
                result_doc += line + LS
            else:
                result_doc += '* @return ' + line[2:] + LS
        elif status == 3:
            m_exception = p_exception.match(line)
            if not m_exception:
                m_exception = p_param_exception.match(line)
            m_exception2 = p_doc_ok.match(line)
            if m_exception2:
                fixed_line = line.replace('@throw ', '@throws ')
                result_doc += fixed_line + LS
            elif m_exception:
                result_doc += '* @throws ' + m_exception.group(1) + ' ' + m_exception.group(2) + LS
            else:
                result_doc += line + LS
        elif status == 4:
            result_imp += '    //' + line[1:] + LS
        else:
            temp = correct_invalid_char(line)
            result_doc += add_last_period(temp) + LS
    # Fix the '@param return xxx' -> '@return xxx'
    result_doc = result_doc.replace('@param return', '@return')
    return (result_doc, result_imp)


def get_all_java_files(dirpath, walk_in=False):
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
                if name.endswith('.java'):
                    src_files.append(os.path.join(parent, name))
    else:
        for name in os.listdir(dirpath):
            if name.endswith('.java'):
                src_files.append(os.path.join(dirpath, name))

    return src_files


def transfer_all_java_files(dirpath):
    # tranfer all java files that generated by tcuml
    src_files = get_all_java_files(dirpath)
    # sort files
    src_files.sort()
    #print(src_files)
    output = os.path.abspath(dirpath) + '/tostring.txt'
    # clear the file
    with open(output, 'w') as f:
        f.write(LS)

    for filename in src_files:
        #output = filename.replace('/src/', '/fixed/')
        transfer_tcuml_file(filename, output)


def transfer_one_java_file(filepath):
    # tranfer one jave file
    #output = filepath.replace('.java', '_fixed.java')
    output = filepath.replace('.java', '_toString.txt')
    transfer_tcuml_file(filepath, output)


def usage():
    # Print the help message
    print('This is used to fixed the java doc for files that generated by tcuml.')
    print('It can transfer one java file.')
    print('It can also transfer all files in directory, dir must be \'/src/\'+package.')
    print('The command:')
    print('    -h print this message')
    print('    -i the file or path')
    print('The sample usage:')
    print('    trans_tcuml.py -i test.java')
    print('    trans_tcuml.py -i componet_dir')


opts, args = getopt.getopt(sys.argv[1:], 'hi:')
pathname = ''

for op, value in opts:
    if op == '-i':
        pathname = value
    elif op == '-h':
        usage()
        sys.exit()

if pathname:
    if os.path.isfile(pathname):
        transfer_one_java_file(pathname)
    elif os.path.isdir(pathname):
        transfer_all_java_files(pathname)
else:
    usage()
