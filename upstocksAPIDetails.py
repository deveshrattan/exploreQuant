import requests
from flask import session

def getAccessToken(api_key, api_secret, redirect_uri):
    # Upstox API endpoints
    base_url = "https://api-v2.upstox.com/login/authorization/dialog"
    token_url = "https://api-v2.upstox.com/login/authorization/token"

    # Step 1: Get the authorization code by opening the login URL in a web browser
    authorization_url = f"{base_url}?response_type=code&client_id={api_key}&redirect_uri={redirect_uri}"
    print(f"Open this URL in your web browser and authorize the application:\n{authorization_url}")

    # Step 2: Retrieve the authorization code after successful login
    authorization_code = input("Enter the authorization code from the URL: ")

    # Step 3: Exchange the authorization code for an access token
    token_data = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "redirect_uri": redirect_uri,
        "client_id": api_key,
        "client_secret": api_secret,
    }

    response = requests.post(token_url, data=token_data)

    if response.status_code == 200:
        access_token = response.json()["access_token"]
        return access_token
    else:
        print(f"Failed to obtain access token. Status code: {response.status_code}")
        print(response.text)

def testGetpositions():
    base_url = 'https://api.upstox.com/v2'
    api_url = f"{base_url}/portfolio/short-term-positions"
    token = session.get('access_token')
    payload={}
    headers = {
    'Accept': 'application/json',
    'Authorization' : f'Bearer {token}'
    }
    res = requests.get(api_url, headers = headers, data = payload)
    return res
