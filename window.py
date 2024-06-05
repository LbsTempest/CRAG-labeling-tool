# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.jsonl_path_label = QtWidgets.QLabel(self.centralwidget)
        self.jsonl_path_label.setText("")
        self.jsonl_path_label.setObjectName("jsonl_path_label")
        self.horizontalLayout.addWidget(self.jsonl_path_label)
        self.select_jsonl_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_jsonl_button.setObjectName("select_jsonl_button")
        self.horizontalLayout.addWidget(self.select_jsonl_button)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.start_line_label = QtWidgets.QLabel(self.centralwidget)
        self.start_line_label.setObjectName("start_line_label")
        self.horizontalLayout_3.addWidget(self.start_line_label)
        self.start_line_box = QtWidgets.QSpinBox(self.centralwidget)
        self.start_line_box.setObjectName("start_line_box")
        self.horizontalLayout_3.addWidget(self.start_line_box)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.end_line_label = QtWidgets.QLabel(self.centralwidget)
        self.end_line_label.setObjectName("end_line_label")
        self.horizontalLayout_4.addWidget(self.end_line_label)
        self.end_line_box = QtWidgets.QSpinBox(self.centralwidget)
        self.end_line_box.setObjectName("end_line_box")
        self.horizontalLayout_4.addWidget(self.end_line_box)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setObjectName("id_label")
        self.horizontalLayout_5.addWidget(self.id_label)
        self.id_input = QtWidgets.QLineEdit(self.centralwidget)
        self.id_input.setObjectName("id_input")
        self.horizontalLayout_5.addWidget(self.id_input)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.confirm_button = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_button.setObjectName("confirm_button")
        self.horizontalLayout_6.addWidget(self.confirm_button)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.work_widget = QtWidgets.QWidget(self.centralwidget)
        self.work_widget.setObjectName("work_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.work_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lines_layout = QtWidgets.QVBoxLayout()
        self.lines_layout.setObjectName("lines_layout")
        self.verticalLayout_3.addLayout(self.lines_layout)
        self.verticalLayout.addWidget(self.work_widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setObjectName("info_label")
        self.horizontalLayout_2.addWidget(self.info_label)
        self.is_sentences_correct = QtWidgets.QCheckBox(self.centralwidget)
        self.is_sentences_correct.setObjectName("is_sentences_correct")
        self.horizontalLayout_2.addWidget(self.is_sentences_correct)
        self.horizontalLayout_2.setStretch(0, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 10)
        self.verticalLayout.setStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.select_jsonl_button.setText(_translate("MainWindow", "选择文件"))
        self.start_line_label.setText(_translate("MainWindow", "起始行数"))
        self.end_line_label.setText(_translate("MainWindow", "结束行数"))
        self.id_label.setText(_translate("MainWindow", "学号"))
        self.confirm_button.setText(_translate("MainWindow", "确认"))
        self.info_label.setText(_translate("MainWindow", "TextLabel"))
        self.is_sentences_correct.setText(_translate("MainWindow", "CheckBox"))
