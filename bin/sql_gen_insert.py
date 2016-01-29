#!/usr/bin/env python3

import sys
import getopt
import os

LS = os.linesep
INSERT_STR = 'INSERT INTO '
VALUES_STR = ' VALUES('
REPEAT_TIMES = 3
TIMESTAMP_FORMAT = "'2016-01-%02d 12:30:21'"
# This date format is for ORACLE
#TIMESTAMP_FORMAT = "to_date('2015-%02d-11 12:30:21', 'YYYY-MM-DD HH:MI:SS')"
#DATE_FORMAT = "to_date('2015-%02d-11', 'YYYY-MM-DD')"

NUMBER = ('int', 'bigint', 'tinyint', 'number', 'serial')
FLOAT = ('decimal', 'float', 'double')
STRING = ('varchar', 'text', 'clob')
BOOLEAN = ('boolean')
TIME = ('timestamp', 'datetime')
DATE = ('date')
BIT = ('bit')
IGNORE_WORD = ('create', 'primary', 'foreign', 'constraint', 'references', 'unique', 'on')


def transfer_sql(filepath):
    # Generate insert data for create.sql

    # Check the file whether exists and generate the del and drop file name
    if not os.path.isfile(filepath):
        print('The file path:' + filepath + ' is not exists')
        return False
    fname, fextension = os.path.splitext(filepath)
    if fextension != '.sql':
        print("The sql file's extenstion must be '.sql'")
        return False
    file_abs_dir = os.path.dirname(os.path.abspath(filepath))
    file_insert_tables = os.path.join(file_abs_dir, 'insert_gen.sql')

    # if insert file exits, ask user whether overwrite
    #if os.path.exists(file_insert_tables):
        #x = input('del or drop sql file exists, overwrite? Yes ').lower()
        #if x != '' and x != 'y' and x != 'yes':
            #return False

    # Get the tables names from input file and generate del and drop files
    #input_file = open(filepath, 'r').readlines()
    #out_insert_file = open(file_insert_tables, 'w')

    tables = {}
    tablenames = []
    flagInTable = False
    tablename = ''
    with open(filepath, 'r') as f1:
        line = f1.readline()
        while line:
            lowline = line.strip().lower()

            if len(lowline) != 0 and not lowline.startswith('--'):
                start_index = lowline.find('table ')
                if start_index > 0:
                    flagInTable = True
                    end_index = lowline.rfind(' ')
                    start_index = lowline.rfind(' ', 0, end_index-1)
                    #print('======%d    %d' %(start_index,end_index))
                    tablename = fix_name_in_table(lowline[start_index+1 : end_index])
                    tablenames.append(tablename)
                    tables[tablename] = []
                if lowline.strip() == ');':
                    flagInTable = False

                if flagInTable:
                    cols = lowline.split()
                    #print('============', cols)
                    if not cols[0] in IGNORE_WORD:
                        tables[tablename].append((fix_name_in_table(cols[0]),
                                                  rm_type(cols[1])))
            line = f1.readline()

    #print(tablenames)
    #print(tables)

    with open(file_insert_tables, 'w') as f2:
        for tname in tablenames:
            tdata = tables[tname]
            for i in range(REPEAT_TIMES):
                idx = str(i + 1)
                sql = INSERT_STR + tname + VALUES_STR
                for colname, coltype in tdata:
                    if colname.find('email') >= 0:
                        sql += "'bob" + idx + "@tc.com', "
                    elif colname == 'name':
                        sql += "'" + tname + idx + "', "
                    elif colname.find('phone') >= 0 or colname.find('fax') >= 0:
                        sql += "'123-456-" + (idx*3) + "', "
                    elif coltype in BOOLEAN:
                        if i % 2 == 0:
                            sql += 'true, '
                        else:
                            sql += 'false, '
                    elif coltype in BIT:
                        sql += str((i+1) % 2) + ', '
                    elif coltype in TIME:
                        sql += TIMESTAMP_FORMAT % (i+1) + ", "
                    elif coltype in DATE:
                        sql += DATE_FORMAT % (i+1) + ", "
                    elif coltype in NUMBER:
                        sql += idx + ', '
                    elif coltype in FLOAT:
                        sql += str(float(i+1)) + ', '
                    elif coltype in STRING:
                        sql += "'" + colname + idx + "', "
                    else:
                        sql += 'null, '
                sql = sql[:-2] + ');'
                print(sql)
                f2.write(sql + LS)
            print()
            f2.write(LS)

    print('Success to output file for insert sql data!')


def rm_type(type_str):
    res = type_str
    idx = res.find('(')
    if idx > 0:
        res = res[:idx]
    idx = res.find(',')
    if idx > 0:
        res = res[:idx]
    return res


def fix_name_in_table(name):
    if name.startswith('`') and name.endswith('`'):
        return name[1:-1]
    else:
        return name


def usage():
    # Print the help message
    print('This is used to generate insert data for create sql file.')
    print('The command:')
    print('    -h print this message')
    print('    -f the create sql file')
    print('The sample usage:')
    print('    sql_gen_insert.py -f create.sql')

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
