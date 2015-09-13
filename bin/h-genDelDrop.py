#!/usr/bin/env python3

import frog_util
import os
import re

LS = os.linesep
PREFIX_WHITE_SPACES = '    '
POSTGRES_FILE = '/home/stevenfrog/TC_Assembly_2015/SRT-HTML5/srf-cloud-app/src/main/sql/postgresql/update_coreunified.sql'


TABLE_CREATE_P = re.compile('CREATE TABLE (\w+) \(')
DELETE_TABLE = 'DELETE FROM %s;'
DROP_TRIGGER = 'DROP TRIGGER T%s;'
DROP_SEQUENCE = 'DROP SEQUENCE S%s;'
DROP_TABLE = 'DROP TABLE %s;'

def generateDelDrop(filename):

    tableNames = []
    with open(filename, 'r') as f1:

        for line in f1:
            line = line.strip()

            regexRes = TABLE_CREATE_P.match(line)
            if regexRes:
                tableNames.append(regexRes.group(1))

    tableNames.reverse()
    print('############################################################')
    print('####   DELETE')
    print()
    for name in tableNames:
        print(DELETE_TABLE % name)

    print()
    print()
    print('############################################################')
    print('####   DROP Postgres')
    print()
    for name in tableNames:
        print(DROP_TABLE % name)
        print(DROP_SEQUENCE % name)

    print()
    print()
    print('############################################################')
    print('####   DROP Oracle')
    print()
    for name in tableNames:
        print(DROP_TRIGGER % name)
    print('------------------------------------------------------------')
    for name in tableNames:
        print(DROP_SEQUENCE % name)
    print('------------------------------------------------------------')
    for name in tableNames:
        print(DROP_TABLE % name)


if __name__ == '__main__':
    generateDelDrop(POSTGRES_FILE)
