import re
import codecs
import os
import openpyxl
import shutil
import os.path
import sys
import win_dialog
import win_open_file


def creating_file(tamplate_report_path, report_path, month, year): # Создание файла отчета

    def creating_file_path(report_path, month, year):
        file_path = ('%s %s %s.xlsx' % (report_path,
            month, year))  # Создаем путь к файлу с требуемым годом и месяцем
        check_existence = os.path.isfile(file_path)  # Проверяем существование файла с таким именем
        return check_existence  # True - если файл существует

    def creating_file(tamplate_report_path, report_path, month, year):
         shutil.copy('%s.xlsx'% (tamplate_report_path),
                    '%s %s %s.xlsx' % (report_path, month, year))# Cоздаем новый файл

    if creating_file_path(report_path, month, year) == True: # если файл сушествует
        click_resultat = win_dialog.window_dialog() # вызываем окно "файл существует, заменить файл?
        if click_resultat == 'Ok':
            try:
                myfile = open('%s %s %s.xlsx' % (report_path, month, year), "r+") # проверяем открыт ли сейчас файл(вызывет исключение)
                myfile.close() # закрываем если открылся и исключение не было вызвано
            except IOError:
                win_open_file.window_open_file()  # если открыт вызываем окно "файл открыт, закройте его"
            creating_file(tamplate_report_path, report_path, month, year)
        elif click_resultat == 'Cancel':
            sys.exit() # закрываем программу
    creating_file(tamplate_report_path, report_path, month, year) # если файл не существует создаем его

















