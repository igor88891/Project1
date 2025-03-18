from src.widget import get_date
import datetime


def sort_by_date(dct, reverse=True):
    return sorted(dct, key=lambda x: x['date'], reverse=reverse)


def filter_by_state(dct, state='EXECUTED'):
    state_list = []
    for item in dct:
        if item['state'] == state:
            state_list.append(item)
    return state_list













