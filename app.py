import time
import urllib.request
from bs4 import BeautifulSoup

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    current_time = time.time()
    return "Hello World! I am raccoon. Current time is %s" % str(current_time)

@app.route("/get")
def get_remote_url():
    source_url = request.args.get('url')

    response = urllib.request.urlopen(source_url)
    data = response.read()      # a `bytes` object
    text = data.decode('utf-8') # a `str`; this step can't be used if data is binary

    soup = BeautifulSoup(text)
    wordpress_content = soup.find('div', {'id': 'content'})

    file = {
        'size': len(text),
        'content': text,
        'header': response.info(),
        'textonly': wordpress_content.text
    }
    return render_template('get.html', file=file)

@app.route("/myname")
def myname():
    name = request.args.get('name')

    return render_template('name.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
