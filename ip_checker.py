import requests

def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        return response.json()['ip']
    except requests.RequestException as e:
        return f"Error: {e}"

print(f"My Public IP Address: {get_public_ip()}")