#!/usr/bin/env python3

import sys
import os
import re
from pyquery import PyQuery as pq
import frog_util

LS = os.linesep

d = pq(filename='/home/stevenfrog/ext_libdir/apache-tomcat-7.0.55/webapps/srt/partials/request.activities/coreUnified.html')


PACKAGES = [
    ('serviceRequest.coreUnifiedRequestData.block',   'core-unified-block'),
    ('serviceRequest.coreUnifiedRequestData.file',    'core-unified-file'),
    ('serviceRequest.coreUnifiedRequestData.feature', 'core-unified-feature'),
    ('serviceRequest.coreUnifiedRequestData.upgrade', 'core-unified-upgrade'),
    ('serviceRequest.coreUnifiedRequestData.esi',     'core-unified-esi')
]


elements = []
for services in d('div.step-content div.content-inner'):
    #for elm in pq(services).find('p label span.tip'):
    #    print('=== '+ pq(elm).parent().text())
    #    elements.append(pq(elm).parent().text())

    for elm in pq(services).parent().find('div.check-set label.chk-lbl'):
        text = '=CHECK== ' + pq(elm).text()
        print(text)
        elements.append(text)


for subtitle in d('div div.sub-title'):
    elements.append('')
    elements.append('######## ' + pq(subtitle).text())
    elements.append('')

    for elm in pq(subtitle).parent().find('p label span.tip'):
        labelEle = pq(elm).parent()
        prefix = ''
        idText = ''
        modelText = ''

        if (labelEle.parent().find('input:radio').length > 0):
            prefix = '=RADIO=='
            ele = pq(labelEle.parent().find('input:radio')[0])
            idText = ele.attr('name')
            modelText = ele.attr('data-ng-model')
        elif (labelEle.parent().find('select').length > 0):
            prefix = '=SELECT='
            ele = labelEle.parent().find('input:select')
            idText = ele.attr('id')
            modelText = ele.attr('data-ng-model')
        elif (labelEle.parent().find('input:checkbox').length > 0):
            prefix = '=CHECK=='
            ele = labelEle.parent().find('input:checkbox')
            idText = ele.attr('id')
            modelText = ele.attr('data-ng-model')
        elif (labelEle.parent().find('input:text').length > 0):
            prefix = '=NUM===='
            ele = labelEle.parent().find('input:text')
            idText = ele.attr('id')
            modelText = ele.attr('data-ng-model')
        else:
            prefix = '========'

        innerText = labelEle.text()

        #if(prefix == '======== '):
        #    print(prefix + innerText)


        if (prefix == '=SELECT='):
            #print(prefix + innerText)
            elements.append(prefix + innerText)
            for elm2 in labelEle.parent('p').find('select option'):
                optionText = pq(elm2).text()
                #print(optionText)
                elements.append(optionText)
        elif (prefix == '========' and (innerText.startswith('Select') or innerText.startswith('Include'))):
            elements.append('')
            prefix = '=CHKINF='
            elements.append((prefix, 'xxxxx', 'xxxxx', innerText))

            for elm2 in labelEle.parent().parent('div.check-set').find('input:checkbox'):
                prefix = '=CHKELM='
                ele = pq(elm2)
                idText = ele.attr('id')
                modelText = ele.attr('data-ng-model')
                innerText = ele.next().text()
                elements.append((prefix, modelText, idText, innerText))
            elements.append('')
        else:
            elements.append((prefix, modelText, idText, innerText))


    for elm in pq(subtitle).parent().find('div.select-row label span.tip'):
        elements.append('')
        elements.append('======== MULTISELECT')
        labelEle = pq(elm).parent()

        prefix = '=CHKINF='
        innerText = labelEle.text()
        elements.append((prefix, 'xxxxx', 'xxxxx', innerText))

        for elm3 in labelEle.parent('div.select-row').find('input:checkbox'):
            prefix = '=CHKELM='
            ele = pq(elm3)
            idText = ele.attr('id')
            modelText = ele.attr('data-ng-model')
            innerText = ele.next().text()
            elements.append((prefix, modelText, idText, innerText))
        elements.append('')




def adjustPrintArray(eleArrays, packages):
    resultArray = []
    currentPackage = 'xxx'
    currentIdPackage = 'xxx'
    for element in eleArrays:
        if isinstance(element, str):
            resultArray.append(element)
            continue

        elePackage = element[1]
        eleIdPackage = element[2]

        lastPtIdx = elePackage.rfind('.')

        if (not (elePackage.startswith(currentPackage))) or (lastPtIdx - len(currentPackage) > 1):
            packageIdx = -1
            for i in range(len(packages)):
                package = packages[i][0]
                idPackage = packages[i][1]
                if elePackage.startswith(package) and eleIdPackage.startswith(idPackage):
                    packageIdx = i

            if packageIdx != -1:
                currentPackage = packages[packageIdx][0]
                currentIdPackage = packages[packageIdx][1]

                lastPtIdx = elePackage.rfind('.')
                if lastPtIdx - len(currentPackage) > 1:
                    currentPackage = elePackage[:lastPtIdx]

                if isinstance(resultArray[-1], tuple) and resultArray[-1][0].startswith('=CHKINF='):
                    chkInfTxt = resultArray[-1]
                    resultArray[-1] = ('======== PACKAGE: ' + currentPackage + ', ' + currentIdPackage)
                    resultArray.append(chkInfTxt)
                else:
                    resultArray.append('')
                    resultArray.append('======== PACKAGE: ' + currentPackage + ', ' + currentIdPackage)
            else:
                currentPackage = 'xxx'
                currentIdPackage = 'xxx'


        if len(currentPackage) > 3:
            modelText = elePackage[(len(currentPackage)+1):]
            idText = eleIdPackage[(len(currentIdPackage)+1):]
            resultArray.append((element[0], modelText, idText, element[3]))
        else:
            resultArray.append(element)


    return resultArray


print('=======================================')
#for ele in elements:
#    print(ele)
#frog_util.printAlignedArray(elements, all_column_char='|')
result = adjustPrintArray(elements, PACKAGES)
frog_util.printAlignedArray(result, all_column_char='|')
