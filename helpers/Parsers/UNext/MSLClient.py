# 旧: helpers/Parsers/Netflix/MSLClient.py
# MSLクライアントをU-NEXT用に変更
import requests

class UNextClient:
    def __init__(self):
        self.base_url = "https://video.unext.jp/"
    
    def get_license(self, challenge):
        license_url = f"{self.base_url}license"
        response = requests.post(license_url, data=challenge)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("License retrieval failed.")