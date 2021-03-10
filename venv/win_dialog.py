
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


def window_dialog():
    def dialog():

        def on_clik():
            clik.ok = True

        def cancel_clik():
            clik.cancel = True


        Form, Window = uic.loadUiType("dialog.ui")
        app = QApplication([])
        window = Window()
        form = Form()
        form.setupUi(window)
        window.show()
        form.buttonBox.accepted.connect(on_clik)
        form.buttonBox.rejected.connect(cancel_clik)
        app.exec_()

    class Clik():
        ok = False
        cancel = False

    clik = Clik

    dialog()

    clik_resultat = 'Error'
    if clik.ok == True:
       clik_resultat = 'Ok'
    elif clik.cancel == True:
        clik_resultat = 'Cancel'

    return clik_resultat


if __name__ == '__main__':
    window_dialog()




