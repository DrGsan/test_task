import pytest  # pytest -v
from setup import *


class TestValidateToken:
    def test_empty_token(self):
        assert validate_token('foobar') == False

    def test_token(self):
        assert validate_token('tok.qwerty123-456') == True
