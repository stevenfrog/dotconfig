#!/usr/bin/env python3
"""
This class provide util method for java file.
"""

import sys
import getopt
import os
import re
import datetime
import unittest
# import my own script
import frog_util

LS = os.linesep
LINE_LEN = 80


def get_java_structure(filename):
    """
    Parse java file to structure.
    EX:
    {'package': packagename,
     'classdoc': ['classdoc1', 'classdoc2', ...]),
     'class': ('class|interface|enum', 'classname'),
     'fields': [(ftype, fname), ...],
     'methods': [(mtype, mname, mparam, mthrow), ...]}
    """

    java_structure = {}
    java_structure['package'] = ''
    java_structure['classdoc'] = []
    java_structure['class'] = None
    java_structure['fields'] = []
    java_structure['methods'] = []
    p_class = re.compile('(?:public|protected)(?:.*) (class|interface|enum) ([A-Za-z0-9_,<> ]+?)( extends [A-Za-z0-9_,<> ]+)? \{')
    p_field = re.compile('(?:public|protected|private)(?: static)?(?: final)? ([A-Za-z0-9_,<>\[\] ]+)( = [A-Za-z0-9_]+)?;')
    p_method = re.compile('(?:public|protected|private) ([A-Za-z0-9_,<>\[\] ]+?)\(([A-Za-z0-9_,<>\[\] ]*?)\)( throws \w+)?(?: \{|;)?')

    with open(filename, 'r') as f1:
        is_enum = False
        is_classdoc = False

        for line in f1:
            striped_line = line.strip()

            # find the package
            if striped_line[0:8] == 'package ' and striped_line[-1:] == ';':
                java_structure['package'] = striped_line[8:-1]
                continue

            # get class doc
            if java_structure['class'] is None and striped_line.startswith('/**'):
                is_classdoc = True
                continue
            if is_classdoc and striped_line.startswith('*/'):
                is_classdoc = False
                continue
            if is_classdoc:
                if len(striped_line) == 0 or len(striped_line) == 1:
                    continue
                java_structure['classdoc'].append(striped_line[2:])

            m_class = p_class.match(striped_line)
            m_field = p_field.match(striped_line)
            m_method = p_method.match(striped_line)

            if m_class:
                #print(m_class.groups())
                str_c = m_class.group(2)
                idx = str_c.find('<')
                if idx > 0:
                    java_structure['class'] = ((m_class.group(1), str_c[:idx]))
                else:
                    strs = m_class.group(2).split()
                    java_structure['class'] = (m_class.group(1), strs[0])
                is_enum = m_class.group(1) == 'enum'
            elif is_enum:
                if len(striped_line) == 0 or striped_line.startswith('/*')\
                        or striped_line.startswith('*') or striped_line.startswith('}'):
                    continue
                if striped_line.endswith(',') or striped_line.endswith(';'):
                    java_structure['fields'].append(('', striped_line[:-1]))
                else:
                    java_structure['fields'].append(('', striped_line))
            elif m_method:
                strs = m_method.group(1).split()
                strslen = len(strs)
                if strslen == 1:
                    # This is constructor
                    continue
                elif strslen == 2:
                    mtype = strs[0]
                    mname = strs[1]
                else:
                    mtype = strs[0]
                    for i in range(1, strslen-1):
                        mtype += ' ' + strs[i]
                    mname = strs[-1]
                #strs2 = m_method.group(1).split()
                str_throw = None
                if m_method.group(3):
                    str_throw = m_method.group(3).split()[1]
                java_structure['methods'].append((mtype, mname, m_method.group(2), str_throw))
            elif m_field:
                f_str = m_field.group(1)
                idx = f_str.rfind('>')
                if idx > 0:
                    java_structure['fields'].append((f_str[:idx+1], f_str[idx+2:]))
                else:
                    strs = m_field.group(1).split()
                    java_structure['fields'].append((strs[0], strs[1]))

    # print('========= package ===============')
    # print(java_structure['package'])
    # print('========= class doc ===============')
    # print(java_structure['classdoc'])
    # print('========= class ===============')
    # print(java_structure['class'])
    # print('========= fields ==============')
    # for ftype, fname in java_structure['fields']:
    #     print(ftype, "--", fname)
    # print('========= methods =============')
    # for mtype, mname, mparam, mthrow in java_structure['methods']:
    #     print(mtype, '--', mname, '--', mparam, '--', mthrow, '--')
    # print('+++++++++++++++++++++++++++++++')

    return java_structure


