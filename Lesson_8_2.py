import os
import requests
from pprint import pprint

TOKEN = ''

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
            }

    def get_files(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()


    def upload(self, path_to_file):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        file_name = os.path.basename(path_to_file)
        disk_path = f'disk:/{file_name}'
        params = {
            'path': disk_path,
            'overwrite': 'true'
        }
        response = requests.get(upload_url, headers = headers, params = params)
        answer = response.json()
        res = requests.put(answer['href'], data = open(path_to_file, 'rb'))
        res.raise_for_status()
        if res.status_code == 201:
            print('Файл загружен')
        

if __name__ == '__main__':     # Получить путь к загружаемому файлу и токен от пользователя

    path_to_file = 'c:/TEST/Lesson_8_2.txt'
    token = TOKEN

    uploader = YaUploader(token)
    uploader.upload(path_to_file)

   
    