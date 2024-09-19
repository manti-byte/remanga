import requests

def get_token(username, password, recaptcha_response):
    url = "https://api.remanga.org/api/users/login/"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/json'
    }
    data = {
        "user": username,
        "password": password,
        "g-recaptcha-response": recaptcha_response
    }

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        token = response.json().get('content', {}).get('access_token')
        if token:
            print(f"Your token: {token}")
            return token
        else:
            print("Error: ", response.json())
            return None
    else:
        print(f"Error {response.status_code}. Response: {response.text}")
        return None

username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
recaptcha_response = "WITHOUT_TOKEN" 

get_token(username, password, recaptcha_response)