def generate_tostring(fields):
    res = '/**' + LS
    res += ' * The toString method.' + LS
    res += ' *' + LS
    res += ' * @return the string for this entity' + LS
    res += ' */' + LS
    res += '@Override' + LS
    res += 'public String toString() {' + LS
    res += '    StringBuilder sb = new StringBuilder();' + LS
    res += '    sb.append("{").append(super.toString());' + LS

    l = len(fields)
    for i in range(l):
        ftype, fname = fields[i]
        if i == l-1:
            res += '    sb.append(", ' + fname + ':").append(' + fname + ').append("}");' + LS
        else:
            res += '    sb.append(", ' + fname + ':").append(' + fname + ');' + LS
    res += '    return sb.toString();' + LS
    res += '}' + LS + LS
    return res


def generate_header():
    # create the tocpder header
    today = datetime.date.today()
    header = '/*' + LS + ' * Copyright (C) '
    header += today.strftime('%Y')
    header += ' TopCoder Inc., All Rights Reserved.' + LS + ' */' + LS
    return header


def generate_package(package_name):
    return 'package ' + package_name + ';' + LS + LS


def generate_class_doc(class_docs, designer, developer):
    # Transfer the java doc for class part
    result = '/**' + LS
    result += ' * <p>' + LS
    is_thread_safety = False
    for line in class_docs:
        #lower_line = line.lower()
        if line.lower().find('thread safety') != -1:
            is_thread_safety = True
            result += ' * </p>' + LS + ' * <p>' + LS + ' * <b>Thread Safety:</b> '
            continue

        line = correct_invalid_char(line)
        line = add_last_period(line)
        line = split_long_line(line)
        if not is_thread_safety:
            result += ' * ' + line + '<br>' + LS
        else:
            result += line

    result += LS + ' * </p>' + LS   # The first LS is for thread safety
    result += ' *' + LS
    result += ' * @author ' + designer + ', ' + developer + LS
    result += ' * @version 1.0' + LS
    result += ' */' + LS
    return result


def generate_field_doc(field_name):
    res = '    /**' + LS
    res += '     * <p>' + LS
    res += '     * The ' + field_name + '.' + LS
    res += '     * </p>' + LS
    res += '     */' + LS
    return res


def generate_constructor(class_name):
    res = '    /**' + LS
    res += '     * <p>' + LS
    res += '     * The default constructor.' + LS
    res += '     * </p>' + LS
    res += '     */' + LS
    res += '    public ' + class_name + '() {' + LS
    res += '       // Empty' + LS
    res += '    }' + LS + LS
    return res


