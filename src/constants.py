BASE_URL = 'https://qa-scooter.praktikum-services.ru'
CREATE_COURIER = BASE_URL + '/api/v1/courier'
DELETE_COURIER = BASE_URL + '/api/v1/courier/'
LOG_IN_COURIER = BASE_URL + '/api/v1/courier/login'
ORDERS = BASE_URL + '/api/v1/orders'

EXPECTED_RESPONSE_LOGIN_IS_USED = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
EXPECTED_RESPONSE_NO_MORE_DATA_FOR_CREATE_COURIER = {'code': 400, 'message': "Недостаточно данных для создания учетной записи"}
EXPECTED_RESPONSE_NO_MORE_DATA_FOR_LOG_IN = {'code': 400, "message":  "Недостаточно данных для входа"}
EXPECTED_RESPONSE_SUCCESSFUL_CREATE_COURIER = {"ok": True}
EXPECTED_RESPONSE_NOT_FOUND_USER = {'code': 404, "message": "Учетная запись не найдена"}
