from flask import Flask, render_template, redirect, url_for, request
from urllib.parse import quote
from random import *
import os
import requests
import base64
import string
import json


app = Flask(__name__)

# For use in generating a random string for state (if I understand 'state' correctly)
allchar = string.ascii_letters + string.punctuation + string.digits



#  Client Keys
CLIENT_ID = <CLIENT_ID>
CLIENT_SECRET = <CLIENT_SECRET>

# For authorizsation
REDIRECT_URI = "http://localhost:3000/callback/" #TODO: whitelist the uri in Spotify Dev Dashboard
SCOPE = "playlist-read-private user-library-read"
RESPONSE_TYPE = "code"
# State is not required but highly recommended
STATE = "".join(choice(allchar) for num in range(randint(2, 6)))
# This is automatically set to false anyway but I'm including it as a learning exercise
# It prevents a previously authenticated user from going through the auth process again
SHOW_DIALOG_bool = False
# helps with encoding to utf-8 in url_args
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"


auth_query_parameters = {
    "client_id": CLIENT_ID,
    "response_type": RESPONSE_TYPE,
    "redirect_uri": REDIRECT_URI,
    "state": STATE,
    "scope": SCOPE,
    # "show_dialog": SHOW_DIALOG_str
}

@app.route('/')
def index():
    url_args = "&".join(["{}={}".format(key,quote(val.encode('utf-8'))) for key,val in auth_query_parameters.items()])
    return redirect("{}/?{}".format(SPOTIFY_AUTH_URL, url_args))

@app.route('/callback/')
def callback():
    auth_code = request.args['code']
    request_body_parameters = {
        "grant_type": "authorization_code",
        "code": str(auth_code),
        "redirect_uri": REDIRECT_URI
    }
    base_64_encoding = base64.b64encode("{}:{}".format(CLIENT_ID, CLIENT_SECRET).encode('utf-8'))
    header = {"Authorization": "Basic {}".format(base_64_encoding)}
    post_request = requests.post("https://accounts.spotify.com/api/token", data=request_body_parameters, headers=header)

    response_data = json.loads(post_request.text)




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
