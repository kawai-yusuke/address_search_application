import requests

response = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111")

data = response.json()

print(data["results"][0]["address1"])
