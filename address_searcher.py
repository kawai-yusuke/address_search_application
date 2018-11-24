import requests

class AdressSearcher():
    def __init__(self):
        self.base_url = "http://zipcloud.ibsnet.co.jp/api/search"

    def search(self, postal_code):
        url = f"{self.base_url}?zipcode={postal_code}"

        response = requests.get(url)

        response_dict = response.json()

        都道府県 = response_dict["results"][0]["address1"]
        市区町村 = response_dict["results"][0]["address2"]
        町域 = response_dict["results"][0]["address3"]
        不存在 = response_dict["results"]

        if 不存在 == "null":
            return "該当する郵便番号は見つかりません"
        else:
            return f"{都道府県}{市区町村}{町域}"
