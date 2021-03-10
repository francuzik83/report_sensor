import re
import codecs
import os
import win_file_missing
import win_open_file


def extract_value_file(list_file):
    '''

    :param list_file: список с абсолютными путями к файлам
    :return: словарь где ключ - помешение и обозначеаие параметра а объект - значение параметра

    example: {'Чердак (датчик 2)_°C': 0.6, 'Чердак (датчик 2)_%': 93.2,.......}

    '''
    dictionary_value = {}
    a = 5  # номер строки после которой начинаем заполнять словарь
    with open(list_file, 'r', encoding='utf-16 le') as f:  # Открываем файл

        for i, line in enumerate(f):  # Считываем строки файла(i- номер итерации)
            if i > a:
                data_extract = re.findall(r'"(.+?)"', line)  # извлекаем из строки значение параметра
                data = float(re.sub(r',', '.', data_extract[1]))  # конвертируем значение в float
                name_extract = re.findall(r'"(.+?)"', line)  # извлекаем из строки название помещения
                name = name_extract[0]  # делаем из списка строку
                number_sensor_extract = re.findall(r'"(.+?)"', line)  # извлекаем из строки обозначение параметра %-влажность, С- температура
                number_sensor = number_sensor_extract[2]  # делаем из списка строку
                key = '%s_%s' % (name, number_sensor)  # создаем новый ключ
                dictionary_value[key] = data  # записываем значение для нового ключа

    return dictionary_value  # получаем словарь где ключ - помешение и параметр а объект - значение параметра


def get_list_of_file(data_path, month, year):
    '''

    :param data_path: Путь файла к папкам с данными для создания отчета(из config.json)
    :param month: месяц(двузначное число)
    :param year: год(четырехзначное число)
    :return: список с абсолютными путями к файлам

    example: ['D:\\Python\\Example\\Rep\\12_2019\\01_12_2019_02_00.txt', 'D:\\Python\\Example\\Rep\\12_2019\\01_12_2019_06_00.txt',......]

    '''
    list_file = []
    try:
        for i, file in enumerate(os.listdir("%s\\%s_%s" % (data_path, month, year))):  # извлекаем названия файлов
            list_file.insert(i, "%s\\%s_%s\\%s"%(data_path, month, year, file))  # создаем список с полными путями к файлу

    except FileNotFoundError:
       win_file_missing.window_file_missing() # если файл не найден вызываем окно "файл не найден"

    return list_file

def get_list_of_name_file(data_path, month, year):
    '''

    :param data_path: Путь файла к папкам с данными для создания отчета(из config.json)
    :param month: месяц(двузначное число)
    :param year: год(четырехзначное число)
    :return: список с названием файлов

    example: ['01_12_2019_02_00', '01_12_2019_06_00',.....]


    '''
    name_file = []
    try:
        for i, file in enumerate(os.listdir("%s\\%s_%s" % (data_path, month, year))): # извлекаем названия файлов
            name_file_extract = re.findall(r'(\d+_\d+_\d+_\d+_\d+).txt', file) # убираем разрешение фаилов
            name_file_converting = name_file_extract[0] # делаем из списка строку
            name_file.insert(i, name_file_converting) #Создаем список с названием файлов
    except FileNotFoundError:
       win_file_missing.window_file_missing() # если файл не найден вызываем окно "файл не найден"

    return name_file


def get_value_sensor(result, key_result, list_sensor):
    '''

    :param result: результирующий словарь({'01_12_2019_02_00': {'Штофная Опоч. (подполье)_%': 36.3, 'Штофная Опоч. (подполье)_°C': 16.0,....)
    :param key_result: ключи результируещего словаря(['01_12_2019_02_00', '01_12_2019_06_00'
    :param list_sensor: Помещение и параметр('Штофная Опоч. (подполье)_%')
    :return: все найденные значения датчика по ключу 'list_sensor'
    '''
    value_sensor = []
    for i, j in enumerate(key_result): #Перебираем ключи результирующего словаря
        dictionary_date = result.get(j) #Получааем значение для ключа(словарь)
        value_sensor.insert(i, dictionary_date.get(list_sensor)) #Ищем в полученном словаре значение для ключа 'list_sensor'
    return value_sensor


def dictionary_value(data_path, month, year):
    '''
    :param data_path: Путь файла к папкам с данными для создания отчета(из config.json)
    :param month: месяц(двузначное число)
    :param year: год(четырехзначаое число)
    :return: словарь вида('01_12_2019_02_00': {'Штофная Опоч. (подполье)_%': 36.3, 'Штофная Опоч. (подполье)_°C': 16.0,...)
    '''

    result = {}
    key_result = get_list_of_name_file(data_path, month, year) # вызываем функцию для ключей словаря('01_12_2019_02_00', '01_12_2019_06_00'...)

    for i, j in enumerate(get_list_of_file(data_path, month, year)):  # вызываем функцию для извлечения списка всех файлов
        key = key_result[i]
        result[key] = extract_value_file(j) # присваиваем ключу значения

    return result


