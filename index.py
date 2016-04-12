from htmlgen import *
html=htmlgen.HTMLgen(pagelayout.getLayoutXML().decode('utf-8'),"Home Page")
html.addArticle("Markdown test","*Hello, World!*")
print(html.renderSite())