def generate_getter_setter(ftype, fname):
    res = '    /**' + LS
    res += '     * <p>' + LS
    res += '     * Retrieves the ' + fname + ' field.' + LS
    res += '     * </p>' + LS
    res += '     *' + LS
    res += '     * @return the ' + fname + LS
    res += '     */' + LS
    if ftype == 'boolean':
        #if fname.startswith('is') and fname[2].isupper():
            #res += '    public ' + ftype + ' ' + fname + '() {' + LS
        #else:
            #res += '    public ' + ftype + ' is' + fname[0].upper() + fname[1:] + '() {' + LS
        res += '    public ' + ftype + ' is' + fname[0].upper() + fname[1:] + '() {' + LS
    else:
        res += '    public ' + ftype + ' get' + fname[0].upper() + fname[1:] + '() {'+ LS
    res += '       return ' + fname + ';' + LS
    res += '    }' + LS + LS
    res += '    /**' + LS
    res += '     * <p>' + LS
    res += '     * Sets the value to ' + fname + ' field.' + LS
    res += '     * </p>' + LS
    res += '     *' + LS
    res += '     * @param ' + fname + LS
    res += '     *            the ' + fname + LS
    res += '     */' + LS
    #if ftype == 'boolean' and fname.startswith('is') and fname[2].isupper():
        #res += '    public void set' + fname[2:] + '() {' + LS
    #else:
        #res += '    public void set' + fname[0].upper() + fname[1:] + '(' + ftype + ' ' + fname + ') {' + LS
    res += '    public void set' + fname[0].upper() + fname[1:] + '(' + ftype + ' ' + fname + ') {' + LS
    res += '       this.' + fname + ' = ' + fname + ';' + LS
    res += '    }' + LS + LS
    return res


def add_last_period(line):
    # add '.' in the end of line
    if not line.endswith('.'):
        return line + '.'
    else:
        return line


def correct_invalid_char(line):
    # change '<' '>' into html string
    temp = line.replace('<', '&lt;')
    return temp.replace('>', '&gt;')


def split_long_line(line):
    # split long line into several
    if  len(line) <= LINE_LEN:
        return line

    n = LINE_LEN
    tmp = line
    while n < len(tmp):
        idx = tmp.rfind(' ', (n-LINE_LEN), n)
        tmp = tmp[0:idx] + LS + ' * ' + tmp[idx+1:]
        n += LINE_LEN
    return tmp


