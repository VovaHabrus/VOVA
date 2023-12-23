import requests


def test_api():
    # Створюємо словник з даними, які хочемо надіслати
    data = {
        "title": "foo",
        "body": "bar",
        "userId": "1"
    }

    # Надсилаємо запит POST на URL з даними
    response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)

    # Виводимо статус-код, заголовки і тіло відповіді
    print(response.status_code)
    print(response.headers)
    print(response.text)
