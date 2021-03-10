import openpyxl
import os
import json


def write_data(result, date_list, report_path, month, year): # Запись данных в файл отчета
    '''

    :param result: словарь вида('01_12_2019_02_00': {'Штофная Опоч. (подполье)_%': 36.3, 'Штофная Опоч. (подполье)_°C': 16.0,...)
    :param date_list: список с названием файлов(['01_12_2019_02_00', '01_12_2019_06_00',.....])
    :param report_path: Путь файла для создания отчета
    :param month: название месяца(напр."август")
    :param year: год
    :return:
    '''

    with open('list_sensor.json','r', encoding='utf-8') as f: # открываем файл с данными куда писать значения в отчет
        list_sensor = json.load(f)
        room_list = list_sensor.keys() # извлекаем список с названиями помещений

    wb = openpyxl.load_workbook('%s %s %s.xlsx' % (report_path, month, year)) # открываем созданную для отчета книгу Exel
    worksheet = wb['Отчет'] # делаем активным лист "отчет"
    for i, date in enumerate(date_list):
        worksheet['A%d'%(i+4)] = date # записываем дату и время(напр.01_12_2019_02_00) в соответств. ячейку(первая ячейка будет A5)
        get_dictionary_sensor = result[date] # достаем словарь с данными на это время(напр.01_12_2019_02_00)
        for name_sensor in room_list:
            if (name_sensor in get_dictionary_sensor) == True: # если название пом. есть в словаре с данными
                param_sensor = list_sensor[name_sensor] # по названию помещения извлекаем данные(ячейку куда писать и обозначение(напр.["FE", "%"]))
                number_cell_string_data = param_sensor[0] # извлекаем ячейку куда писать(напр."FE")
                number_cell_index_data = openpyxl.utils.column_index_from_string(number_cell_string_data)
                number_cell_string_unit = openpyxl.utils.get_column_letter(number_cell_index_data + 1)
                data_sensor = get_dictionary_sensor[name_sensor]
                worksheet['%s%d'%(number_cell_string_data, i+4)] = data_sensor
                worksheet['%s%d'%(number_cell_string_unit, i+4)] = param_sensor[1]
    wb.save('%s %s %s.xlsx' % (report_path, month, year))
    # TODO:

if __name__ == '__main__':
    write_data(3,3,3,3,3)


