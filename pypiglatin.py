#!/usr/bin/env python3

"""A translator of pig Latin using HTTPS API calls."""

import json
from urllib.parse import urlencode
from urllib.request import urlopen

SERVER = "api.funtranslations.com"


def translate(text: str) -> str:
    """
    Translate text to pig Latin.

    Args:
        text: the text to translate

    Returns:
        Translated text
    """
    data = {"text": text}
    form_encoded_data = urlencode(data).encode()
    url = f"https://{SERVER}/translate/piglatin.json"
    with urlopen(url, form_encoded_data) as response:
        result = json.load(response)
        print(result)
    return result["contents"]["translated"]
