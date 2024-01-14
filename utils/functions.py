import json
from datetime import datetime
import os.path


def get_format_date(input_date):
    """Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018)."""


    # Преобразуем строку в формат datetime
    date_object = datetime.strptime(input_date, "%Y-%m-%dT%H:%M:%S.%f")

    # Форматируем дату в нужный вид
    formatted_date = date_object.strftime("%d.%m.%Y")

    return formatted_date


def get_format(transaction):
    ''' проводим форматирование даты и маскировку номеров счетов
    с отработкой случайностей отсутствия _откуда и куда_'''


    transaction['date'] = get_format_date(transaction['date'])
    try:
        transaction['from'] = get_mask(transaction['from'])
    except KeyError:
        transaction['from'] = 'Внесение на счёт'
    try:
        transaction['to'] = get_mask(transaction['to'])
    except KeyError:
        transaction['to'] = 'Неизвестно'
    return

def get_mask(account_number):
    """Номер карты замаскирован и не отображается целиком в формате
    XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по
    блокам по 4 цифры, разделенных пробелом)
    отработка неверных номеров"""


    result = account_number.split(' ')
    #print(result)
    account_number_ret = ''
    result_number = result[-1]
    if len(result_number) == 16:
        result[-1] = result_number[:4] + " " + result_number[4:6] + "**" + " " + "****" + " " + result_number[-4:]
        account_number_ret = ' '.join(result)
        return account_number_ret
    if len(result_number) == 20:
        result[-1] = "**" + result_number[:4]
        account_number_ret = ' '.join(result)
        return account_number_ret
    else:
        return "Неправильная длина номера карты/счета"




def open_file():
    """ Открыть файл JSON"""


    operations_json = os.path.join('utils', 'operations.json')
    with open(operations_json, 'r', encoding="utf-8") as file:
        operations_list = json.load(file)
        return operations_list


def list_executed(data):
    """ Создание списка успешных выполненных транзакций"""


    new_list_exe = []
    try:
        for trans_exe in data:
            if trans_exe['state'] == "EXECUTED":
                new_list_exe.append(trans_exe)
    except KeyError:  # обработка исключения, если встречается пустой словарь
        print()
    return new_list_exe