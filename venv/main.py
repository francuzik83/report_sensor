import win_report
import num_month
import creat_file
import ext_value
import json
import wr_data
import win_open_file




month_year = win_report.windows_report() # вызываем функцию с окном выбора месяца и года

month = month_year[0] # получаем название месяца(напр."август")
year = month_year[1]  # получаем год

with open('config.json','r', encoding='utf-8') as f: # открываем файл с настройками для создания отчета
    config = json.load(f)
    report_path = config['report_path'] # получаем путь для создания отчета
    tamplate_report_path = config['tamplate_report_path'] # получаем путь к папкам с данными для создания отчета
    data_path = config['data_path'] # получаем путь к шаблону для создания отчета 777


number_month = num_month.number_month(month) # название месяца в число

date_list = ext_value.get_list_of_name_file(data_path, number_month, year)  # получаем список с датами и временем для создания отчета

creat_file.creating_file(tamplate_report_path, report_path, month, year) # создаем файл отчета копируя шаблон

result = ext_value.dictionary_value(data_path, number_month, year) # получаем результирующий словарь с числами, названиями и данными

wr_data.write_data(result, date_list, report_path, month, year)  # создаем отчет









