from flask import Flask
import urllib3
from selectolax.parser import HTMLParser

app = Flask(__name__)

def modify_html(text, domain):
    tree = HTMLParser(text)
    tree.css_first('video').decompose()
    return tree.html


@app.route("/<target>")
def hello_world(target=None):
    print(target)

    # should handle exception
    resp = urllib3.request("GET", "https://"+target)
    
    return (modify_html(resp.data.decode(), target), resp.status)
