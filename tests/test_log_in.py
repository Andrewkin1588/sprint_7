import json

import allure
import pytest

from src.crud.methods import Methods
from src.constants import (CREATE_COURIER,
                           LOG_IN_COURIER,
                           EXPECTED_RESPONSE_NOT_FOUND_USER,
                           EXPECTED_RESPONSE_NO_MORE_DATA_FOR_LOG_IN)


class TestLogInCourier:

    @allure.title("курьер может авторизоваться")
    @allure.title("для авторизации нужно передать все обязательные поля")
    @allure.title("успешный запрос возвращает id.")
    def test_log_in_courier(self, generate_data_for_create_courier, data_for_log_in_courier):
        method = Methods(CREATE_COURIER)
        method.post(data=generate_data_for_create_courier)
        with allure.step("Авторизуемся за курьера"):
            method = Methods(LOG_IN_COURIER)
            response = method.post(expected_status_code=200, data=data_for_log_in_courier)
        with allure.step('Возвращает id'):
            assert response.json()['id']

    @allure.title("система вернёт ошибку, если неправильно указать логин или пароль")
    @allure.title("если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    def test_auth_not_found_login(self, data_for_log_in_courier):
        with allure.step("Авторизуемся с неверными данными"):
            method = Methods(LOG_IN_COURIER)
            method.post(data=data_for_log_in_courier,
                        expected_body=EXPECTED_RESPONSE_NOT_FOUND_USER)

    @allure.title("если какого-то поля нет, запрос возвращает ошибку")
    @pytest.mark.parametrize('field', ([{"login": "test"}, {"password": "test"}]))
    def test_error_without_required_field(self, field):
        with allure.step("Авторизуемся с неверными данными"):
            method = Methods(LOG_IN_COURIER)
            method.post(data=json.dumps(field), expected_body=EXPECTED_RESPONSE_NO_MORE_DATA_FOR_LOG_IN)
