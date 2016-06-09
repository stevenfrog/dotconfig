#!/usr/bin/env python3

import sys
import getopt
import os

LS = os.linesep
DELETE_STR = 'DELETE FROM '
#DROP_STR = 'DROP TABLE '
DROP_STR = 'DROP TABLE IF EXISTS '
DROP_SEQUENCE_STR = 'DROP SEQUENCE '


def transfer_sql(filepath):
    # Transfer create.sql into drop and delete tables

    # Check the file whether exists and generate the del and drop file name
    if not os.path.isfile(filepath):
        print('The file path:' + filepath + ' is not exists')
        return False
    fname, fextension = os.path.splitext(filepath)
    if fextension != '.sql':
        print("The sql file's extenstion must be '.sql'")
        return False
    file_abs_dir = os.path.dirname(os.path.abspath(filepath))
    file_del_tables = os.path.join(file_abs_dir, 'clear.sql')
    file_drop_tables = os.path.join(file_abs_dir, 'drop.sql')

    # if del or drop file exits, ask user whether overwrite
    if os.path.exists(file_del_tables) or os.path.exists(file_drop_tables):
        x = input('del or drop sql file exists, overwrite? Yes ').lower()
        if x != '' and x != 'y' and x != 'yes':
            return False

    # Get the tables names from input file and generate del and drop files
    input_file = open(filepath, 'r')
    out_del_file = open(file_del_tables, 'w')
    out_drop_file = open(file_drop_tables, 'w')

    tables = []
    sequences = []
    try:
        for line in input_file:
            lowline = line.lower()
            if not lowline.startswith('--'):
                start_index = lowline.find('table ')
                if start_index > 0:
                    end_index = lowline.rfind(' ')
                    start_index = lowline.rfind(' ', 0, end_index-1)
                    tablename = fix_db_table_name(line[start_index+1 : end_index])
                    tables.append(tablename)
                start_index = lowline.find('sequence ')
                if start_index > 0:
                    start_index += len('sequence ')
                    end_index = lowline.find(' ', start_index)
                    sequencename = fix_db_table_name(line[start_index : end_index])
                    sequences.append(sequencename)
        tables.reverse()
        sequences.reverse()

        for sequence in sequences:
            out_drop_file.write(DROP_SEQUENCE_STR + sequence + ';' + LS)
        for table in tables:
            out_del_file.write(DELETE_STR + table + ';' + LS)
            out_drop_file.write(DROP_STR + table + ';' + LS)
        print('Success to output file for clearing and droping sql ables!')
    finally:
        out_del_file.close()
        out_drop_file.close()
        input_file.close()


def fix_db_table_name(name):
    #if name.startswith('`') and name.endswith('`'):
    #    return name[1:-1]
    #else:
    #    return name
    return name



def usage():
    # Print the help message
    print('This is used to generate del and drop sql file from create sql file.')
    print('The command:')
    print('    -h print this message')
    print('    -f the create sql file')
    print('The sample usage:')
    print('    sql_gen_del_drop.py -f create.sql')


try:
    opts, args = getopt.getopt(sys.argv[1:], 'hf:', ['help'])
    create_sql_file = ''

    for op, value in opts:
        if op == '-f':
            create_sql_file = value
        elif op in ('-h', '--help'):
            usage()
            sys.exit()

    if create_sql_file:
        transfer_sql(create_sql_file)
    else:
        usage()
except getopt.GetoptError:
    print('getopt error')
    usage()
    sys.exit()
