from src.widget import mask_account_card, get_date
from src.processing import filter_by_state

if __name__ == '__main__':
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


if __name__ == '__main__':
    data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

    for dct in data:
        print(filter_by_state(dct))









