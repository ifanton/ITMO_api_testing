import requests


class Client:

    @staticmethod  # статический метод
    def get(url):  # метод принимает только url
        return requests.request('GET', url)  # возвращает ответ от сервера на запрос по переданному url

    @staticmethod
    def post(url, headers, payload):
        return requests.request('POST', url, headers=headers, data=payload)

    @staticmethod
    def delete(url):
        return requests.request('DELETE', url)
