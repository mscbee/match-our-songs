import os
from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    client_id = '455caa6c91784978888beca833756069'
    return redirect('https://accounts.spotify.com/authorize' + client_id)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
