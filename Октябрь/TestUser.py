import requests


class TestStore:
    base_url = "https://petstore.swagger.io/v2/user"

    def test_get_username_not_found(self):
        username = "Cati"
        response = requests.get(f"{self.base_url}/{username}")
        data = response.json()
        assert response.status_code == 404
        assert data["message"] == "User not found"

    def test_post_username(self):
        data = {"id": 2,
              "username": "Dogi",
              "firstName": "Эдвард",
              "lastName": "Каллен",
              "email": "123@mail.ru",
              "password": "789587",
              "phone": "88005553535",
                "userStatus": 0}
        post_url = (f"{self.base_url}")
        response = requests.post(post_url, json=data)
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"

    def test_put_username_update(self):
        username = "Dogi"
        data = {"id": 2,
                "username": "Dogi",
                "firstName": "Эдвард",
                "lastName": "Каллен",
                "email": "123@mail.ru",
                "password": "789587",
                "phone": "88005553535",
                "userStatus": 0}
        put_url = (f"{self.base_url}/{username}")
        response = requests.put(put_url, json=data)
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"

    def test_post_username_error_email(self):
        data = {"id": 2,
              "username": "Dogi",
              "firstName": "Эдвард",
              "lastName": "Каллен",
              "email": "kallenA",
              "password": "789587",
              "phone": "88005553535",
                "userStatus": 0}
        post_url = (f"{self.base_url}")
        response = requests.post(post_url, json=data)
        assert response.status_code == 400

    def test_post_username_short_date(self):
        data = {"id": 2,
              "firstName": "Недостачно Данных",
              "password": "987456",
                "userStatus": 0}
        post_url = (f"{self.base_url}")
        response = requests.post(post_url, json=data)
        assert response.status_code == 404

    def test_get_username_found(self):
        username = "Dogi"
        response = requests.get(f"{self.base_url}/{username}")
        data = response.json()
        assert response.status_code == 200
        assert data["username"] == username

    def test_post_username_max_long(self):
        data = {"id": 2,
              "username": "Dogi" * 100,
              "firstName": "Эдвард" * 100,
              "lastName": "Каллен",
              "email": "kallenA",
              "password": "789587" * 50,
              "phone": "88005553535",
                "userStatus": 0}
        post_url = (f"{self.base_url}")
        response = requests.post(post_url, json=data)
        assert response.status_code == 400

    def test_post_username_del(self):
        data = {"id": 666,
              "username": "Del",
              "firstName": "Удаленный",
              "lastName": "пользователь",
              "email": "del@mail.ru",
              "password": "deldeldeldeldel",
              "phone": "deldeldeldeldel",
                "userStatus": 0}
        post_url = (f"{self.base_url}")
        response = requests.post(post_url, json=data)
        assert response.status_code == 200

    def test_del_user(self):
        username = "Del"
        url = "user"
        del_url = (f"{self.base_url}/{url}/{username}")
        response = requests.delete(del_url)
        assert response.status_code == 404
        assert response.headers["Content-Type"] == "application/xml"
    """
    Когда ставлю код ошибки - 404, тест падает потому что ошибка 200.
    Когда ставлю код ошибки 200 - тест падает потому что ошибка 404.
    По документации должен быть 404
    """

    def test_put_username_delete_update(self):
        username = "Del"
        data = {"id": 666,
              "username": "Delete",
              "firstName": "Удаленный",
              "lastName": "пользователь",
              "email": "del@mail.ru",
              "password": "deldeldeldeldel",
              "phone": "deldeldeldeldel",
                "userStatus": 0}
        put_url = (f"{self.base_url}/{username}")
        response = requests.put(put_url, json=data)
        assert response.status_code == 404

