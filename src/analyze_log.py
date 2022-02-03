from src.file_manager import readFile
from src.filter_function import (
    top_dishes,
    count_hamburger,
    dishes_not_joao,
    joao_is_absent,
)


def analyze_log(path_to_file):
    # raise NotImplementedError
    list_data = readFile(path_to_file)
    print(list_data)

    top_dishes(list_data)
    count_hamburger(list_data)
    dishes_not_joao(list_data)
    joao_is_absent(list_data)
