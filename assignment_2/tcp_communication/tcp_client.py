import requests

url = "http://127.0.0.1:5001/api/chat"
payload = {"message": "Hello Server, this is a TCP request"}

try:
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Server Replied: {data['reply']}")
    else:
        print("Failed to connect.")

except Exception as e:
    print(f"Error: {e}")
