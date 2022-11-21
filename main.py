import requests

class YaUploader:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, path):
        uri = 'v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def upload(self, file_path: str):
        name_file = file_path.split('/')[-1]
        request_url = self._get_upload_link(name_file)
        response = requests.put(request_url, data=open(file_path, 'rb'), headers=self.get_headers())

        if response.status_code == 201:
            print('Загрузка прошла успешно')
        else:
            print(response.status_code)



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input()
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
