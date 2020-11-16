from PyQt5 import QtWidgets
from view_controllers import BreastCancer


#load ui and save it python code
# pyuic5 forms/field_form.ui -o views/field_view.py
def __test__():
    app = QtWidgets.QApplication([])
    f1 = BreastCancer
    app.exec_()

if __name__ == '__main__':
    __test__()
