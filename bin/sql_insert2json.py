#!/usr/bin/env python3

import sys
import getopt
import os
import json


LS = os.linesep


TABLE_DEF = {
    'DEFAULT': ['id', 'name'],
    'Division': ['id', 'divisionName', 'emailAddress', 'shortName'],
    'pdmname': ['id', 'pdm_name', 'title', 'address1', 'address2', 'city', 'state', 'postalCode', 'officeNumber', 'faxNumber', 'mobileNumber', 'emailAddress', 'division'],
    'GeoState': ['id', 'geography', 'defaultDivision', 'defaultPdmname', 'name'],
    'DealQuestion': ['name', 'commentCondition', 'commentPlaceHolder', 'section'],
}


def sql_insert_to_json(filepath):
    # Check the file whether exists and generate the del and drop file name
    if not os.path.isfile(filepath):
        print('The file path:' + filepath + ' is not exists')
        return False
    fname, fextension = os.path.splitext(filepath)
    if fextension != '.sql':
        print("The SQL insert file's extenstion must be '.sql'")
        return False
    file_abs_dir = os.path.dirname(os.path.abspath(filepath))
    file_transfer_json = os.path.join(file_abs_dir, fname + '.json_str')

    table = {}
    with open(filepath, 'r') as f1:
        line = f1.readline()
        while line:
            line = line.strip()
            lowerline = line.lower()
            if len(line) != 0 and not line.startswith('#'):
                insert_idx = lowerline.find('insert into')
                values_idx = lowerline.find('values(')
                table_name = line[insert_idx + 11:values_idx].strip()

                open_curly = table_name.find('(')
                if open_curly >= 0:
                    close_curly = table_name.find(')')
                    table_content = table_name[open_curly + 1:close_curly]
                    table_name = table_name[0:open_curly]
                    if table_name not in TABLE_DEF.keys():
                        TABLE_DEF[table_name] = map(
                            strip, table_content.split(','))

                if table_name not in table.keys():
                    table[table_name] = []sssaaa;;eee

                end_idx = lowerline.find(');')
                table_value_str = line[values_idx + 6:end_idx + 1]

                table_value_str = table_value_str.replace(' true', ' True')
                table_value_str = table_value_str.replace(' false', ' False')

                table_value = eval(table_value_str)

                tableDef = TABLE_DEF['DEFAULT']
                if table_name in TABLE_DEF.keys():
                    tableDef = TABLE_DEF[table_name]

                if len(table_value) == len(tableDef):
                    res_json = dict(zip(tableDef, table_value))
                    table[table_name].append(res_json)

            line = f1.readline()

    with open(file_transfer_json, 'w') as f2:
        for name in table.keys():
            print("==============================")
            f2.write("==============================" + LS)
            print(name)
            f2.write(name + LS)
            json_res_str = json.dumps(table[name])
            print(json_res_str)
            f2.write(json_res_str + LS)
            print(LS)
            f2.write(LS)
        f2.close()

    print('--- Success to output file for inserting json data! ---')


def strip(s):
    return s.strip()


def usage():
    # Print the help message
    print('This is used to transfer SQL insert data to Mongoose json data.')
    print('The command:')
    print('    -h print this message')
    print('    -f the SQL insert file')
    print('')
    print('The sample usage:')
    print('    sql_insert2json.py -f insert_lookup.sql')


try:
    opts, args = getopt.getopt(sys.argv[1:], 'hf:', ['help'])
    input_file = ''

    for op, value in opts:
        if op == '-f':
            input_file = value
        elif op in ('-h', '--help'):
            usage()
            sys.exit()

    if input_file:
        sql_insert_to_json(input_file)
    else:
        usage()
except getopt.GetoptError:
    print('getopt error')
    usage()
    sys.exit()
