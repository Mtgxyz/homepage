#!/usr/bin/env python3
from htmlgen import *
import storage
print("Content-type: text/html\r\n\r\n")
html=htmlgen.HTMLgen(pagelayout.getLayoutXML().decode('utf-8'),"Home Page")
count=storage.count("articles")
for i in range(count):
    try:
        article=storage.get("articles",i)
        if "anime" in article["tags"]:
            html.addArticle(**article)
    except:
        html.addArticle(**storage.get("articles",i), aid=i)

print("<!DOCTYPE html>")
print(html.renderSite())