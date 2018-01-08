import os
from flask import Flask, render_template, redirect, url_for, request
import requests
import base64
import urllib
import string
from random import *


app = Flask(__name__)

# For use in generating a random string for state (if I understand 'state' correctly)
allchar = string.ascii_letters + string.punctuation + string.digits



#  Client Keys
CLIENT_ID = "455caa6c91784978888beca833756069"
CLIENT_SECRET = "8e4df8b4372f4df6bb80a1dcba10b364"

# For authorizsation
REDIRECT_URI = "http://0.0.0.0:5000/callback/q"
SCOPE = "playlist-read-private user-library-read user top read"
RESPONSE_TYPE = "code"
STATE = "".join(choice(allchar) for num in range(randint(2, 6)))
print(STATE)
SHOW_DIALOG_bool = False
# TODO: remember to remove the client ID and secret before pushing

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)
# This is automatically set to false anyway but I'm including it as a learning exercise
# It prevents a previously authenticated user from going through the auth process again
SHOW_DIALOG_bool = False


auth_query_parameters = {
    "client_id": CLIENT_ID,
    "response_type": RESPONSE_TYPE,
    "redirect_uri": REDIRECT_URI,
    "state": STATE,
    "scope": SCOPE,
    "show_dialog": SHOW_DIALOG_bool
}


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
