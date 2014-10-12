#!/usr/bin/env python3

import sys
import getopt
import os
import re
# import my own script
import frogutil

LS = os.linesep


def gen_fields(filename):
    fields = []
    with open(filename, 'r') as f:
        p_field = re.compile('getAll(\w+?)\(\)')

        for line in f:
            striped_line = line.strip()

            m_field = p_field.match(striped_line)

            if m_field:
                fields.append(frogutil.word_remove_s(m_field.group(1)))

    for field in fields:
        print(field)


def usage():
    # Print the help message
    print('This is used to generate insert data for create sql file.')
    print('The command:')
    print('    -h print this message')
    print('    -f the create sql file')
    print('The sample usage:')
    print('    gen.py -f input.txt')

opts, args = getopt.getopt(sys.argv[1:], 'h:', ['field='])
input_file_name = ''

for op, value in opts:
    if op == '--field':
        gen_fields(value)
        print('------ Generate fields successfully ------')
        sys.exit()
    elif op == '-h':
        usage()
        sys.exit()
usage()
