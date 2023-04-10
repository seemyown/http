import requests

url = f"https://api.stackexchange.com/2.3/questions?fromdate=1680912000&todate=1681084800&tagged=python&site=stackoverflow"
response = requests.get(url)
data = response.json()

for item in data['items']:
    print(item['title'])
