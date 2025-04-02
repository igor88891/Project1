from dateutil.parser import isoparse


def sort_by_date(dct: list, reverse=True) -> list:
    '''Функция сортирует список словарей по дате'''
    date_list_rerverse = []
    for item in dct:
        if isoparse(item['date']):
            date_list_rerverse.append(item)
            print(isoparse(item['date']))
        else:
            return "Дата отсутствует, либо введена в некоректном формате!"
    return sorted(date_list_rerverse, key=lambda x: x['date'], reverse=reverse)


def filter_by_state(dct: list, state='EXECUTED') -> list:
    """Функция сортирует словари по ключу состояние, если выполнено, добавляет его в отдельный список"""
    state_list_true = []
    state_list_false = []
    for item in dct:
        if item['state'] == state:
            state_list_true.append(item)
        else:
            state_list_false.append(item)
    return state_list_true
