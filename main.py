import base64
import json

import requests
from urllib.parse import urlencode
from flask import Flask, make_response, redirect, request, render_template

app = Flask(__name__)

# TODO: Security
secretkey = "[removed for security]"
access_key = ""

refreshcode = ""


@app.route("/")
def getspotifyauthentication():
    spotify_url = "https://accounts.spotify.com/authorize"

    options = {
        'client_id': '7f9370bd0a3e4af797091179f9a526f7',
        'client_secret': secretkey,
        'response_type': 'code',
        'redirect_uri': 'http://127.0.0.1:5000/callback',
    }

    res = make_response(redirect(f'{spotify_url}/?{urlencode(options)}'))

    return res


@app.route("/callback")
def returnresult():
    error = request.args.get('error')
    access_key = request.args.get('code')

    if error:
        return "Error while authenticating."

    spotifybody = {
        'grant_type': "authorization_code",
        'code': access_key,
        'redirect_uri': 'http://127.0.0.1:5000/callback'
    }

    req = requests.post('https://accounts.spotify.com/api/token', auth=('7f9370bd0a3e4af797091179f9a526f7', secretkey),
                        data=spotifybody)

    print("!!! Response: ", req.json())

    reqjson = json.dumps(req.json())

    return checkauthcode(reqjson)


def checkauthcode(jsonpackage):
    response = json.loads(jsonpackage)

    if 'error' in response:
        if refreshcode != "":
            return refreshauthkey()
        return redirect('/')

    return response

def refreshauthkey():
    return 'Generate new key'
    # TODO: use refresh token to generate new access key