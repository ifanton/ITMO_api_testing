from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert


def test_register_positive():
    email = 'eve.holt@reqres.in'
    password = '123'
    res = api.registration(email, password)

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res.json())


def test_register_negative():
    email = 'eve.holt@reqres.in'
    password = ''
    res = api.registration(email, password)
    res_body = res.json()

    assert res.status_code == HTTPStatus.BAD_REQUEST
    Assert.validate_schema(res.json())
    Assert.validate_schema(res_body)
    example = {
        "error": "Missing password"
    }
    assert example == res_body
