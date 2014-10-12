#!/usr/bin/env python3

import sys
import os
import re
from pyquery import PyQuery as pq
import frog_util

LS = os.linesep

d = pq(filename='/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/temp/CreateServiceRequestStep3Vipr.html')

print('=======================================')
print()

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
    print()
    print('### '+ pq(subtitle).text())
    elements.append('### '+ pq(subtitle).text())
    print()

    for elm in pq(subtitle).parent().find('p label span.tip'):
        labelEle = pq(elm).parent()
        prefix = ''
        if (labelEle.parent().find('input:radio').length > 0):
            prefix = '=RADIO== '
        elif (labelEle.parent().find('select').length > 0):
            prefix = '=SELECT= '
        #elif (labelEle.parent().parent().find('div.check-set input:checkbox').length > 0):
        #    prefix = '=CHECK== '
        else:
            prefix = '======== '
            
        innerText = labelEle.text()
        
        if (prefix == '=SELECT= '):
            print(prefix + innerText)
            elements.append(prefix + innerText)
            for elm2 in labelEle.parent('p').find('select option'):
                optionText = pq(elm2).text()
                print(optionText)
                elements.append(optionText)
        elif (prefix == '======== ' and (innerText.startswith('Select') or innerText.startswith('Include'))):
            prefix = '=CHKINF= '
            print(prefix + innerText)
            elements.append(prefix + innerText)
            for elm2 in labelEle.parent().parent('div.check-set').find('input:checkbox'):
                checkboxText = '=CHKELM= ' + pq(elm2).next().text()
                print(checkboxText)
                elements.append(checkboxText)
        else:
            print(prefix + innerText)
            elements.append(prefix + innerText)

print('=======================================')
