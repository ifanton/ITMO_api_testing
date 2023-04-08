import json

from api.client import Client


class Api(Client):
    USERS = '/users'  # создаем два атрибута USERS и BASE_URL
    BASE_URL = 'https://reqres.in/api'

    def list_users(self):  # метод принимает только self
        """
        :method:    get
        :rout:      /users?page=2
        :status:    200
        """
        url = self.BASE_URL + self.USERS + '?page=2'  # создает переменную url
        return self.get(url)  # возвращает вызов метода get из класса Client с созданным url

    def single_user_not_found(self):
        """
        :method:    get
        :rout:      /api/users/23
        :status:    404
        """
        url = self.BASE_URL + self.USERS + '/23'
        return self.get(url)

    def single_user(self):
        """
        :method:    get
        :rout:      /api/users/2
        :status:    200
        """
        url = self.BASE_URL + self.USERS + '/2'
        return self.get(url)

    def create(self, name: str, job: str):  # метод принимает name: str, job: str
        """
        :method:    post
        :rout:      /api/users/
        :status:    201
        :body:      {
                        "name": "",
                        "job": ""
                     }
        """
        url = self.BASE_URL + self.USERS  # генерирует url, payload и headers
        payload = json.dumps({
            "name": F"{name}",
            "job": F"{job}"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        return self.post(url, headers, payload)  # возвращает вызов метода post из класса Client

    def delete_user(self, id: int):
        """
        :method:    delete
        :rout:      /api/users/id
        :status:    204
        """
        url = self.BASE_URL + self.USERS + F"/{id}"
        return self.delete(url)


api = Api()
