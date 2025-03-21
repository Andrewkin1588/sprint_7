import allure
import pytest

from src.crud.methods import Methods
from src.constants import (CREATE_COURIER,
                           EXPECTED_RESPONSE_LOGIN_IS_USED,
                           EXPECTED_RESPONSE_NO_MORE_DATA_FOR_CREATE_COURIER,
                           EXPECTED_RESPONSE_SUCCESSFUL_CREATE_COURIER)


class TestCreateCourier:

    @allure.title("курьера можно создать")
    def test_create_courier(self, generate_data_for_create_courier):
        method = Methods(CREATE_COURIER)
        with allure.step("Создаем курьера"):
            method.post(201, data=generate_data_for_create_courier)


    @allure.title("нельзя создать двух одинаковых курьеров")
    def test_two_courier(self, generate_data_for_create_courier):
        courier = generate_data_for_create_courier
        method = Methods(CREATE_COURIER)
        with allure.step("Создаем первого курьера"):
            method.post(201, data=courier)
        with allure.step("Создаем второго курьера"):
            method.post(409, data=courier, expected_body=EXPECTED_RESPONSE_LOGIN_IS_USED)

    @allure.title("чтобы создать курьера, нужно передать в ручку все обязательные поля")
    @pytest.mark.parametrize('data', ([{"login": "test", "firstName": "Andrew"},
                                       {"password": "test", "firstName": "Andrew"}]))
    def test_without_required_field(self, data):
        method = Methods(CREATE_COURIER)
        with allure.step("Проверяем создание курьера без обязательного поля"):
            method.post(400, data=data, expected_body=EXPECTED_RESPONSE_NO_MORE_DATA_FOR_CREATE_COURIER)

    @allure.title("запрос возвращает правильный код ответа")
    def test_status_code(self, generate_data_for_create_courier):
        method = Methods(CREATE_COURIER)
        with allure.step("Проверяем статус код"):
            method.post(201, data=generate_data_for_create_courier)

    @allure.title("успешный запрос возвращает {ok:true}")
    def test_response_body(self, generate_data_for_create_courier):
        method = Methods(CREATE_COURIER)
        with allure.step("Проверяем тело ответа"):
            method.post(data=generate_data_for_create_courier, expected_body=EXPECTED_RESPONSE_SUCCESSFUL_CREATE_COURIER)
