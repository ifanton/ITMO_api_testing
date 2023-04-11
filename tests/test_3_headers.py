import allure
import re

from api.httpbin_api import http_bin_api
from http import HTTPStatus
from utils.assertions import Assert


@allure.feature('test_list_html')
@allure.story('Отправка GET запроса - тест заголовка')
@allure.severity(allure.severity_level.NORMAL)
def test_list_html():
    res = http_bin_api.list_html()

    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'text/html; charset=utf-8'


@allure.feature('test_robots')
@allure.story('Отправка GET запроса - тест на соответствие текста из полученного файла')
@allure.severity(allure.severity_level.NORMAL)
def test_robots():
    res = http_bin_api.robots()
    res_body = res.text  # создаем объект тела ответа

    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'text/plain'
    assert re.fullmatch(r'.*User-agent: \*.*Disallow: /deny.*', res_body, flags=re.DOTALL)  # проверка соотв. текста


@allure.feature('test_ip')
@allure.story('Отправка GET запроса - IP адрес')
@allure.severity(allure.severity_level.NORMAL)
def test_ip():
    res = http_bin_api.ip()

    assert res.status_code == HTTPStatus.OK
    if res.headers['Content-Type'] == 'application/json':
        Assert.validate_schema(res.json())

        origin = res.json()['origin']  # из ответа получаем значение по ключу origin
        assert re.fullmatch(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', origin)  # сравнение полученного значения с паттерном
