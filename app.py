from flask import Flask
#from flask import render_template
import urllib3

app = Flask(__name__)

# https://stackoverflow.com/questions/38724132/remove-html-block-in-python
# this is brittle ... maybe use a real parser
def removeOneTag(text, tag):
    if "<"+tag+">" in text:
        return text[:text.find("<"+tag+">")] + text[text.find("</"+tag+">") + len(tag)+3:]
    else:
        return text[:text.find("<"+tag+" ")] + text[text.find("</"+tag+">") + len(tag)+3:]


@app.route("/<target>")
def hello_world(target=None):
    #return render_template("index.html")
    #return "<p>Hello, World!</p>"
    print(target)

    # should handle exception
    resp = urllib3.request("GET", "https://"+target)
    
    return (removeOneTag(resp.data.decode(), "video"), resp.status)
