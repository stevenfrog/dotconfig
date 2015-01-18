#!/usr/bin/env python3

import sys
import getopt
import os
import re
# import my own script
import frog_util

LS = os.linesep

INPUT_VALUES4 = '''
=CHKINF= |  isSrdfS              |  is_srdf_s               |  *** n. Select SAN Storage Network connectivity options: Pull down with multiple selections allowed
=CHKELM= |  isFibreChannel       |  is_dat_pro_adv          |  Fibre Channel
=CHKELM= |  isFcoe               |  is_fast_lun_mig         |  Fibre Channel over Ethernet (FCoE)
=CHKELM= |  isIscsi              |  is_mirror_view          |  iSCSI
=CHKELM= |  isSanExt             |  is_san_ext              |  SAN Extension
=CHKELM= |  isVsan               |  is_qua_ser_mag          |  Virtual SANs - VSAN/LSAN
=CHKELM= |  isFcRouting          |  is_repl_mag             |  FC Routing

'''

FIELDS = '''

is_srdf_s
is_fibre_channel
is_fcoe
is_iscsi
is_san_ext
is_vsan
is_fc_routing






'''


def gen_fields(input_values):
    for line in input_values.splitlines():
        line = line.strip()
        if len(line) == 0:
            print()
            continue
        if line.startswith('PACKAGE'):
            continue
        if line.startswith('PREFIX'):
            continue

        values = line.split('|')
        # remove useless white space
        for i in range(len(values)):
            values[i] = values[i].strip()

        print(frog_util.uncamel_name(values[1], '_'))



def usage():
    # Print the help message
    print('This is used to generate insert data for create sql file.')
    print('The command:')
    print('    -h print this message')
    print('    -f the create sql file')
    print('The sample usage:')
    print('    gen.py -f input.txt')

opts, args = getopt.getopt(sys.argv[1:], 'h:')
input_file_name = ''

#for op, value in opts:
#    if op == '-h':
#        usage()
#        sys.exit()
#    else:
#        gen_fields(INPUT_VALUES4)
#        print('------ Generate fields successfully ------')
#        sys.exit()
#usage()
gen_fields(INPUT_VALUES4)
print('------ Generate fields successfully ------')
#sys.exit()
