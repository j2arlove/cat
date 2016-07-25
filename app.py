#-*-coding:utf-8-*-
import time
import urllib.request
import re
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

    soup = BeautifulSoup(text,"html.parser")
    wordpress_content = soup.find('body')

    pattern = '사드는 국가안위와 오천만 국민의 생명이 직결되는 중요한 안보문제 임에도 불구하고 작금의 대한민국은 한미 사드배치 결정에 따라 근거없는 괴담으로 인해 온 나라가 몸살을 앓고 있다.'
    match = re.findall(pattern, wordpress_content.text)

    file = {
        'size': len(text),
        'content': match,
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
