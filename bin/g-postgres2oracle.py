#!/usr/bin/env python3

import frog_util
import os
import re

LS = os.linesep
PREFIX_WHITE_SPACES = '    '
POSTGRES_FILE = '/home/stevenfrog/TC_Assembly_2015/SRT-HTML5/srf-cloud-app/src/main/sql/postgresql/update_coreunified.sql'


SEQUENCE_O = 'CREATE SEQUENCE S%s INCREMENT BY 1 START WITH 1000 NOMAXVALUE NOCYCLE;'
ID_O = 'id NUMBER NOT NULL PRIMARY KEY,'
TRIGGER_O = '''
CREATE TRIGGER T%(name)s
BEFORE INSERT ON %(name)s
FOR EACH ROW
when (new.id = 0 or new.id is null)
    BEGIN
        SELECT S%(name)s.NEXTVAL
        INTO   :new.id
        FROM   dual;
    END;
'''


SEQUENCE_CREATE_P = re.compile('CREATE SEQUENCE S(\w+) INCREMENT BY 1 START WITH 1000;')
TABLE_CREATE_P = re.compile('CREATE TABLE (\w+) \(')
ID_P = re.compile('id BIGINT NOT NULL PRIMARY KEY DEFAULT nextval\(\'\w+\'\),')
FIELD_P = re.compile('([a-z0-9_]+) (INT|BIGINT|BOOLEAN|DECIMAL\([\d, ]+\)|VARCHAR\(\d+\))( NOT NULL)?')
FOREIGN_KEY_P = re.compile('FOREIGN KEY [\w\d\(\)_]+ REFERENCES [\w\d\(\)_]+')


def transferPostgres2Oracle(filename):

    with open(filename, 'r') as f1:
        print('############################################################')

        currentTable = ''
        isTableEnd = False
        for line in f1:
            line = line.strip()

            if len(line) == 0:
                print()
            elif line == ');':
                print(line)
                isTableEnd = True

            if isTableEnd:
                print(TRIGGER_O % {'name': currentTable})
                isTableEnd = False
                continue

            if line.startswith('ALTER TABLE'):
                outline = line.replace('BIGINT', 'NUMBER')
                outline = outline.replace('BOOLEAN', 'NUMBER(1)')
                print(outline)
                continue

            if SEQUENCE_CREATE_P.match(line):
                regexRes = SEQUENCE_CREATE_P.match(line)
                print(SEQUENCE_O % regexRes.group(1))
                currentTable = ''
            elif TABLE_CREATE_P.match(line):
                regexRes = TABLE_CREATE_P.match(line)
                currentTable = regexRes.group(1)
                print(line)
            elif ID_P.match(line):
                print(PREFIX_WHITE_SPACES + ID_O)
            elif FOREIGN_KEY_P.match(line):
                print(PREFIX_WHITE_SPACES + line)
                if line.endswith(');'):
                    isTableEnd = True
            elif FIELD_P.match(line):
                regexRes = FIELD_P.match(line)
                fieldName = regexRes.group(1)
                fieldType = regexRes.group(2)

                outline = ''
                if fieldType.startswith('INT'):
                    outline = PREFIX_WHITE_SPACES + fieldName + ' INT'
                elif fieldType.startswith('BIGINT'):
                    outline = PREFIX_WHITE_SPACES + fieldName + ' NUMBER'
                elif fieldType.startswith('BOOLEAN'):
                    outline = PREFIX_WHITE_SPACES + fieldName + ' NUMBER(1)'
                elif fieldType.startswith('DECIMAL'):
                    outline = PREFIX_WHITE_SPACES + fieldName + ' DECIMAL(20, 2)'
                elif fieldType.startswith('VARCHAR'):
                    outline = PREFIX_WHITE_SPACES + fieldName + ' ' + fieldType

                if regexRes.group(3):
                    outline += ' NOT NULL'

                if line.endswith(','):
                    print(outline + ',')
                else:
                    print(outline)

                if line.endswith(');'):
                    print(');')
                    isTableEnd = True


if __name__ == '__main__':
    transferPostgres2Oracle(POSTGRES_FILE)
