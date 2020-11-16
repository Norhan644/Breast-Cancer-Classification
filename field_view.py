# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/field_form.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(382, 81)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.field_lbl = QtWidgets.QLabel(Form)
        self.field_lbl.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.field_lbl.setFont(font)
        self.field_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.field_lbl.setObjectName("field_lbl")
        self.horizontalLayout.addWidget(self.field_lbl)
        self.val_edit = QtWidgets.QLineEdit(Form)
        self.val_edit.setMinimumSize(QtCore.QSize(30, 30))
        self.val_edit.setObjectName("val_edit")
        self.horizontalLayout.addWidget(self.val_edit)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.field_lbl.setText(_translate("Form", "TextLabel"))

