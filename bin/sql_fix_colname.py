#!/usr/bin/env python3

import sys
import getopt
import os

LS = os.linesep


def transfer_sql(filepath):
    # Fix column name of sql file
    # openReplyHost INT  --> open_reply_host INT

    # Check the file whether exists and generate the del and drop file name
    if not os.path.isfile(filepath):
        print('The file path:' + filepath + ' is not exists')
        return False
    fname, fextension = os.path.splitext(filepath)
    if fextension != '.sql':
        print("The sql file's extenstion must be '.sql'")
        return False
    file_abs_dir = os.path.dirname(os.path.abspath(filepath))
    file_fixed_tables = os.path.join(file_abs_dir, 'fixed_create.sql')

    # if insert file exits, ask user whether overwrite
    if os.path.exists(file_fixed_tables):
        x = input('fixed sql file name exists, overwrite? Yes ').lower()
        if x != '' and x != 'y' and x != 'yes':
            return False

    # fixed all column names in input file
    flagInTable = False
    filelines = []
    with open(filepath, 'r') as f1:
        line = f1.readline()
        while line:
            lowline = line.lower()
            start_index = lowline.find('table ')
            if start_index > 0:
                flagInTable = True
            if lowline.strip() == ');':
                flagInTable = False

            if flagInTable:
                colname = line.split()[0]
                #print(colname)
                start_idx = line.find(colname)
                end_idx = line.find(' ', start_idx)
                #print(line, start_idx, end_idx)
                res_str = ''
                for i in range(start_idx, end_idx):
                    if i == 0:
                        res_str += line[i]
                    elif line[i].isupper() and (line[i-1].islower() or line[i-1].isnumeric()):
                        res_str += '_' + line[i].lower()
                    else:
                        res_str += line[i]
                #print('====', res_str)
                line = line[:start_idx] + res_str + line[end_idx:]
                #print('rrrr', res_line)
                #cols = lowline.split()
                #print(cols)
                #if not cols[0] in IGNORE_WORD:
                    #tables[tablename].append((cols[0], rm_type(cols[1])))
            filelines.append(line)
            print(line, end='')
            line = f1.readline()

    with open(file_fixed_tables, 'w') as f2:
        f2.writelines(filelines)

    # print output file
    #with open(file_fixed_tables, 'r') as f3:
        #for line in f3:
            #print(line, end='')

    print('Success to output file for fixed column names!')


def rm_type(type_str):
    res = type_str
    idx = res.find('(')
    if idx > 0:
        res = res[:idx]
    idx = res.find(',')
    if idx > 0:
        res = res[:idx]
    return res


def usage():
    # Print the help message
    print('This is used to generate insert data for create sql file.')
    print('The command:')
    print('    -h print this message')
    print('    -f the create sql file')
    print('The sample usage:')
    print('    sql_fix_colname.py -f create.sql')

opts, args = getopt.getopt(sys.argv[1:], 'hf:')
create_sql_file = ''

for op, value in opts:
    if op == '-f':
        create_sql_file = value
    elif op == '-h':
        usage()
        sys.exit()

if create_sql_file:
    transfer_sql(create_sql_file)
else:
    usage()
