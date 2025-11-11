import requests
import json

# Your securely stored credentials
AA_CONTROL_ROOM_URL = "https://your-control-room.automationanywhere.com"
AA_CLIENT_ID = "YOUR_CLIENT_ID"
AA_CLIENT_SECRET = "YOUR_CLIENT_SECRET"

# Request a new access token
token_endpoint = f"{AA_CONTROL_ROOM_URL}/v1/authentication"
body = {
    "username": AA_CLIENT_ID,
    "password": AA_CLIENT_SECRET
}
headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(token_endpoint, headers=headers, json=body)
    response.raise_for_status()
    access_token = response.json().get("token")
    print(f"Retrieved Access Token: {access_token}")

    # Now you can use this access token for other API calls
    # For example:
    # api_endpoint = f"{AA_CONTROL_ROOM_URL}/v1/usermanagement/users/list"
    # authorized_headers = {
    #     "X-Authorization": access_token,
    #     "Content-Type": "application/json"
    # }
    # api_response = requests.get(api_endpoint, headers=authorized_headers)
    # print(api_response.json())

except requests.exceptions.RequestException as e:
    print(f"Error during authentication: {e}")