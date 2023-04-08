from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert


def test_list_users():
    res = api.list_users()  # переменная ответа от сервера

    assert res.status_code == HTTPStatus.OK  # Проверяем статус ответа
    Assert.validate_schema(res.json())  # Проверяем валидность json


def test_single_user_not_found():
    res = api.single_user_not_found()

    assert res.status_code == HTTPStatus.NOT_FOUND
    Assert.validate_schema(res.json())


def test_single_user():
    res = api.single_user()
    res_body = res.json()  # переменная тела ответа

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res_body)

    assert res_body["data"]["first_name"] == "Janet"  # проверка соответствия отдельной строки ответа
    example = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    assert example == res_body  # проверка соответствия на все тело ответа


def test_create():  # тест на запрос создания пользователя (метод create класса api и передадим в него тестовые данные)
    name = 'Anton'  # тестовые данные
    job = 'Tester'
    res = api.create(name, job)

    assert res.status_code == HTTPStatus.CREATED  # проверяем статус ответа
    assert res.json()['name'] == name  # проверяем данные ответа
    assert res.json()['job'] == job

    assert api.delete_user(res.json()['id']).status_code == HTTPStatus.NO_CONTENT  # Добавим удаление созданной записи
