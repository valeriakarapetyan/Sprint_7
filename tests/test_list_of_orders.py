import requests
import allure
from conftest import URL


@allure.epic("Тестирование GET /api/v1/orders")
class TestListOfOrders:

    @allure.feature("Получение списка заказов")
    @allure.title("Проверка наличия orders в ответе")
    def test_get_orders(self):
        response = requests.get(f"{URL}/api/v1/orders")
        response_json = response.json()
        assert response.status_code == 200
        assert 'orders' in response_json

        for order in response_json['orders']:
            assert 'id' in order
            assert 'firstName' in order
            assert 'lastName' in order
            assert 'address' in order
            assert 'metroStation' in order
            assert 'phone' in order
            assert 'rentTime' in order
            assert 'deliveryDate' in order
            assert 'track' in order
            assert 'color' in order
            assert 'comment' in order
            assert 'createdAt' in order
            assert 'updatedAt' in order
            assert 'status' in order
