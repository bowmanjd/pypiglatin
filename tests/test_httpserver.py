"""Test HTTP client."""

import ssl
from urllib.parse import urlencode

import pytest
import trustme  # type: ignore

import pypiglatin

SERVER = "localhost"
PORT = 8888

ENDPOINT = "/translate/piglatin.json"


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return (SERVER, PORT)


@pytest.fixture(scope="session")
def httpserver_ssl_context():
    ca = trustme.CA()
    client_context = ssl.SSLContext()
    server_context = ssl.SSLContext()
    server_cert = ca.issue_cert("test-host.example.org")
    ca.configure_trust(client_context)
    server_cert.configure_cert(server_context)

    def default_context():
        return client_context

    ssl._create_default_https_context = default_context

    return server_context


def test_post(httpserver):
    text = "Thank you for your hospitality"
    translated = "ank-Thay ou-yay or-fay our-yay ospitality-hay "
    response = {
        "success": {"total": 1},
        "contents": {
            "translated": translated,
            "text": text,
            "translation": "pig-latin",
        },
    }

    httpserver.expect_request(
        ENDPOINT, method="POST", data=urlencode({"text": text})
    ).respond_with_json(response)
    assert pypiglatin.translate(text, f"{SERVER}:{PORT}") == translated
