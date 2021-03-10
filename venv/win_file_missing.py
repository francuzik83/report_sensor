from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import  sys

def window_file_missing():

    def on_click():
        sys.exit()

    Form, Window = uic.loadUiType("files_are_missing.ui")
    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()

    form.pushButton.clicked.connect(on_click)

    app.exec_()

if __name__ == '__main__':
    window_file_missing()