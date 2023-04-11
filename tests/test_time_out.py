import allure

from api.httpbin_api import http_bin_api
from http import HTTPStatus


@allure.feature('test_time_out')
@allure.story('Отправка GET запроса - проверка таймаута - позитивный')
@allure.severity(allure.severity_level.NORMAL)
def test_time_out():
    res = http_bin_api.time_out(5)

    assert res.status_code == HTTPStatus.OK  # Проверяем, что запрос успевает проходить за указанное время


@allure.feature('test_time_out')
@allure.story('Отправка GET запроса - проверка таймаута - негативный')
@allure.severity(allure.severity_level.NORMAL)
def test_time_out_no():
    res = http_bin_api.time_out(2)

    assert not res[0]  # проверяем, что запрос НЕ успевает выполниться за указанное время
