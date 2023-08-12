import json
from datetime import datetime


def load_operations(path):
    """
    Функция загружает список операций из файла json. Если в нем есть пустые операции, удаляет их.
    :param path: Директория с файлом
    :return: Список операций
    """
    with open(path, encoding="utf-8") as operations:
        operations = json.load(operations)
        operations = list(filter(None, operations))

    return operations


def sorted_operations_list_by_datetime(operations):
    """
    Редактирует написание даты и времени.
    Сортирует список операций по дате и времени.
    :param operations: Список операций
    :return: Отсортированный список
    """
    for operation in operations:
        operation['date'] = operation["date"].replace("T", " ")

    sorted_operations_by_date = sorted(
        operations,
        key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d %H:%M:%S.%f"), reverse=True
    )

    return sorted_operations_by_date


def edited_the_information_from_the_transfer(direction):
    """
    Редактирует информацию о переводе под нужный формат вывода
    :param direction: Информация откуда или куда сделан перевод
    :return: Строка с информацией откуда или куда перевод
    """
    if direction is None:
        edited_direction = ""
    elif direction.startswith('Счет'):
        list_direction = direction.split(" ")
        last_six_numbers = list_direction[-1][-6:]
        edited_number = last_six_numbers.replace(last_six_numbers[0:2], "**")
        edited_direction = list_direction[0] + " " + (edited_number.replace(edited_number[0:2], "**"))

    else:
        direction = direction.split(" ")
        private_direction = direction[-1].replace(direction[-1][6:12], "******")
        list_edited_direction = []

        for chunk in range(0, 16, 4):
            list_edited_direction.append(private_direction[chunk:chunk + 4])

        edited_direction = " ".join(direction[:-1]) + " " + " ".join(list_edited_direction)

    return edited_direction


def formatted_the_operation(operation):
    """
    Получает операцию и форматирует ее для итогового вывода на экран
    :return:Отформатированную операцию
    """
    date_formatted = datetime.strptime(operation['date'], '%Y-%m-%d %H:%M:%S.%f').strftime('%d.%m.%Y')
    description = operation['description']
    from_ = operation.get('from')
    to_ = operation.get('to')
    edited_from_ = edited_the_information_from_the_transfer(from_)
    edited_to_ = edited_the_information_from_the_transfer(to_)
    transfer_amount = operation['operationAmount']['amount']
    transfer_currency = operation['operationAmount']['currency']['name']

    return f"{date_formatted} {description}\n{edited_from_} -> {edited_to_}\n{transfer_amount} {transfer_currency}\n"
