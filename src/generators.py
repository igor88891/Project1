from typing import Iterator


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    "Фунцция возвращает описание каждой операции"
    for item in transactions:
        yield item["description"]


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator:
    "Функция принимает спичок словарей, возвращает те, где валюта соответствует заданной"
    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item


def card_number_generator(start: int, stop: int) -> Iterator:
    for number in range(start, stop + 1):
        number_card = f"{number:016d}"
        number_card_format = f"{number_card[:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:16]}"
        yield number_card_format



