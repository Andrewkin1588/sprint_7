import json

import allure
import pytest

from src.crud.methods import Methods
from src.constants import CREATE_COURIER, LOG_IN_COURIER
from src.helpers import Helpers

helper = Helpers()
new_courier = {
    "login": helper.generate_random_string(10),
    "password": "test",
    "firstName": "test"
}
courier = {
    "login": new_courier.get("login"),
    "password": "test"
}


class TestLogInCourier:

    @allure.title("курьер может авторизоваться")
    @allure.title("для авторизации нужно передать все обязательные поля")
    @allure.title("успешный запрос возвращает id.")
    def test_log_in_courier(self):
        method = Methods(CREATE_COURIER)
        method.post(data=new_courier)
        with allure.step("Авторизуемся за курьера"):
            method = Methods(LOG_IN_COURIER)
            response = method.post(expected_status_code=200, data=courier)
        with allure.step('Возвращает id'):
            assert response.json()['id']

    @allure.title("система вернёт ошибку, если неправильно указать логин или пароль")
    @allure.title("если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    def test_auth_not_found_login(self):
        expected_body_response = {'code': 404, "message": "Учетная запись не найдена"}
        with allure.step("Авторизуемся с неверными данными"):
            method = Methods(LOG_IN_COURIER)
            method.post(data={"login": helper.generate_random_string(10), "password": "test"},
                        expected_body=expected_body_response)

    @allure.title("если какого-то поля нет, запрос возвращает ошибку")
    @pytest.mark.parametrize('field', ([{"login": "test"}, {"password": "test"}]))
    def test_error_without_required_field(self, field):
        expected_body_response = {'code': 400, "message":  "Недостаточно данных для входа"}
        with allure.step("Авторизуемся с неверными данными"):
            method = Methods(LOG_IN_COURIER)
            method.post(data=json.dumps(field), expected_body=expected_body_response)
