import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_number():
    return "1596837868705199"


@pytest.fixture
def account_number():
    return "64686473678894779589"


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1596 83** **** 5199"


@pytest.mark.parametrize('invalid_card', ("159683786870519", "1596837868705194555", "159"))
def test_get_mask_card_number_invalid(invalid_card):
    assert get_mask_card_number(invalid_card) == "Вы ввели некоректные данные!"


def test_get_mask_card_number_isdigit():
    assert get_mask_card_number("159683786870519g") == "Вы ввели некоректные данные!"


def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == '**9589'


@pytest.mark.parametrize("invalid_account", ("6468647367889477958956665", "646864736788949589", "646864736"))
def test_get_mask_account_invalid(invalid_account):
    assert get_mask_account(invalid_account) == "Вы ввели некоректные данные!"


def test_get_mask_account_isdigit():
    assert get_mask_card_number("6468647e67889t779589") == "Вы ввели некоректные данные!"
