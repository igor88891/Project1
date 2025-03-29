import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """функция, которая умеет обрабатывать информацию как о картах, так и о счетах."""
    if len(type_and_number) < 1:
        return 'Вы ввели некоректные данные!'
    elif "Счет" in type_and_number and type_and_number[-20:].isdigit() == True:
        number = type_and_number.replace("Счет", "").strip()
        return "Счет" + get_mask_account(number)
    else:
        number = type_and_number[-16:]
        # ["Maestro", "Visa", "12233456"]
        updated_card = (
            " ".join(type_and_number.split()[:-1]) + " " + get_mask_card_number(number)
        )
        return updated_card


def get_date(user_date: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и
    возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")"""

    date_format = datetime.datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date






