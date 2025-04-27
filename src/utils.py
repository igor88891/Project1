import json


def get_transaction_json(operations_file):
    with open(operations_file, encoding="utf-8") as file:
        try:
            operations_data = json.load(file)
        except json.JSONDecodeError:
            return []
        except FileNotFoundError:
            return []
    return operations_data
