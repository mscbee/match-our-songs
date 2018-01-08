import os
from flask import Flask, render_template, redirect, url_for, request
import requests
import base64
from urllib.parse import quote
import string
from random import *


app = Flask(__name__)

# For use in generating a random string for state (if I understand 'state' correctly)
allchar = string.ascii_letters + string.punctuation + string.digits



#  Client Keys
CLIENT_ID = <YOUR-CLIENT-ID>
CLIENT_SECRET = <YOUR-CLIENT-SECRET>

# For authorizsation
REDIRECT_URI = "http://0.0.0.0:5000/callback/"
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

    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
