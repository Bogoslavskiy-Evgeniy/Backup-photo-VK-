import requests
import json

class Backup_photo:

    def __init__(self, id_VK):
        self.id_VK = id_VK
        self.token_VK = .....

    def get_photo(self):
        URL = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': self.id_VK,
            'album_id': 'profile',
            'access_token': self.token_VK,
            'v': '5.131',
            'extended': '1',
            'photo_sizes': '1',
            'count': '4'
          }
        res = requests.get(URL, params=params)
        response = res.json()
        return response

    def list_photo(self):
        list_photo_json = self.get_photo()
        list_all_photo = []
        items = list_photo_json['response']['items']
        for element in items:
            dict_photo = {}
            file_name = element['likes']['count']
            date = element['date']
            dict_photo['file_name'] = f'{file_name}.jpg'
            for part in element['sizes']:
                type = part['type']
                if type == 'z':
                    url = part['url']
                    dict_photo['url_photo'] = url
                    dict_photo['size'] = 'z'
            for photo_file in list_all_photo:
                if dict_photo['file_name'] == f'{file_name}.jpg':
                    dict_photo['file_name'] = f'{file_name}.{date}.jpg'
            list_all_photo.append(dict_photo)
        return list_all_photo

    def photo_json(self, ):
        list_photo_1 = self.list_photo()
        file_photo = []
        for el in list_photo_1:
            del (el['url_photo'])
            file_photo.append(el)
        with open('photo_file.json', 'w') as f:
            json.dump(file_photo, f)
        with open('photo_file.json', 'r') as file:
            print(file.read())