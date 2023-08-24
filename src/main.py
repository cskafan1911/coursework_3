from src.utils import load_operations, sorted_operations_list_by_datetime, formatted_the_operation, get_executed_only
import pathlib

# Загруженный список операций в формате JSON
PATH = pathlib.Path(pathlib.Path.cwd(), "operations.json")



# Отсортированный по дате и времени список операций


# Счетчик выводимых операций на экран
count_operations = 0


def main():
    """
    Функция вывода на экран последних 5 выполненных операций
    """
    # Список операций переведенный из JSON
    operations = load_operations(PATH)
    # Отсортированный по дате и времени список операций
    sorted_operations_by_date = sorted_operations_list_by_datetime(operations)
    # 5 последних удачных операций
    five_executed_operations = get_executed_only(sorted_operations_by_date, 5)

    # Цикл вывода на экран удачных операций
    for operation in five_executed_operations:
        print(formatted_the_operation(operation))


if __name__ == '__main__':
    main()
