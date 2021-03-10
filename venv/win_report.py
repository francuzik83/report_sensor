from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def windows_report():
    def report():

        def on_click():
            shoose_date.month = form.list_month.currentText()
            shoose_date.year = form.list_year.currentText()
            window.close()


        Form, Window = uic.loadUiType("report.ui")
        app = QApplication([])
        window = Window()
        form = Form()
        form.setupUi(window)
        window.show()

        form.list_month.addItems(['Январь', 'Февраль', 'Март', 'Апрель',
                                          'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
                                          'Октябрь', 'Ноябрь', 'Декабрь'])
        form.list_year.addItems(['2015', '2016', '2017', '2018', '2019', '2020',
                                         '2021', '2022', '2023', '2024', '2025', '2026',
                                         '2027', '2028', '2029', '2030', '2031', '2032'])

        form.pushButton.clicked.connect(on_click)


        app.exec_()

    class The_date():
        month = ''
        year = ''

    shoose_date = The_date

    report()

    month_year = [shoose_date.month, shoose_date.year]

    return  month_year


if __name__ == '__main__':
    windows_report()