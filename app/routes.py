import adal
from app import app
from flask import Flask, request, Response
import uuid
import requests

CLIENT_ID = 'a273ed9e-915c-4e0f-9109-ec2541deb7b5'
CLIENT_SECRET = 'F*denrd?/+pHjNV7lKcO6K309b?t9gHE'
BASEURL = 'http://localhost:3000'
RESOURCE = 'https://graph.microsoft.com'
API_VERSION = 'v1.0'
TENANT = 'am.amrita.edu'
AUTHORITY_URL = 'https://login.microsoftonline.com/' + TENANT
REDIRECT_URI = BASEURL + '/getAToken'
AUTHORIZE_URL = 'https://login.microsoftonline.com/am.amrita.edu/oauth2/authorize?'+'response_type=code&client_id='+ CLIENT_ID +'&redirect_uri='+BASEURL+'/getAToken'+'&'+'state={}'

@app.route("/")
def main():
    return "IDENTITY"

@app.route("/auth/")
def auth_begin():
    return "Hello"

@app.route("/id/authorize/")
def login():
    auth_state = str(uuid.uuid4())
    resp = Response(status=307)
    resp.headers['location'] = AUTHORIZE_URL.format(auth_state)
    return resp

@app.route("/getAToken")
def main_logic():
    code = request.args['code']
    auth_context = adal.AuthenticationContext(AUTHORITY_URL)
    token_response = auth_context.acquire_token_with_authorization_code(code, REDIRECT_URI, 'https://graph.microsoft.com', CLIENT_ID, CLIENT_SECRET)
    token = token_response['accessToken']
    print(token)
    endpoint = RESOURCE + '/' + API_VERSION + '/me/'
    http_headers = {'Authorization': 'Bearer ' + token,
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'client-request-id': str(uuid.uuid4())}
    print(http_headers)
    graph_data = requests.get(endpoint, headers=http_headers, stream=False).json()
    return graph_data