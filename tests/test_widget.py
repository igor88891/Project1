import pytest

from src.widget import  mask_account_card,get_date

def test_mask_account_card():
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"

def test_mask_account_card_score():
    assert mask_account_card("Счет 64686473678894779589") == "Счет**9589"

def test_mask_account_card_empty():
    assert mask_account_card("") == 'Вы ввели некоректные данные!'


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"