import pytest
import allure
import requests
from conftest import URL

order_data = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha"
}


@allure.epic("Тестирование POST /api/v1/orders")
class TestCreateOrder:

    @allure.feature("Создание заказа")
    @pytest.mark.parametrize('color_input', [(["BLACK"]), (["GREY"]), (["BLACK", "GREY"]), ([])])
    @allure.title("Создание заказа с цветом: {color_input}")
    def test_create_order_with_different_colors(self, color_input):
        payload = order_data.copy()
        payload["color"] = color_input
        response = requests.post(f"{URL}/api/v1/orders", json=payload)
        response_json = response.json()
        assert response.status_code == 201
        assert "track" in response_json
