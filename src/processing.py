def sort_by_date(dct: list, reverse=True) -> list:
    return sorted(dct, key=lambda x: x['date'], reverse=reverse)


def filter_by_state(dct: list, state='EXECUTED') -> list:
    state_list = []
    for item in dct:
        if item['state'] == state:
            state_list.append(item)
    return state_list