class TestSelfFuntions(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_java_structure(self):
        filename = 'test_files/Customer.java'
        js = get_java_structure(filename)
        self.assertEqual(js['package'], 'com.emc.gs.tools.srf.models')
        self.assertTrue('This is Customer entity class.' in js['classdoc'])
        self.assertTupleEqual(('class', 'Customer'), js['class'])
        self.assertTrue(('String', 'name') in js['fields'])
        self.assertTrue(('String', 'email') in js['fields'])
        self.assertTrue(('State', 'state') in js['fields'])
        self.assertTrue(('Date', 'servicesAgreementDate') in js['fields'])
        self.assertTrue(('List<CustomerWorkSite>', 'customerWorkSites') in js['fields'])
        self.assertTrue(('String', 'getName', '', None) in js['methods'])
        self.assertTrue(('void', 'setName', 'String name', None) in js['methods'])
        self.assertTrue(('Country', 'getCountry', '', None) in js['methods'])
        self.assertTrue(('void', 'setCountry', 'Country country', None) in js['methods'])
        self.assertTrue(('String', 'getServicesAgreementNote', '', None) in js['methods'])
        self.assertTrue(('String', 'toString', '', None) in js['methods'])

    def test_get_java_structure2(self):
        filename = 'test_files/ReplicationManagerInformation.java'
        js = get_java_structure(filename)
        self.assertEqual(js['package'], 'com.emc.gs.tools.srf.models.bc')
        self.assertTupleEqual(('class', 'ReplicationManagerInformation'), js['class'])
        self.assertTrue(('boolean', 'snapViewManaged') in js['fields'])
        self.assertTrue(('Integer', 'replicatedStorageSize') in js['fields'])
        self.assertTrue(('String', 'customScriptingDetails') in js['fields'])
        self.assertTrue(('boolean', 'snapViewManaged') in js['fields'])
        self.assertTrue(('ConfigChangeType', 'configChangeType') in js['fields'])
        self.assertTrue(('Map<String, Integer>', 'databaseNumber') in js['fields'])
        self.assertTrue(('boolean', 'isTimeFinderManaged', '', None) in js['methods'])
        self.assertTrue(('void', 'setTimeFinderManaged', 'boolean timeFinderManaged', None) in js['methods'])
        self.assertTrue(('void', 'setConfigChangeType', 'ConfigChangeType configChangeType', None) in js['methods'])
        self.assertTrue(('Map<String, Integer>', 'getDatabaseNumber', '', None) in js['methods'])
        self.assertTrue(('String', 'getCustomScriptingDetails', '', None) in js['methods'])
        self.assertTrue(('String', 'toString', '', None) in js['methods'])

    def test_get_java_structure3(self):
        filename = 'test_files/SrdfArrayInformation.java'
        js = get_java_structure(filename)
        self.assertEqual(js['package'], 'com.emc.gs.tools.srf.models.bc')
        self.assertTupleEqual(('class', 'SrdfArrayInformation'), js['class'])
        self.assertTrue(('List<Integer>', 'replicateSize') in js['fields'])
        self.assertTrue(('List<SrdfMode>', 'currentSrdfMode') in js['fields'])
        self.assertTrue(('List<String>', 'targetName') in js['fields'])
        self.assertTrue(('List<Boolean>', 'getExistingOptionEnabled', '', None) in js['methods'])
        self.assertTrue(('List<SrdfMode>', 'getNewSrdfMode', '', None) in js['methods'])
        self.assertTrue(('void', 'setNewSrdfMode', 'List<SrdfMode> newSrdfMode', None) in js['methods'])
        self.assertTrue(('List<String>', 'getTargetName', '', None) in js['methods'])
        self.assertTrue(('void', 'setTargetName', 'List<String> targetName', None) in js['methods'])
        self.assertTrue(('String', 'toString', '', None) in js['methods'])

    def test_get_java_structure4(self):
        filename = 'test_files/SortOrder.java'
        js = get_java_structure(filename)
        self.assertTrue('This is SortOrder enum class.' in js['classdoc'])
        self.assertTupleEqual(('enum', 'SortOrder'), js['class'])
        self.assertTrue(('', 'ASC') in js['fields'])
        self.assertTrue(('', 'DESC') in js['fields'])
        self.assertEqual(0, len(js['methods']))

    def test_get_java_structure5(self):
        filename = 'test_files/RequestService.java'
        js = get_java_structure(filename)
        self.assertEqual(js['package'], 'com.emc.gs.tools.srf.services')
        self.assertTupleEqual(('interface', 'RequestService'), js['class'])
        self.assertEqual(0, len(js['fields']))
        self.assertTrue(('StartRequestData', 'getStartRequestData', '', 'ServiceRequestToolException') in js['methods'])
        self.assertTrue(('BcRequestData', 'getBcRequestData', 'long requestId', None) in js['methods'])
        self.assertTrue(('UnifiedRequestData', 'getUnifiedRequestData', 'long requestId', 'ServiceRequestToolException') in js['methods'])
        self.assertTrue(('SearchResult<Request>', 'search', 'RequestSearchCriteria criteria', 'ServiceRequestToolException') in js['methods'])

    def test_get_java_structure6(self):
        filename = 'test_files/GenericService.java'
        js = get_java_structure(filename)
        self.assertTrue('This interface defines a generic contract for managing an entity. It is responsible for creating, updating, deleting' in js['classdoc'])
        self.assertTupleEqual(('interface', 'GenericService'), js['class'])
        self.assertEqual(0, len(js['fields']))
        self.assertTrue(('T', 'create', 'T entity', 'ServiceRequestToolException') in js['methods'])
        self.assertTrue(('T', 'update', 'T entity', 'ServiceRequestToolException') in js['methods'])
        self.assertTrue(('void', 'delete', 'long[] ids', 'ServiceRequestToolException') in js['methods'])
        self.assertTrue(('T', 'get', 'long id', None) in js['methods'])


if __name__ == '__main__':
    unittest.main()
