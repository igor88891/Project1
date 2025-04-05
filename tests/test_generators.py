import pytest
from src.generators import card_number_generator, transaction_descriptions,  filter_by_currency


def test_card_number_generator():
    assert next(card_number_generator(1, 9999999999999999)) == '0000 0000 0000 0001'


@pytest.fixture
def descriptions():
    return 'Перевод организации'


def test_transaction_descriptions(descriptions):
    assert transaction_descriptions(descriptions)


@pytest.fixture
def currency_f():
    return {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации',
            'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}


def test_filter_by_currency(currency_f):
    assert filter_by_currency(currency_f, 'USD')






