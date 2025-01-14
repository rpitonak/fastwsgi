import requests


def test_wsgi_get(wsgi_test_server):
    url = f"{wsgi_test_server.endpoint}/get"
    result = requests.get(url)
    assert result.status_code == 200
    assert result.text == "OK"


def test_wsgi_post(wsgi_test_server):
    # Post with no data
    url = f"{wsgi_test_server.endpoint}/post"

    result = requests.post(url)
    assert result.status_code == 201
    assert result.text == "OK"

    # Post with data
    result = requests.post(url, json={"test": "data"})
    assert result.status_code == 201
    assert result.text == "OK"


def test_wsgi_delete(wsgi_test_server):
    url = f"{wsgi_test_server.endpoint}/delete"
    result = requests.delete(url)
    assert result.status_code == 204
    assert result.text == ""
