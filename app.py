import os
from flask import Flask
from redis import Redis
app = Flask(__name__)

redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

@app.route('/')
def hello_world():
    return 'Hello World. We\'re finally doing this'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
