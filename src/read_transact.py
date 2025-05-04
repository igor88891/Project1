import pandas as pd
import csv
import openpyxl


def get_read_excel_transact(path: str) -> list[dict]:
    """Функция принимает файл Excel и возвращает список словарей"""
    try:
        excel_data = pd.read_excel(path, engine="openpyxl")
        trans_excel = excel_data.to_dict(orient="records")
        print(trans_excel)
        return trans_excel
    except Exception as ex:
        print(f"Произошла ошибка: {ex}")


if __name__ == "__main__":
    list_new = get_read_excel_transact(
        "C:/Users/admin/PycharmProjects/PythonProject/data/transactions_excel (1).xlsx"
    )


def get_read_csv_transact(path: str) -> list[dict]:
    """Функция принимает файл CSV и возвращает список словарей"""
    transact_list = []
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            my_dict = {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "amount": row["amount"],
                "currency_name": row["currency_name"],
                "currency_code": row["currency_code"],
                "from": row["from"],
                "to": row["to"],
                "description": row["description"],
            }
            transact_list.append(my_dict)
    return transact_list


if __name__ == "__main__":
    transact_new = get_read_csv_transact("..\\data\\transactions.csv")
    print(transact_new)
