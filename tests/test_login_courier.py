import requests
import allure
from conftest import URL


@allure.epic("Тестирование /api/v1/courier/login")
class TestLoginCourier:

    @allure.feature("Успешный логин")
    @allure.title("Проверка кода и ответа")
    def test_courier_login_success(self, register_new_courier_and_return_login_password):
        login = register_new_courier_and_return_login_password[0]
        password = register_new_courier_and_return_login_password[1]
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f"{URL}/api/v1/courier/login", json=payload)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.feature("Неудачный логин")
    @allure.title("Логин без логина")
    def test_login_missing_login(self, register_new_courier_and_return_login_password):
        payload = {
            "password": register_new_courier_and_return_login_password[1]
        }
        response = requests.post(f"{URL}/api/v1/courier/login", json=payload)
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для входа"}

    @allure.feature("Неудачный логин")
    @allure.title("Логин без пароля")
    def test_login_missing_password(self, register_new_courier_and_return_login_password):
        payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": ""
        }
        response = requests.post(f"{URL}/api/v1/courier/login", json=payload)
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для входа"}

    @allure.feature("Неудачный логин")
    @allure.title("Логин с неправильным логином")
    def test_login_invalid_login(self):
        payload = {
            "login": "random_non_existent_user",
            "password": "1234"
        }
        response = requests.post(f"{URL}/api/v1/courier/login", json=payload)
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    @allure.feature("Неудачный логин")
    @allure.title("Логин с неправильным паролем")
    def test_login_invalid_password(self, register_new_courier_and_return_login_password):
        login = register_new_courier_and_return_login_password[0]
        payload = {
            "login": login,
            "password": "wrong_password"
        }
        response = requests.post(f"{URL}/api/v1/courier/login", json=payload)
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    @allure.feature("Неудачный логин")
    @allure.title("Логин с несуществующим пользователем")
    def test_login_with_non_existent_user(self):
        payload = {
            "login": "random_non_existent_user",
            "password": "random_password"
        }
        response = requests.post(f"{URL}/api/v1/courier/login", json=payload)
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}
