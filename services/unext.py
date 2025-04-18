import requests

class unext:
    def __init__(self, args, commands):
        self.base_url = "https://video.unext.jp/"
        self.logger = logging.getLogger(__name__)
        self.args = args
        self.commands = commands

    def get_manifest(self, content_id):
        url = f"{self.base_url}manifest/{content_id}"
        response = requests.get(url)
        if response.status_code != 200:
            self.logger.error("Failed to fetch U-NEXT manifest.")
            return None
        return response.json()