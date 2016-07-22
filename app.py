import time

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    current_time = time.time()
    return "Hello World! I am raccoon. Current time is %s" % str(current_time)

if __name__ == "__main__":
    app.run()
