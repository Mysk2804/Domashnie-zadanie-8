import requests
from pprint import pprint
import os

TOKEN ="2619421814940190"


def intelligence_super_heroys(super_names):
    intelekt_heroys = {}
    for super_name in super_names:
        url = "https://superheroapi.com/api/" + TOKEN + "/search/" + super_name
        response = requests.get(url).json()
        power = response['results'][0]['powerstats']['intelligence']
        intelekt_heroys[super_name] = power
    # print(intelekt_heroys)
    znach_intelekta = 0
    name_hero = ''
    for name, intelekt in intelekt_heroys.items():
        i = int(intelekt)
        if i >= znach_intelekta:
            znach_intelekta = i
            name_hero = name
        else:
            pass
    print(f'Самый интелектуальный супер герой {name_hero}')

if __name__ == '__main__':
    super = intelligence_super_heroys(['Hulk', 'Captain America', 'Thanos'])



class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _upload_pro(self, file):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": file, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def upload(self, loadfile, savefale):
        href = self._upload_pro(file=loadfile).get("href", "")
        resource = requests.put(href, data=open(savefale, 'rb'))
        resource.raise_for_status()


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file = "text.txt"
    path_to_file = os.path.join(os.getcwd(), 'ext.txt')
    token = ''
    uploader = YaUploader(token)
    pprint(uploader.upload(file, path_to_file))

