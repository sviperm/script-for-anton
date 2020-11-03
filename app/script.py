import os
from os.path import isfile

input_str = input('Ввод: ')
list_of_files = os.scandir(os.path.join(__file__, '..'))
is_match = False


def check_input_in_file(filename):
    global is_match
    filepath = os.path.abspath(os.path.join(__file__, '..', filename))
    with open(filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if input_str in line:
                is_match = True
                print(f'{filename} - {line}')


try:
    for filename in list_of_files:
        filename_str = filename.name
        rules = (os.path.isfile(filename),
                 not filename_str.endswith('.exe'),
                 not filename_str.endswith('.py'))
        if all(rules):
            check_input_in_file(filename_str)

    if not is_match:
        print('Совпадений не найдено')
except Exception as e:
    print(e)

input('Нажмите на Enter, чтобы закрыть')
