import requests
from allure_commons.types import AttachmentType
from jsonschema import validate
import json
from pathlib import Path
import allure
import logging
from requests import Response

from schemas.post_login import login_successfully, login_unsuccessfully


def schema_path(name):
    return str(Path(__file__).parent.parent.joinpath(f'schemas/{name}'))


def reqres_api_post(url, **kwargs):
    with allure.step("API Request"):
        response = requests.post(url="https://reqres.in" + url, **kwargs)
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)
    return response


@allure.story('Проверка успешной регистрации')
def test_post_register_successful(browser_settings):
    with allure.step("Успешная регистрация"):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        endpoint = '/api/register'

        response: Response = reqres_api_post(endpoint, data=payload)

        with allure.step("Статус код"):
            assert response.status_code == 200
        with allure.step("Значение в response"):
            assert 'token' in response.json()
        with allure.step("Схема ответа"):
            schema = schema_path("post_register.json")
            with open(schema) as file:
                validate(response.json(), schema=json.loads(file.read()))


@allure.step('Проверка неуспешной регистрации, без ввода пароля')
def test_post_register_unsuccessful(browser_settings):
    with allure.step("Регистрация без пароля"):
        payload = {"email": "peter@klaven"}
        endpoint = '/api/register'

        response: Response = reqres_api_post(endpoint, data=payload)

        with allure.step("Статус код"):
            assert response.status_code == 400
        with allure.step("Значение в response"):
            assert response.json()['error'] == "Missing password"


@allure.story('Проверка успешной авторизации')
def test_post_login_successful(browser_settings):
    with allure.step("Успешная авторизация"):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        endpoint_login = "/api/login"

        response: Response = reqres_api_post(endpoint_login, json=payload)
        body = response.json()

        with allure.step("Статус код"):
            assert response.status_code == 200
        with allure.step("Значение в response"):
            assert 'token' in response.json()
        with allure.step("Схема ответа"):
            validate(body, schema=login_successfully)


@allure.story('Проверка неуспешной авторизации, без пароля')
def test_post_login_unsuccessful(browser_settings):
    with allure.step("Неуспешная авторизация (без пароля)"):
        payload = {
            "email": "peter@klaven"
        }
        endpoint_login = "/api/login"

        response: Response = reqres_api_post(endpoint_login, json=payload)
        body = response.json()

        with allure.step("Статус код"):
            assert response.status_code == 400
        with allure.step("Значение в response"):
            assert 'error' in response.json()
        with allure.step("Схема ответа"):
            validate(body, schema=login_unsuccessfully)
