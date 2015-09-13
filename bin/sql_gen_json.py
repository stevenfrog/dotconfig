#!/usr/bin/env python3

import sys
import getopt
import os
import json

LS = os.linesep
DATA_NUMS = 3
TIMESTAMP_FORMAT = '2014-04-26 12:30:21'


def schema_to_gen_json(filepath):
    # Check the file whether exists and generate the del and drop file name
    if not os.path.isfile(filepath):
        print('The file path:' + filepath + ' is not exists')
        return False
    fname, fextension = os.path.splitext(filepath)
    if fextension != '.js':
        print("The Mongoose Schema file's extenstion must be '.js'")
        return False
    file_abs_dir = os.path.dirname(os.path.abspath(filepath))
    file_insert_json = os.path.join(file_abs_dir, fname+'.json')


    tdata = {}
    with open(filepath, 'r') as f1:
        line = f1.readline()
        while line:
            if len(line) != 0 and not line.startswith('//'):
                start_index = line.find('= new Schema({')
                if start_index > 0:
                    tdata = getBraketContent(f1)
            line = f1.readline()


    res_data = []
    num = 0
    for i in range(DATA_NUMS):
        num += 1
        res_data.append(fillDictValue(tdata, num))

    res_json = json.dumps(res_data)

    with open(file_insert_json, 'w') as f2:
        f2.write(res_json)
        f2.write(LS)

    print("-------------------------")
    print(res_json)
    print('--- Success to output file for inserting json data! ---')


def getBraketContent(file):
    line = file.readline().strip()
    bdata = {}
    while line:
        if len(line) != 0 and not line.startswith('//'):
            line = rmComma(line.strip())
            if line.endswith(': {'):
                cols = line.split(':')
                col1 = cols[0].strip()
                bdata[col1]=getBraketContent(file)

            elif line.endswith('}') or line.endswith('})'):
                if "type" in bdata:
                    return bdata["type"]
                else:
                    return bdata

            elif line.find(':') > 0:
                cols = line.split(':')
                col1 = cols[0].strip()
                col2 = cols[1].strip()

                bdata[col1]=col2

        line = file.readline()

    print("=== Error: schema should be end correctly ===")
    return "error"


def rmComma(str):
    if str.endswith(',') or str.endswith(';'):
        return str[:-1]
    else:
        return str


def fillDictValue(data, num):
    res = {}
    for colname, coltype in data.items():
        if coltype == 'Number':
            res[colname] = num
        elif coltype == 'Boolean':
            res[colname] = num % 2 == 1
        elif coltype == 'Date':
            res[colname] = TIMESTAMP_FORMAT
        elif coltype == 'String':
            if colname == 'email':
                res[colname] = colname + str(num) + '@test.com'
            elif colname.find('phone') >=0 or colname.find('fax') >= 0:
                res[colname] = '123-456-0' + str(num)
            else:
                res[colname] = colname + str(num)
        elif isinstance(coltype, dict):
            res[colname] = fillDictValue(coltype, num)
    return res;


def usage():
    # Print the help message
    print('This is used to generate json data for Mongoose Schema.')
    print('The command:')
    print('    -h print this message')
    print('    -f the Mongoose Schema file')
    print('The sample usage:')
    print('    sql_gen_json.py -f Profile.js')


try:
    opts, args = getopt.getopt(sys.argv[1:], 'hf:', ['help'])
    schema_file = ''

    for op, value in opts:
        if op == '-f':
            schema_file = value
        elif op in ('-h', '--help'):
            usage()
            sys.exit()

    if schema_file:
        schema_to_gen_json(schema_file)
    else:
        usage()
except getopt.GetoptError:
    print('getopt error')
    usage()
    sys.exit()
