import requests
from tqdm import tqdm
import time
class Yandex_disk:

    def __init__(self, token_yandex):
        self.token_yandex = token_yandex

    def upload_photo_to_disk(self, list_photo_upload):
        self.list_photo_upload = list_photo_upload
        for i in tqdm(self.list_photo_upload):
            time.sleep(1)
        for photo in list_photo_upload:
            filename = photo['file_name']
            url_photo = photo['url_photo']
            path = f'/Photo VK/{filename}'
            upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token_yandex)}
            params = {'path': path, 'url': url_photo}
            resp = requests.post(upload_url, headers=headers, params=params)
            if resp.status_code == 202:
                print("Success")
