# import necessary packages
import pytest
from unittest.mock import patch
import source.generate_password as generate_password


### test function to obtain valid inputted text
def test_input_text_valid(monkeypatch):
    with patch("builtins.input", return_value="valid Input1234"):
        assert generate_password.input_text() == "Valid Input1234"

### test function to obtain valid inputted text
def test_input_text_short():
    with patch("builtins.input", side_effect=["short", "stillshort", "valid Input1234"]):
        assert generate_password.input_text() == "Valid Input1234"


### test function to replacement of non-valid characters
def test_replace_nonvalid_char():
    with pytest.raises(KeyError):
        result = generate_password.replace_char("S")


### test function to replacement of valid characters with one value
def test_replace_valid_char():
    result = generate_password.replace_char("a")
    assert result == "@"


### test function to replacement of valid characters with multiple values
def test_replace_valid_char_two_options():
    result = generate_password.replace_char("s")
    assert result == '$' or result == '5'


### test function to generate the password
def test_gen_passwords():
    ## test cases:
    test_cases = ["hello world",
                  "Data Science",
                  "Born believer",
                  "1234 happy lamb"]
    print("\n")
    for test_case in test_cases:
        result = generate_password.gen_password(test_case)
        print(f'{test_case} --> {result}')
