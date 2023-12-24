import requests


def test_api():
    # Створюємо словник з даними, які хочемо надіслати
    data = {
            "name": "morpheus",
            "job": "leader"
    }

    # Надсилаємо запит POST на URL з даними
    response = requests.post("https://reqres.in/api/users", data=data)

    # Виводимо статус-код, заголовки і тіло відповіді
    print(response.status_code)
    print(response.headers)
    print(response.text)
