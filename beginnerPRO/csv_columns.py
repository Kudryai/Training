import csv


def csv_columns(filename : csv) -> dict:
    """Функция должна возвращать словарь, в котором ключом является 
    название столбца файла filename, а значением — список элементов этого столбца."""
    result = {}
    with open(f'./beginnerPro/{filename}', 'r', encoding='utf8') as f:
        data = csv.DictReader(f, delimiter=';')
        for first_list in data:
            for go_list in first_list:
                result[go_list] = result.get(go_list, list()) + [first_list[go_list]]
    return result




print(csv_columns('salary_data.csv'))
