from flask import Flask
import urllib3
from selectolax.parser import HTMLParser

app = Flask(__name__)

def modify_html(text, target):
    tree = HTMLParser(text)
    
    tree.css_first('video').decompose()
    
    for node in tree.css('a'):
        if 'href' in node.attrs:
            if node.attrs['href'] == '/':
                node.attrs['href'] = '/'+target
            # relative links
            elif node.attrs['href'].startswith('/'):
                node.attrs['href'] = "https://"+target + node.attrs['href']
    
    return tree.html


@app.route("/<target>")
def hello_world(target=None):
    print(target)
    
    # should handle exception
    resp = urllib3.request("GET", "https://"+target)
    
    return (modify_html(resp.data.decode(), target), resp.status)
