import cgitb
import markdown2
cgitb.enable()
class HTMLgen:
    def __init__(self, layout, title):
        self.layout=layout
        self.articles=[]
        self.titles=[]
        self.title=title
    def addArticle(self, name, markdown):
        self.articles.append(markdown2.markdown(markdown))
        self.titles.append(name)
    def renderSite(self):
        nav=""
        x=0
        for title in self.titles:
            nav=nav+("<a href=\"#%i\">%s</a><br/>" % (x, title))
            x=x+1
        main=""
        x=0
        for article in self.articles:
            main=main+("<h2 id=\"%i\">%s</h2><article>%s</article>" %(x,self.titles[x],article))
            x=x+1
        styleargs = {"title":self.title,"nav":nav,"main":main,"aside":str(x),"footer":"Copyright 2016 Morten"}
        return self.layout%styleargs
