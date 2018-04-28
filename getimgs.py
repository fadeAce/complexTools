#coding = utf-8
import urllib
import re

def getHtml(html):
    page = urllib.urlopen(html)
    html = page.read()
    return html

html = getHtml("http://club.qingdaonews.com/showAnnounce_27_3979506_1_0.htm")

print getHtml(html)