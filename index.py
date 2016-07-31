#!/usr/bin/env python3
from htmlgen import *
import sys
import storage
print("Content-type: text/html\r\n\r\n")
html=htmlgen.HTMLgen(pagelayout.getLayoutXML().decode('utf-8'),"Home Page")
count=storage.count("articles")
for i in range(count):
    try:
        article=storage.get("articles",i)
        if "homepage" in article["tags"]:
            html.addArticle(**article)
    except:
        html.addArticle(aid=i, **storage.get("articles",i))

print("<!DOCTYPE html>")
sys.stdout.buffer.write(html.renderSite().encode('utf8'))
#print(html.renderSite())
