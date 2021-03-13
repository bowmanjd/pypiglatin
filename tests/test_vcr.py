import pytest

import pypiglatin


@pytest.mark.vcr()
def test_translate():
    text = "Thank you for your hospitality"
    translated = "ank-Thay ou-yay or-fay our-yay ospitality-hay "
    assert pypiglatin.translate(text) == translated
