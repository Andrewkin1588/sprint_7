import allure
import pytest

from src.crud.methods import Methods
from src.constants import CREATE_COURIER
from src.helpers import Helpers


class TestCreateCourier:

    helper = Helpers()

    @allure.title("курьера можно создать")
    def test_create_courier(self):
        courier_data = {
            "login": self.helper.generate_random_string(10),
            "password": "test",
            "firstName": "test"
        }
        method = Methods(CREATE_COURIER)
        with allure.step("Создаем курьера"):
            method.post(201, data=courier_data)

    @allure.title("нельзя создать двух одинаковых курьеров")
    def test_two_courier(self):
        login_courier = self.helper.generate_random_string(10)
        data = {
            "login": login_courier,
            "password": "qwerty12",
            "firstName": "Andrew"
        }
        expected_body_response = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
        method = Methods(CREATE_COURIER)
        with allure.step("Создаем первого курьера"):
            method.post(201, data=data)
        with allure.step("Создаем второго курьера"):
            method.post(409, data=data, expected_body=expected_body_response)

    @allure.title("чтобы создать курьера, нужно передать в ручку все обязательные поля")
    @pytest.mark.parametrize('data', ([{"login": "test", "firstName": "Andrew"},
                                       {"password": "test", "firstName": "Andrew"}]))
    def test_without_required_field(self, data):
        expected_body_response = {'code': 400, 'message': "Недостаточно данных для создания учетной записи"}
        method = Methods(CREATE_COURIER)
        with allure.step("Проверяем создание курьера без обязательного поля"):
            method.post(400, data=data, expected_body=expected_body_response)

    @allure.title("запрос возвращает правильный код ответа")
    def test_status_code(self):
        courier_data = {
            "login": self.helper.generate_random_string(10),
            "password": "test",
            "firstName": "test"
        }
        method = Methods(CREATE_COURIER)
        with allure.step("Проверяем статус код"):
            method.post(201, data=courier_data)

    @allure.title("успешный запрос возвращает {ok:true}")
    def test_response_body(self):
        courier_data = {
            "login": self.helper.generate_random_string(10),
            "password": "test",
            "firstName": "test"
        }
        method = Methods(CREATE_COURIER)
        with allure.step("Проверяем тело ответа"):
            response_body_expected = {"ok": True}
            method.post(data=courier_data, expected_body=response_body_expected)
