# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LastPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LastPage(object):
    
    def setup(self, LastPage):
        LastPage.setObjectName("LastPage")
        LastPage.resize(794, 525)
        LastPage.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(LastPage)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 774, 464))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 750, 288))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.O_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.O_label.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"font: 14pt \"MS Reference Sans Serif\";")
        self.O_label.setText("")
        self.O_label.setObjectName("O_label")
        self.gridLayout_2.addWidget(self.O_label, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.R_q = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.R_q.setStyleSheet("border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"border-color:rgb(0, 168, 81);\n"
"font: 14pt \"MS Reference Sans Serif\";")
        self.R_q.setObjectName("R_q")
        self.gridLayout_3.addWidget(self.R_q, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Yes = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Yes.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"font: 14pt \"MS Reference Sans Serif\";")
        self.Yes.setObjectName("Yes")
        self.horizontalLayout.addWidget(self.Yes)
        self.No = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.No.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"font: 14pt \"MS Reference Sans Serif\";\n"
"")
        self.No.setObjectName("No")
        self.horizontalLayout.addWidget(self.No)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.New_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.New_button.setStyleSheet("#New_button\n"
"{background-color: rgb(85, 255, 127);\n"
"font: 14pt \"MS Reference Sans Serif\";\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"border-color:rgb(0, 168, 81);\n"
"}\n"
"#New_button:hover{\n"
"background-color: rgb(0, 170, 170);\n"
"}")
        self.New_button.setObjectName("New_button")
        self.New_button.clicked.connect(LastPage.hide)
        self.horizontalLayout_2.addWidget(self.New_button)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        LastPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LastPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName("menubar")
        self.menuMENU = QtWidgets.QMenu(self.menubar)
        self.menuMENU.setObjectName("menuMENU")
        LastPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LastPage)
        self.statusbar.setObjectName("statusbar")
        LastPage.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(LastPage)
        self.actionAbout.setObjectName("actionAbout")
        self.menuMENU.addSeparator()
        self.menuMENU.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMENU.menuAction())

        self.retranslate(LastPage)
        QtCore.QMetaObject.connectSlotsByName(LastPage)

    def retranslate(self, LastPage):
        _translate = QtCore.QCoreApplication.translate
        LastPage.setWindowTitle(_translate("LastPage", "D's"))
        self.R_q.setText(_translate("LastPage", "Was the Question Helpful?"))
        self.Yes.setText(_translate("LastPage", "YES"))
        self.No.setText(_translate("LastPage", "NO"))
        self.New_button.setText(_translate("LastPage", "Exit"))
        self.menuMENU.setTitle(_translate("LastPage", "MENU"))
        self.actionAbout.setText(_translate("LastPage", "About"))


if __name__ == "__main__":
    import sys
    app2 = QtWidgets.QApplication(sys.argv)
    LastPage = QtWidgets.QMainWindow()
    ui2 = Ui_LastPage()
    ui2.setup(LastPage)
    LastPage.show()
    sys.exit(app2.exec_())

