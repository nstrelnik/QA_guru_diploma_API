import requests
from allure_commons.types import AttachmentType
from jsonschema import validate
import json
import allure
import logging
from requests import Response

from schemas.get_resources import single_resource


def reqres_api_get(url, **kwargs):
    with allure.step("API Request"):
        response = requests.get(url="https://reqres.in" + url, **kwargs)
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)
    return response


@allure.story('Проверка получения данных о существующем пользователе')
def test_get_existing_resource_by_id(browser_settings):
    with allure.step("Получить данные существующего пользователя"):
        id_user = '2'
        endpoint = f'/api/unknown/{id_user}'

        response: Response = reqres_api_get(endpoint)
        body = response.json()

        with allure.step("Статус код"):
            assert response.status_code == 200
        with allure.step("Значение в response"):
            assert body['data']['id'] == int(id_user)
        with allure.step("Схема ответа"):
            validate(body, schema=single_resource)


@allure.story('Проверка получения данных о несуществующем пользователе')
def test_not_get_existing_resource_by_id(browser_settings):
    with allure.step("Получить данные несуществующего пользователя"):
        id_user = '23'
        endpoint = f'/api/unknown/{id_user}'

        response: Response = reqres_api_get(endpoint)
        body = response.json()

        with allure.step("Статус код"):
            assert response.status_code == 404
        with allure.step("Значение в response"):
            assert body == {}