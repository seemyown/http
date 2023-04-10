import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    # def upload_link(self, )

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать\
        ya_upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                    'Authorization': f'OAuth {self.token}'}
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(ya_upload_url, headers=headers, params=params)

        # print(response.json()["href"])
        upload = requests.put(response.json()["href"], file_path)
        # print(upload.status_code)
        if upload.status_code == 201:
            return "upload comlete"
        else:
            return "error"
        
        



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'some_file.txt'
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(open(path_to_file, 'rb'))
    print(result)