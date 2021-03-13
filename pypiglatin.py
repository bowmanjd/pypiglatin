#!/usr/bin/env python3

"""A translator of pig Latin using HTTPS API calls."""

import json
from urllib.parse import urlencode
from urllib.request import urlopen


def translate(text: str, server: str = "api.funtranslations.com") -> str:
    """
    Translate text to pig Latin.

    Args:
        text: the text to translate
        server: the API server domain

    Returns:
        Translated text
    """
    data = {"text": text}
    form_encoded_data = urlencode(data).encode()
    url = f"https://{server}/translate/piglatin.json"
    with urlopen(url, form_encoded_data) as response:
        result = json.load(response)
        print(result)
    return result["contents"]["translated"]
