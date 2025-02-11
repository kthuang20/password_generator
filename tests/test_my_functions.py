# import necessary packages
import pytest
from unittest.mock import patch
import source.generate_password as generate_password


### test function to obtain valid text for generating password
def test_check_text():
    result = generate_password.check_text("validInput1234")
    assert result == True

### test function to obtain invalid text for generating password
def test_check_invalid_text():
    result = generate_password.check_text("short")
    assert result == False

### test function to obtain invalid text for generating password
def test_check_invalid_text_all_nums():
    result = generate_password.check_text("12334235409584059")
    assert result == False

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
def test_gen_password():
    ## test cases:
    test_cases = ["hello world",
                  "Data Science",
                  "Born believer",
                  "1234 happy lamb"]
    print("\n")
    for test_case in test_cases:
        result = generate_password.gen_password(test_case)
        print(f'{test_case} --> {result}')
