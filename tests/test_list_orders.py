import allure

from src.crud.methods import Methods
from src.constants import ORDERS


class TestGetOrders:

    @allure.title("Проверь, что в тело ответа возвращается список заказов.")
    def test_list_orders(self):
        method = Methods(ORDERS)
        with allure.step('Проверяем статус код'):
            response = method.get(expected_status_code=200)
        with allure.step('Проверяем список'):
            assert response.json()['orders']
