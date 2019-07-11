import adal
from app import app
from flask import Flask, request, Response
import uuid
import requests
from config import Config

CLIENT_ID = 'a273ed9e-915c-4e0f-9109-ec2541deb7b5'
CLIENT_SECRET = 'F*denrd?/+pHjNV7lKcO6K309b?t9gHE'
BASEURL = 'http://localhost:3000'
RESOURCE = 'https://graph.microsoft.com'
API_VERSION = 'v1.0'
TENANT = 'am.amrita.edu'
AUTHORITY_URL = 'https://login.microsoftonline.com/' + TENANT
REDIRECT_URI = BASEURL + '/getAToken'
AUTHORIZE_URL = 'https://login.microsoftonline.com/am.amrita.edu/oauth2/authorize?'+'response_type=code&client_id='+ CLIENT_ID +'&redirect_uri='+BASEURL+'/getAToken'+'&'+'state={}'

TEMP_AUTH = ''

@app.route("/")
def main():
    return "IDENTITY"


@app.route("/login")
def login():
    auth_state = str(uuid.uuid4())
    resp = Response(status=307)
    resp.headers['location'] = AUTHORIZE_URL.format(auth_state)
    return resp

@app.route("/getAToken")
def main_logic():
    code = request.args['code']
    auth_context = adal.AuthenticationContext(AUTHORITY_URL)
    token_response = auth_context.acquire_token_with_authorization_code(code, REDIRECT_URI, 'https://graph.microsoft.com',
                                                                        CLIENT_ID, CLIENT_SECRET)
    TEMP_AUTH = token_response['accessToken']
    return TEMP_AUTH

@app.route('/graphcall')
def graphcall():
    token = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6IkFRQUJBQUFBQUFBUDB3TGxxZExWVG9PcEE0a3d6U254d0t6SzROaktKNU53OHJDWXI5aXhTRThDXzBWdmhFZElXMllvVkdNZ2ltMkkyZ3o0RVJ5eGxETWFfS0tOYnRuaERKczBHZ09nbzB3Q215a2xxZUVJRENBQSIsImFsZyI6IlJTMjU2IiwieDV0IjoidTRPZk5GUEh3RUJvc0hqdHJhdU9iVjg0TG5ZIiwia2lkIjoidTRPZk5GUEh3RUJvc0hqdHJhdU9iVjg0TG5ZIn0.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yZDU0ODkwZi0xOGUzLTRjNzAtOTdjZC1iYzFlNWYyMWY5Y2IvIiwiaWF0IjoxNTYyODU4NzA5LCJuYmYiOjE1NjI4NTg3MDksImV4cCI6MTU2Mjg2MjYwOSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IjQyRmdZSGlZdWtWTGRHVzM2UkxwQ3Q2Rm9ReU1BbTFPc3gvR2UweWN5dWZwSmQwZTloa0EiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IklkZW50aXR5IiwiYXBwaWQiOiJhMjczZWQ5ZS05MTVjLTRlMGYtOTEwOS1lYzI1NDFkZWI3YjUiLCJhcHBpZGFjciI6IjEiLCJnaXZlbl9uYW1lIjoiTmFuZGFraXNob3JlIEoiLCJpcGFkZHIiOiIxODIuMTkuNDguMTgiLCJuYW1lIjoiTmFuZGFraXNob3JlIEoiLCJvaWQiOiJlODE5YzJmZS1hNDNiLTQ5NjYtYTljNS1lZmQ0ODUyZjU1YzAiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtNTkxODIyMDAxLTM5NDE5Nzk0OTAtMTUxNDY5MTQ3NC0yMDk5IiwicGxhdGYiOiIxNCIsInB1aWQiOiIxMDAzN0ZGRUFBOUE1MjE2Iiwic2NwIjoiVXNlci5SZWFkIiwic3ViIjoiY05JX0N2S29aY1BlZkdROURaV1Z5TVlWajZvaGJMY3loeGxNa2FDMmFTMCIsInRpZCI6IjJkNTQ4OTBmLTE4ZTMtNGM3MC05N2NkLWJjMWU1ZjIxZjljYiIsInVuaXF1ZV9uYW1lIjoibmFuZGFraXNob3JlQGFtLnN0dWRlbnRzLmFtcml0YS5lZHUiLCJ1cG4iOiJuYW5kYWtpc2hvcmVAYW0uc3R1ZGVudHMuYW1yaXRhLmVkdSIsInV0aSI6IkRrRTAwZEdyZVVxd1FWZGg3ZFVzQUEiLCJ2ZXIiOiIxLjAiLCJ4bXNfdGNkdCI6MTQ1NDM4OTI1OH0.WkjyNJvJtUI9Az-TeVopqF9BmdrT2OF9BDuwGIQawWmyU_GrTStAdiz2Kwg3ahiYmo5-zdhxvWEq6eikfMXIKUPYvQjEXdoMjiyJpri-p8jjbFBzQNpni6zxJZHh-3mtf4zxFB7f5SHxruBf6_5yRjhWNBwLa2qcDsEqIXVF7hauLlSz_zFFZQq_nGZSoKlWqYjCh4vlxPbVVcKXNKWqdBSaXvH2Ez6sWtZbE3QbbfSsLqSZxCFJGHra3TxufoqtLMKZd2R6M55CrhY3jsvJEmtSz48Dm_UMVnkcI8lNtcr8ryISVlWaNOc72RCUZSgxmYALb1R5mWFOZwzamX5rLg'
    endpoint = RESOURCE + '/' + API_VERSION + '/me/'
    http_headers = {'Authorization': 'Bearer ' + token,
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'client-request-id': str(uuid.uuid4())}
    print(http_headers)
    graph_data = requests.get(endpoint, headers=http_headers, stream=False).json()
    return graph_data

if __name__ == "__main__":
    app.run()
