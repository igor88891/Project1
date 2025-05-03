import json
import logging

masks_logger = logging.getLogger("masks_log")
masks_logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('../logs/utils.log', encoding='utf-8')
file_handler.setFormatter(formatter)
masks_logger.addHandler(file_handler)


def get_transaction_json(operations_file):
    with open(operations_file, encoding="utf-8") as file:
        try:
            operations_data = json.load(file)
            masks_logger.info("Операция выполнена!")
        except json.JSONDecodeError:
            masks_logger.error("Ошибка формата!!")
            return []
        except FileNotFoundError:
            masks_logger.info("Информация отсутствует!")
            return []
    return operations_data
masks_logger.info("Программа завершила работу!")

