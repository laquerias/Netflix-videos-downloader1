from pywidevine.decrypt.wvdecryptcustom import WvDecrypt

class UNextKeyFetcher:
    def __init__(self, pssh_data):
        self.pssh_data = pssh_data

    def fetch_keys(self):
        wvdecrypt = WvDecrypt(init_data_b64=self.pssh_data)
        challenge = wvdecrypt.get_challenge()
        # U-NEXTライセンスサーバーのURLを使用
        license_url = "https://video.unext.jp/license"
        response = requests.post(license_url, data=challenge)
        if response.status_code != 200:
            raise Exception("Failed to fetch license from U-NEXT.")
        wvdecrypt.update_license(response.content)
        return wvdecrypt.start_process()