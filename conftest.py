import json

import pytest

from src.constants import LOG_IN_COURIER, DELETE_COURIER
from src.crud.methods import Methods
from src.helpers import Helpers


@pytest.fixture(scope="function")
def generate_data_for_create_courier():
    helper = Helpers()
    courier = {
        "login": helper.generate_random_string(),
        "password": helper.generate_random_string(),
        "firstName": helper.generate_random_string()
    }
    yield courier
    method = Methods(LOG_IN_COURIER)
    courier_id = method.post(data={"login": courier.get("login"), "password": courier.get("password")})
    method.url = DELETE_COURIER
    method.delete(params=str(json.loads(courier_id.text).get('id')))


@pytest.fixture(scope="function")
def data_for_log_in_courier(generate_data_for_create_courier):
    data_courier = generate_data_for_create_courier
    courier = {
        "login": data_courier.get("login"),
        "password": data_courier.get("password")
    }
    return courier
