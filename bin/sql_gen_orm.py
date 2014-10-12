#!/usr/bin/env python3

import sys
import getopt
import os

LS = os.linesep

PACKAGE = 'com.emc.gs.tools.srf.models.'
RETRACTION = '    '

NUMBER = ('int', 'bigint')
STRING = ('varchar')
BOOLEAN = ('boolean')
TIME = 'timestamp'
IGNORE_WORD = ('create', 'foreign')


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
    file_orm = os.path.join(file_abs_dir, 'orm_gen.xml')

    # if insert file exits, ask user whether overwrite
    #if os.path.exists(file_orm):
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
            lowline = line.lower()
            start_index = lowline.find('table ')
            if start_index > 0:
                flagInTable = True
                end_index = lowline.find(' ', start_index + 6)
                tablename = line[start_index + 6: end_index]
                tablenames.append(tablename)
                tables[tablename] = []
            if lowline.strip() == ');':
                flagInTable = False

            if flagInTable:
                cols = lowline.split()
                if not cols[0] in IGNORE_WORD:
                    tables[tablename].append((cols[0], rm_type(cols[1])))
            line = f1.readline()

    #print(tablenames)
    #print(tables)

    with open(file_orm, 'w') as f2:
        for tname in tablenames:
            tdata = tables[tname]
            xmlstr = RETRACTION + '<entity name="' + tname + '" class="' + PACKAGE + tname + '">' + LS
            xmlstr += RETRACTION*2 + '<table name="' + tname + '" />' + LS
            xmlstr += RETRACTION*2 + '<attributes>' + LS
            foreign_ids = []
            not_main_table_flag = tname.find('_') > 0
            list_table_flag = False
            map_table_flag = False

            for colname, coltype in tdata:
                if colname == 'id':
                    continue
                elif colname.endswith('_id'):
                    foreign_ids.append(colname)
                    continue
                elif colname == 'value':
                    list_table_flag = True
                elif colname == 'mapkey':
                    map_table_flag = True
                xmlstr += RETRACTION*3 + '<basic name="' + camel_colname(colname) + '">' + LS
                xmlstr += RETRACTION*4 + '<column name="' + colname + '" nullable="true" />' + LS
                xmlstr += RETRACTION*3 + '</basic>' + LS

            if not_main_table_flag and len(foreign_ids) == 2:
                strs = tname.split('_')
                xmlstr += RETRACTION*3 + '<one-to-many name="' + strs[1] + '" >' + LS
                xmlstr += RETRACTION*4 + '<join-table name="' + tname + '">' + LS
                xmlstr += RETRACTION*5 + '<join-column name="' + foreign_ids[0] + '" referenced-column-name="id" />' + LS
                xmlstr += RETRACTION*5 + '<inverse-join-column name="' + foreign_ids[1] + '" referenced-column-name="id" />' + LS
                xmlstr += RETRACTION*4 + '</join-table>' + LS
                xmlstr += RETRACTION*3 + '</one-to-many>' + LS
            elif not_main_table_flag and list_table_flag:
                if len(foreign_ids) < 1:
                    continue
                strs = tname.split('_')
                xmlstr += RETRACTION*3 + '<element-collection name="' + strs[1] + '">' + LS
                xmlstr += RETRACTION*4 + '<column name="value"/>' + LS
                xmlstr += RETRACTION*4 + '<collection-table name="' + tname + '" >' + LS
                xmlstr += RETRACTION*5 + '<join-column name="' + foreign_ids[0] + '" />' + LS
                xmlstr += RETRACTION*4 + '</collection-table>' + LS
                xmlstr += RETRACTION*3 + '</element-collection>' + LS
            elif not_main_table_flag and map_table_flag:
                if len(foreign_ids) < 1:
                    continue
                strs = tname.split('_')
                xmlstr += RETRACTION*3 + '<element-collection name="' + strs[1] + '" fetch="EAGER">' + LS
                xmlstr += RETRACTION*4 + '<map-key-column name="mapkey"/>' + LS
                xmlstr += RETRACTION*4 + '<column name="mapvalue"/>' + LS
                xmlstr += RETRACTION*4 + '<collection-table name="' + tname + '" >' + LS
                xmlstr += RETRACTION*5 + '<join-column name="' + foreign_ids[0] + '" />' + LS
                xmlstr += RETRACTION*4 + '</collection-table>' + LS
                xmlstr += RETRACTION*3 + '</element-collection>' + LS
            else:
                for colname in foreign_ids:
                        xmlstr += RETRACTION*3 + '<many-to-one name="' + camel_colname(colname[:-3]) + '">' + LS
                        xmlstr += RETRACTION*4 + '<join-column name="' + colname + '" />' + LS
                        xmlstr += RETRACTION*3 + '</many-to-one>' + LS

            xmlstr += RETRACTION*2 + '</attributes>' + LS
            xmlstr += RETRACTION + '</entity>' + LS
            xmlstr += LS

            print(xmlstr)
            print()
            f2.write(xmlstr)

    print('Success to output file for generating orm.xml!')


def rm_type(type_str):
    res = type_str
    idx = res.find('(')
    if idx > 0:
        res = res[:idx]
    idx = res.find(',')
    if idx > 0:
        res = res[:idx]
    return res


def camel_colname(colname):
    res = ''
    needUpper = False
    for c in colname:
        if needUpper:
            needUpper = False
            res += c.upper()
        elif c == '_':
            needUpper = True
        else:
            res += c
    return res


def usage():
    # Print the help message
    print('This is used to generate orm.xml for create sql file.')
    print('The command:')
    print('    -h print this message')
    print('    -f the create sql file')
    print('The sample usage:')
    print('    sql_gen_orm.py -f create.sql')

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
