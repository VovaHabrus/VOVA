import requests


def test_api():

    # Створюємо словник з параметрами запиту
    params = {"key1": "value1", "key2": "value2"}

    # Надсилаємо запит GET на URL із параметрами
    response = requests.get("http://httpbin.org/get", params=params)

    # Виводимо статус-код, заголовки і тіло відповіді
    print(response.status_code)
    print(response.headers)
    print(response.text)


test_api()
