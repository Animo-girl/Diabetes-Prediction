

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUiAbout(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(740, 674)
        Dialog.setMinimumSize(QtCore.QSize(740, 674))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo other without back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("logo other without back.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setMinimumSize(QtCore.QSize(716, 545))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 720, 654))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setMinimumSize(QtCore.QSize(228, 256))
        self.label_2.setStyleSheet("background-image: url(logo other without back.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setStyleSheet("color: rgb(0, 33, 100);\n"
"background-color: rgb(146, 223, 243);\n"
"font: 75 14pt \"Berlin Sans FB Demi\";\n"
"\n"
"\n"
"\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUiAbout(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUiAbout(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt;\">Hola&nbsp;&nbsp;!!!! Myself Aastha Parmar. </span></p><p align=\"center\"><span style=\" font-size:12pt;\">Thank you for using this application. Hope this appliaction would help you to find your answers. </span></p><p align=\"center\"><span style=\" font-size:12pt;\">If you have any queries please feel free to write me at </span></p><p align=\"center\"><span style=\" font-size:12pt;\">aastha.parmar@somaiya.edu</span></p><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">All rights reserved</span></p><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
