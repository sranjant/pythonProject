import pytest
import requests


def test_get_request():
  response = requests.get("https://jsonplaceholder.typicode.com/todos/")
  print(response.text)
  response_status = response.status_code
  assert response_status == 200
