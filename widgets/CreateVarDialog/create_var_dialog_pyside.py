# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PyIDA\widgets\CreateVarDialog\create_var_dialog.ui'
#
# Created: Wed Nov 16 11:14:32 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CreateVarDialog(object):
    def setupUi(self, CreateVarDialog):
        CreateVarDialog.setObjectName("CreateVarDialog")
        CreateVarDialog.resize(487, 510)
        CreateVarDialog.setStyleSheet("background-color: rgb(34, 44, 40);\n"
"color: rgb(248, 248, 248);")
        self.verticalLayout = QtGui.QVBoxLayout(CreateVarDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(CreateVarDialog)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.class_name_edit = QtGui.QLineEdit(CreateVarDialog)
        self.class_name_edit.setObjectName("class_name_edit")
        self.horizontalLayout_2.addWidget(self.class_name_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(CreateVarDialog)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.var_name_edit = QtGui.QLineEdit(CreateVarDialog)
        self.var_name_edit.setObjectName("var_name_edit")
        self.horizontalLayout_3.addWidget(self.var_name_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtGui.QLabel(CreateVarDialog)
        self.label_4.setMinimumSize(QtCore.QSize(80, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.var_type_edit = QtGui.QLineEdit(CreateVarDialog)
        self.var_type_edit.setObjectName("var_type_edit")
        self.horizontalLayout_5.addWidget(self.var_type_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(CreateVarDialog)
        self.label_3.setMinimumSize(QtCore.QSize(80, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.var_offset_edit = QtGui.QLineEdit(CreateVarDialog)
        self.var_offset_edit.setInputMask("")
        self.var_offset_edit.setObjectName("var_offset_edit")
        self.horizontalLayout_4.addWidget(self.var_offset_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.result_window = QtGui.QPlainTextEdit(CreateVarDialog)
        self.result_window.setReadOnly(True)
        self.result_window.setObjectName("result_window")
        self.verticalLayout.addWidget(self.result_window)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_btn = QtGui.QPushButton(CreateVarDialog)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout.addWidget(self.ok_btn)
        self.cancel_btn = QtGui.QPushButton(CreateVarDialog)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(CreateVarDialog)
        QtCore.QMetaObject.connectSlotsByName(CreateVarDialog)

    def retranslateUi(self, CreateVarDialog):
        CreateVarDialog.setWindowTitle(QtGui.QApplication.translate("CreateVarDialog", "Create variable", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CreateVarDialog", "Class name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CreateVarDialog", "var name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CreateVarDialog", "var type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CreateVarDialog", "offset:", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_btn.setText(QtGui.QApplication.translate("CreateVarDialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("CreateVarDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
