import requests

from API.configuration import SERVICE_URL
from API.src.enums.global_enums import GlobalErrorMessages


def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200, GlobalErrorMessages.WRONGSTATUSCODE.value
    print(response.json())
