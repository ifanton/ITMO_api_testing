import requests


class Client:

    @staticmethod  # статический метод
    def get(url, timeout=5):  # метод принимает только url
        return requests.request('GET', url, timeout=timeout)  # возвращает ответ от сервера на запрос по переданному url

    @staticmethod
    def post(url, headers, payload, timeout=5):
        return requests.request('POST', url, headers=headers, data=payload, timeout=timeout)

    @staticmethod
    def delete(url, timeout=5):
        return requests.request('DELETE', url, timeout=timeout)
