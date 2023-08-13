from src.utils import load_operations, sorted_operations_list_by_datetime, formatted_the_operation
import pathlib
from pathlib import Path

# Загруженный список операций в формате JSON
PATH = Path(pathlib.Path.cwd(), "operations.json")

# Список операций переведенный из JSON
operations = load_operations(PATH)

# Отсортированный по дате и времени список операций
sorted_operations_by_date = sorted_operations_list_by_datetime(operations)

# Счетчик выводимых операций на экран
count_operations = 0

# Цикл вывода на экран последних 5 выполненных операций
for operation in sorted_operations_by_date:
    if count_operations > 5:
        break

    if operation['state'] == 'CANCELED':
        count_operations += 1
        continue
    elif operation['state'] == 'EXECUTED':
        count_operations += 1
        print(formatted_the_operation(operation))
