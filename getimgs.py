#coding = utf-8
# -*- coding: utf-8 -*-
# import requests
# url = 'https://github.com/ltfedware/complexTools'
# content = requests.get(url).content
# print content

import urllib2
from bs4 import BeautifulSoup
url="https://github.com/ltfedware/complexTools"
content=urllib2.urlopen(url)
soup=BeautifulSoup(content)
print soup