import allure
import requests
from allure_commons.types import AttachmentType


class Assertion:
    @staticmethod
    def assert_response_body(actual_response_body, expected_response_body):
        assert actual_response_body == expected_response_body

    @staticmethod
    def assert_status_code(actual_status_code, expected_status_code):
        assert actual_status_code == expected_status_code, f"Фактический статус код: {actual_status_code}"


class Methods:

    def __init__(self, url):
        self.url = url
        self.assertion = Assertion()

    @staticmethod
    def attach_method(response):
        allure.attach(response.url, AttachmentType.TEXT, 'url')
        allure.attach(str(response.status_code), AttachmentType.TEXT, 'status_code')

    def get(self, params='', expected_status_code='', expected_body=''):
        response = requests.get(url=self.url, params=params)
        self.attach_method(response)
        if expected_status_code:
            self.assertion.assert_status_code(response.status_code, expected_status_code)
        elif expected_body:
            self.assertion.assert_response_body(response.json(), expected_body)
        return response

    def post(self, expected_status_code='', data='', expected_body=''):
        response = requests.post(url=self.url, data=data)
        self.attach_method(response)
        if expected_status_code:
            self.assertion.assert_status_code(response.status_code, expected_status_code)
        elif expected_body:
            self.assertion.assert_response_body(response.json(), expected_body)
        return response

    def delete(self, expected_status_code='', params=''):
        response = requests.delete(url=self.url + params)
        self.attach_method(response)
        if expected_status_code:
            self.assertion.assert_status_code(response.status_code, expected_status_code)
