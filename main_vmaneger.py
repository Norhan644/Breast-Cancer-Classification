from PyQt5 import QtWidgets
from views import main_view
from view_controllers import InputField

class BreastCancer(QtWidgets.QMainWindow, main_view.Ui_Mainwindow):
    def __init__(self):
        super(BreastCancer, self).__init__()
        self.setupUi(self)
        self.__app_fields = []
        for i in range(20):
            self.__app_fields.append(InputField('volume', 20, 10, 100, 'mm'))
            self.__app_layout.addWidget(self.app_fields)
        self.show()