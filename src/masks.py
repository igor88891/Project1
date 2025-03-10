from typing import Union


"""Получаем данные от пользователя"""


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Возвращаем замаскированый номер карты"""
    len_number = 16
    if len(card_number) == len_number:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return "Вы ввели некоректные данные!"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Возвращаем замаскированный номер счета"""
    len_acc_number = 20
    if len(account_number) == len_acc_number:
        return f"**{account_number[-4:]}"
    else:
        return "Вы ввели некоректные данные!"
