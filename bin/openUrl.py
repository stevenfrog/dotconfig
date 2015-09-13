#!/usr/bin/env python3

import urllib
import urllib.request

#from bs4 import BeautifulSoup

from pyquery import PyQuery as pq

#data={}
#data['word']='Jecvay Notes'

#url_values=urllib.parse.urlencode(data)
#url="https://www.topcoder.com/challenges/develop/active/?challengeTypes=Code&pageIndex=1"
#url="http://www.baidu.com"
url="http://www.baidu.com"
#full_url=url+url_values

html_doc=urllib.request.urlopen(url).read()
html_doc=html_doc.decode('UTF-8')
#print(html_doc)

#soup = BeautifulSoup(html_doc)
#d = pq(url='http://www.powereasy.net')
d = pq(html_doc)
#print(soup.prettify())

#print(d('#content'))
#print(d('#s_main .hot-content-cell li.words-li em.words-item-content').text())
print(d('#s_main .hot-content-cell'))

#for data in d('.hot-content-cell'):
#    print(pq(data).html())
