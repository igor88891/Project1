def filter_by_currency(transactions: list, currency='{"name": "USD", "code": "USD"}') -> list:
    'Функция принимает спичок словарей, возвращает те, где валюта соответствует заданной'
    state_list_currency = []
    for item in transactions:
        for currency in item["operationAmount"]:
            if "currency" == currency:
                state_list_currency.append(item)
    return state_list_currency
