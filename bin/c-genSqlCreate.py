#!/usr/bin/env python3

from frog_java_util import get_java_structure
import frog_util
import frog_sql_util
import os

LS = os.linesep
JAVA_FILE = '''

/home/stevenfrog/TC_Assembly_2015/SRT-HTML5/srf-model/src/main/java/com/emc/gs/tools/srf/model/infrastructure/VnxClariionInformation.java

'''

for f in JAVA_FILE.splitlines():
    if not f:
        print('############################################################')
        continue
    print()
    java_structure = get_java_structure(f)

    print('========= package =================')
    print(java_structure['package'])
    print()
    print('========= class ===================')
    print(java_structure['class'][1])
    print()
    print('========= fields ==================')
    frog_util.printAlignedArray(java_structure['fields'])
    print()
    print(frog_sql_util.generateCreateSQL(java_structure))
    print()
    print()
