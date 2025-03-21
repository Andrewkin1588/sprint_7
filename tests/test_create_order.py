import json

import allure
import pytest

from src.crud.methods import Methods
from src.constants import ORDERS


class TestCreateOrder:

    @allure.title("можно указать один из цветов — BLACK или GREY")
    @allure.title("можно указать оба цвета")
    @allure.title("можно совсем не указывать цвет")
    @allure.title("тело ответа содержит track")
    @pytest.mark.parametrize('color', (["BLACK", "GREY", "'BLACK', 'GREY'", ""]))
    def test_select_color(self, color):
        order_data = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                color
            ]
        }
        method = Methods(ORDERS)
        with allure.step('Проверяем цвета'):
            response = method.post(expected_status_code=201, data=json.dumps(order_data))
        with allure.step('Проверяем ответ'):
            assert response.json()['track']
