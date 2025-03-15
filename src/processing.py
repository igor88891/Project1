def sort_by_date():
    pass


def filter_by_state(dct):
    for key in dct:
        if key == 'state':
            dct['state'] = "CANCELED"
    return dct











