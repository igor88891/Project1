from unittest.mock import Mock

import requests

from src.external_api import get_amount_rub
from tests.conftest import transactions
import os
from dotenv import load_dotenv


def test_get_amount_rub():
    assert (
        get_amount_rub(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {"name": "RUB", "code": "RUB"},
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == 8221.37
    )


def test_get_amount_rub_not_rub():
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    transact = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_response = Mock(spec=requests.Response)
    mock_response.json.return_value = {"result": "8221.37"}
    mock_get = Mock(return_value=mock_response)
    requests.get = mock_get
    assert get_amount_rub(transact) == 8221.37
    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/exchangerates_data/convert?from=USD&to=RUB&amount=8221.37",
        headers={"apikey": API_KEY},
    )
