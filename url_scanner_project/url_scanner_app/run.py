import requests

url = 'http://localhost:8000/scan/'

scan_url = 'https://www.youtube.com'

data = {
    'url': scan_url
}

response = requests.post(url, data=data)

if response.status_code == 200:

    json_data = response.json()

    print('Status:', json_data['status'])
    print('Scan ID:', json_data['scan_id'])
else:
    
    print('Error:', response.text)
