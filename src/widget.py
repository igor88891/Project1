from src.masks import get_mask_card_number, get_mask_account
import datetime



def mask_account_card(type_and_number: str) -> str:
    '''функция, которая умеет обрабатывать информацию как о картах, так и о счетах.'''
    if "Счет" in type_and_number:
        number = type_and_number.replace("Счет", "" ).strip()
        return "Счет " + get_mask_account(number)
    else:
        number = type_and_number[-16:]
        #["Maestro", "Visa", "12233456"]
        updated_card = " ".join(type_and_number.split()[:-1]) +" "+ get_mask_card_number(number)
        return updated_card




def get_date(user_date: str) -> str:
    '''Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")'''

    date_format = datetime.datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")

    return new_date


card_nums = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305"
]

for card in card_nums:
    print(mask_account_card(card))
print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
