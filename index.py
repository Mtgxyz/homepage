#!/usr/bin/env python3
from htmlgen import *
print("Content-type: text/html\r\n\r\n")
html=htmlgen.HTMLgen(pagelayout.getLayoutXML().decode('utf-8'),"Home Page")
html.addArticle("Markdown test","""*
* 1
* 2
* 3

# 1
# 2
# 3

## half adder truth table

|   | 0 | 1 |
|---|---|---|
| 0 |0 0|0 1|
| 1 |0 1|1 0|
""")
html.addArticle("Markdown test","""*Hello, World!*

test
test
**HI**
SPOILERS:
>! SPOILERED!
>! ロボボプラネットはいいぞ！

""")
html.addArticle("Markdown test","""*Hello, World!*

test
test
**HI**



**TEST**""")
html.addArticle("Markdown test","""*Hello, World!*

test
test
**HI**



**TEST**""")
html.addArticle("Markdown test","""*Hello, World!*

test
test
**HI**



**TEST**""")
html.addArticle("Markdown test","""*Hello, World!*

test
test
**HI**



**TEST**""")
html.addArticle("Markdown test","""*Hello, World!*

test
test
**HI**



**TEST**""")
html.addArticle("Markdown test","""*Hello, World!*

test
test
**HI**



**TEST**""")
html.addArticle("Markdown test","""*Hello, World!*

test
test
**HI**



**TEST**""")
html.addArticle("Markdown test","""*Hello, World!*

test
test
**HI**



**TEST**""")
html.addArticle("Markdown test","""*Hello, World!*

test
test
**HI**



**TEST**""")
print("<!DOCTYPE html>")
print(html.renderSite())
