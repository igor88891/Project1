import os

from dotenv import load_dotenv
import requests
load_dotenv()
API_KEY = os.getenv('API_KEY')

def get_amount_rub(transaction):
    "Функция принимает список транзакций и возвращает сумму конвертированную в рубли"
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return float(amount)
    else:
        response = requests.get(
            f'https://api.apilayer.com/exchangerates_data/convert?from={currency}&to=RUB&amount={amount}',
            headers = {'apikey': API_KEY}
        )
        data = response.json()
        return float(data["result"])

# print(get_amount_rub({
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   }))