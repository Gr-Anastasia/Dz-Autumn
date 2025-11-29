import pytest
import auth
from auth import get_user

# Задание 3. Фикстура
@pytest.fixture(scope="module")
def correct_data_user():
    return get_user

# Задание 1. Позитивный кейс: корректный логин пользователя.
def test_correct_user(correct_data_user):
    data_user = correct_data_user("guest")
    login = auth.login(data_user["username"], data_user["password"])
    assert login is True

# Задание 4. Параметризация
@pytest.mark.parametrize("username, password, expected_login",
                    [ ("admin", "admin123", True),
                      ("guest", "guest", True),
                      ("admin", "guest", "Неверный пароль"),
                      ("guest", "admin123", "Неверный пароль"),
                      ("guest23", "guest", "Пользователь не найден"),
                      ("admin", "admin123", "Пользователь не найден")

                    ])
# Задание 5. Негативные кейсы: пользователь не найден; пароль неверен.
def test_parame(username, password, expected_login):
    if expected_login is True:
        login = auth.login(username, password)
        assert login is True
    else:
        try:
            login = auth.login(username, password)
        except ValueError as error:
            assert str(error) == expected_login
