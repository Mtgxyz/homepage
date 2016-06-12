import cgitb
import markdown2
import datetime
cgitb.enable()
class HTMLgen:
    def __init__(self, layout, title):
        self.layout=layout
        self.articles=[]
        self.titles=[]
        self.authors=[]
        self.dates=[]
        self.title=title
    def addArticle(self, name, markdown, author="darklink", date=0):
        self.articles.append(markdown2.markdown(markdown, extras=["tables","spoiler"]))
        self.titles.append(name)
        self.authors.append(author)
        self.dates.append(date)
    def renderSite(self):
        nav=""
        x=0
        for title in self.titles:
            nav=nav+("<a href=\"#%i\">%s</a><br/>" % (x, title))
            x=x+1
        main=""
        x=0
        for article in self.articles:
            main=main+("<h2 id=\"%i\">%s</h2><p>Written on <time datetime=\"%s\">%s</time> by %s</p><article>%s</article>" %(x,self.titles[x],datetime.datetime.fromtimestamp(self.dates[x]).strftime("%Y-%m-%d %H:%M:%S"),datetime.datetime.fromtimestamp(self.dates[x]).strftime("%c"),self.authors[x],article))
            x=x+1
        styleargs = {"title":self.title,"nav":nav,"main":main,"aside":str(x),"footer":"Copyright 2016 Morten"}
        return self.layout%styleargs
