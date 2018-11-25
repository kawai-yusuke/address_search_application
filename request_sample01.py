import requests

response = requests.get(url="http://hachimantai.spartacamp.jp")

data = response.json

# print(data["results"][0]["address1"])
# print(response)
print(data)
