from typing import Union
import logging


masks_logger = logging.getLogger("masks_log")
masks_logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8")
file_handler.setFormatter(formatter)
masks_logger.addHandler(file_handler)


"""Получаем данные от пользователя"""


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Возвращаем замаскированый номер карты"""
    masks_logger.info(f"Получение номера карты: {card_number}")
    len_number = 16
    masks_logger.info("Проверка из 16 цифр состоит номер карты или нет")
    if len(card_number) == len_number and card_number.isdigit():
        masks_logger.info("Результат работы функции get_mask_card_number получен")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        masks_logger.error("Вы ввели некоректные данные!")
        return "Вы ввели некоректные данные!"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Возвращаем замаскированный номер счета"""
    len_acc_number = 20
    masks_logger.info(f"Получение номера карты: {account_number}")
    if len(account_number) == len_acc_number and account_number.isdigit():
        masks_logger.info("Результат работы функции get_mask_account получен")
        return f"**{account_number[-4:]}"
    else:
        masks_logger.error("Вы ввели некоректные данные!")
        return "Вы ввели некоректные данные!"
