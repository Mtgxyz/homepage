#!/usr/bin/env python3
from htmlgen import *
import traceback
import storage
import cgi
import random
import base64
from io import BytesIO
from captcha.image import ImageCaptcha
import time, string
print("Content-type: text/html\r\n\r\n")
form=cgi.FieldStorage()
aid=int(form["aid"].value)
try:
    seed=int(form["seed"].value)
    random.seed(seed)
    checkstr="".join(random.choice(string.digits+string.ascii_lowercase) for _ in range(5))
    if not checkstr == form["checkstr"].value:
        print("Captcha's wrong")
        raise Exception()
    username=form["username"].value
    message=form["message"].value
    timestamp=int(time.time())
    data={"name":form["title"],"markdown":message,"author":username,"date":timestamp}
    storage.append("comments-%i"%aid,data)
except KeyError:
    pass


seed=random.SystemRandom().randint(0,2**24)
random.seed(seed)
checkstr="".join(random.choice(string.digits+string.ascii_lowercase) for _ in range(5))
image = ImageCaptcha()
capt = image.generate(checkstr)
html=htmlgen.HTMLgen(pagelayout.getLayoutXML().decode('utf-8'),"Comments")
html.appendHTML("<form action=\"comments.py?aid=%i\" method=\"POST\">"%aid)
html.appendHTML("<input type=\"hidden\" name=\"seed\" value=\"%i\" />"%seed)
html.appendHTML("<input placeholder=\"Username\" name=\"username\" /><br />")
html.appendHTML("<input placeholder=\"Title\" name=\"title\" /><br />")
html.appendHTML("<textarea name=\"message\" placeholder=\"Compose your message. Markdown is enabled.\" ></textarea><br />")
html.appendHTML("<img src=\"data:image/png;base64,%s\" alt=\"Captcha image\" />" % base64.b64encode(capt.getvalue()).decode("UTF-8"))
html.appendHTML("<input placeholder=\"Captcha. lowercase only. case sensitive\" name=\"checkstr\" />")
html.appendHTML("<input type=\"submit\" /></form>")
count=storage.count("comments-%i"%aid)
for i in range(count):
    html.addArticle(**(storage.get("comments-%i"%aid,i)))

print("<!DOCTYPE html>")
print(html.renderSite(True))
