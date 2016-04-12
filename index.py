#!/usr/bin/env python3
from htmlgen import *
print("Content-type: text/html\r\n\r\n")
html=htmlgen.HTMLgen(pagelayout.getLayoutXML().decode('utf-8'),"Home Page")
html.addArticle("Markdown test","*Hello, World!*")
print(html.renderSite())
