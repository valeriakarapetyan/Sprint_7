import requests
import allure
from conftest import URL


@allure.epic("Тестирование /api/v1/courier")
class TestCreateCourier:

    @allure.feature("Успешное создание")
    @allure.title("Проверка кода и ответа")
    def test_create_courier_success(self, payload):
        response = requests.post(f"{URL}/api/v1/courier", json=payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.feature("Неудачное создание")
    @allure.title("Создание курьера дважды")
    def test_create_courier_twice(self, payload):
        # Создаем первого курьера
        requests.post(f"{URL}/api/v1/courier", json=payload)
        # Пытаемся создать второго с теми же данными
        response = requests.post(f"{URL}/api/v1/courier", json=payload)
        assert response.status_code == 409
        assert response.json() == {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}

    @allure.feature("Неудачное создание")
    @allure.title("Создание без логина")
    def test_create_courier_without_login_error(self, payload):
        firstname = payload["firstName"]
        password = payload["password"]
        body = {
            "password": password,
            "firstName": firstname
        }
        response = requests.post(f"{URL}/api/v1/courier", json=body)
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}

    @allure.feature("Неудачное создание")
    @allure.title("Создание без пароля")
    def test_create_courier_without_password_error(self, payload):
        firstname = payload["firstName"]
        login = payload["login"]
        body = {
            "login": login,
            "firstName": firstname
        }
        response = requests.post(f"{URL}/api/v1/courier", json=body)
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}

    @allure.feature("Успешное создание")
    @allure.title("Создание курьера без необзятельного параметра")
    def test_create_courier_without_firstname_success(self, payload):
        password = payload["password"]
        login = payload["login"]
        body = {
            "login": login,
            "password": password
        }
        response = requests.post(f"{URL}/api/v1/courier", json=body)
        assert response.status_code == 201
        assert response.json() == {"ok": True}
