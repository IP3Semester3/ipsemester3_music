import json
import requests

from urllib.parse import urlencode
from flask import Flask, make_response, redirect, request

app = Flask(__name__)

# TODO: Security
secretkey = "410d6917d0de4fd8b1dc537fb0d8d55f"
access_key = ""
refreshcode = ""

webapiurl = "https://api.spotify.com/v1/me"


@app.route("/")
def getspotifyauthentication():
    spotify_url = "https://accounts.spotify.com/authorize"

    # TODO: Add scopes and state (for security)
    options = {
        'client_id': '7f9370bd0a3e4af797091179f9a526f7',
        'client_secret': secretkey,
        'response_type': 'code',
        'redirect_uri': 'http://127.0.0.1:5000/callback',
    }

    res = make_response(redirect(f'{spotify_url}/?{urlencode(options)}'))

    return res


@app.route("/callback")
def setup():
    global access_key
    if access_key == "":
        return generatetokens()

    header = {
        'Authorization': 'Bearer ' + access_key
    }

    req = requests.get(webapiurl, headers=header)

    return req.json()


def generatetokens():
    global access_key
    error = request.args.get('error')
    access_key = request.args.get('code')

    if error:
        return "Error while authenticating."

    spotifybody = {
        'grant_type': "authorization_code",
        'code': access_key,
        'redirect_uri': 'http://127.0.0.1:5000/callback'
    }

    # Generate access key and refresh token
    req = requests.post('https://accounts.spotify.com/api/token', auth=('7f9370bd0a3e4af797091179f9a526f7', secretkey),
                        data=spotifybody)

    print("!!! Response: ", req.json(), "This was the access_token used: ", access_key)

    reqjson = json.dumps(req.json())

    return checkauthcode(reqjson)


@app.route("/getplaylists")
def getplaylists():
    return 'response'


def checkauthcode(jsonpackage):
    global refreshcode
    global access_key
    response = json.loads(jsonpackage)

    if 'error' in response:
        if refreshcode != "":
            return refreshauthkey()
        # return redirect('/')
        return response['error_description']

    access_key = response['access_token']
    refreshcode = response['refresh_token']

    return response


def refreshauthkey():
    return 'Generate new key'
    # TODO: use refresh token to generate new access key


if __name__ == '__main__':
    app.run(host='0.0.0.0')
