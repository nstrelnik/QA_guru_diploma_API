import requests
import allure
import logging
from requests import Response


def reqres_api_delete(url, **kwargs):
    with allure.step("API Request"):
        response = requests.delete(url="https://reqres.in" + url, **kwargs)
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)
    return response


@allure.story('Проверка удаления пользователя')
def test_delete_user(browser_settings):
    with allure.step("Удаление пользователя"):
        id_user = '2'
        endpoint = f'/api/users/{id_user}'

        response: Response = reqres_api_delete(endpoint)

        with allure.step("Статус код"):
            assert response.status_code == 204
        with allure.step("Значение в response"):
            assert response.text == ''
