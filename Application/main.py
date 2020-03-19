

from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
import numpy as np
import time
import re
from About import *



firebaseConfig = {
     "apiKey": "AIzaSyDEi-6Vm4DqAyC69kbBUXMCRSMhKJcHt3w",
    "authDomain": "udata-b0869.firebaseapp.com",
    "databaseURL": "https://udata-b0869.firebaseio.com",
    "projectId": "udata-b0869",
    "storageBucket": "udata-b0869.appspot.com",
    "messagingSenderId": "855266842555",
    "appId": "1:855266842555:web:255b71f913ff83c33b969e",
    "measurementId": "G-8CVRQ9ET6L"

    }

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


class Ui_DialogSignin(object):
    
    def check(self):
        self.Email = self.EmailEdit.text()
        self.CreatePassword = self.CreatePasswordEdit.text()
        self.ConfirmPassword = self.ConfirmPasswordEdit.text()
        self.Info_label1.setStyleSheet('color:red;\n')

        self.identifier = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",self.Email)
    
        if(self.identifier == None):
            
            self.Info_label1.setText("Please enter valid email!!")
        else:
            self.Info_label1.setText("Vaild Email!!")
            if self.CreatePassword != self.ConfirmPassword:
                self.Info_label1.setText("Passwords Dont match!!Please enter valid passwords!!")
            else:
                # print("Everything is alright!!")    
                
                self.Firebase()
        
    def Firebase(self):
        try:
            email = self.EmailEdit.text()
            password = self.CreatePasswordEdit.text()
            user = auth.create_user_with_email_and_password(email,password)           
            self.Info_label1.setText("Successful!!")
            self.Login2
            
            
        except Exception as e:
            self.Info_label2.setText(str(e))
            print(e)
    
        
    def Login2(self):
        self.Dialoglog = QtWidgets.QDialog()
        self.setupUiLogin(self.Dialoglog)
        self.Dialoglog.show()
        DialogSignin.hide()
    
    def checkLogin(self):
        self.Email = self.EamilEdit.text()
        self.identifier = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",self.Email)
        if(self.identifier == None):
            self.Info_label1.setStyleSheet('color:red;\n')
            self.Info_label1.setText("Please enter valid email!!")
        else:
            self.Info_label1.setText("Vaild Email!!")
        
            self.FirebaseLogin()
    
    def FirebaseLogin(self):

        try:
            
            email = self.EmailEdit.text()
            password = self.CreatePasswordEdit.text()
            login = auth.sign_in_with_email_and_password(email,password)            
            self.Info_label2.setText("Login Was Successful")
            self.mainWindow()
                                    
        except Exception as e:
            
            # m = re.match('(.*)message"(.*)"',str(e)).group(0)
            # n = re.search('/s(.*)',m).group(0)
            self.Info_label2.setText(str(e))
    
    def mainWindow(self):
        self.MainWindow = QtWidgets.QMainWindow()        
        self.setupUimain(self.MainWindow)
        self.MainWindow.show()     
        self.Dialoglog.hide()

    def forgotPassword(self):
        email = self.EmailEdit.text()        
        auth.send_password_reset_email(email)
        self.Info_label1.setText("An email is sent to you please follow the link.")
         
    def setupUiLogin(self, DialogLogin):
        DialogLogin.setObjectName("DialogLogin")
        DialogLogin.resize(900, 400)
        DialogLogin.setMinimumSize(QtCore.QSize(900, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo other without back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("logo other without back.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        DialogLogin.setWindowIcon(icon)
        DialogLogin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(DialogLogin)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(DialogLogin)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 880, 380))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelup = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelup.setText("")
        self.labelup.setObjectName("labelup")
        self.verticalLayout_5.addWidget(self.labelup)
        self.logo_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.logo_label.setMinimumSize(QtCore.QSize(225, 258))
        self.logo_label.setStyleSheet("background-image: url(logo other without back.png);")
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.verticalLayout_5.addWidget(self.logo_label)
        self.labeldown = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labeldown.setText("")
        self.labeldown.setObjectName("labeldown")
        self.verticalLayout_5.addWidget(self.labeldown)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 20, 10, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.EmailLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.EmailLabel.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.EmailLabel.setObjectName("EmailLabel")
        self.verticalLayout.addWidget(self.EmailLabel)
        self.PasswordLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.PasswordLabel.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.verticalLayout.addWidget(self.PasswordLabel)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.EmailEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.EmailEdit.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"")
        self.EmailEdit.setObjectName("EmailEdit")
        self.verticalLayout_2.addWidget(self.EmailEdit)
        self.CreatePasswordEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.CreatePasswordEdit.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"")
        self.CreatePasswordEdit.setText("")
        self.CreatePasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CreatePasswordEdit.setObjectName("CreatePasswordEdit")
        self.verticalLayout_2.addWidget(self.CreatePasswordEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Info_label1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Info_label1.setText("")
        self.Info_label1.setObjectName("Info_label1")
        self.verticalLayout_3.addWidget(self.Info_label1)
        self.Info_label2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Info_label2.setText("")
        self.Info_label2.setObjectName("Info_label2")
        self.verticalLayout_3.addWidget(self.Info_label2)
        self.GO_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.GO_button.setStyleSheet("#GO_button{\n"
"    font: 14pt \"MS Reference Sans Serif\";\n"
"\n"
"background-color: rgb(146,223,243);\n"
"\n"
"}\n"
"\n"
"#GO_button:hover{\n"
"font: 14pt \"MS Reference Sans Serif\";\n"
"color:rgb(255, 255, 255);\n"
"    background-color: rgb(68, 68, 102);\n"
"border-width:5px;\n"
"border-style:dotted;\n"
"border-color:rgb(170, 170, 127);\n"
"}")
        self.GO_button.setObjectName("GO_button")
        self.verticalLayout_3.addWidget(self.GO_button)
        self.GO_button.clicked.connect(self.mainWindow)
        self.ForgotPasswordButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ForgotPasswordButton.setStyleSheet("color: rgb(0,33,100);\n"
"font: 75 12pt \"MS Serif\";")
        self.ForgotPasswordButton.setObjectName("ForgotPasswordButton")
        self.ForgotPasswordButton.clicked.connect(self.forgotPassword)
        self.verticalLayout_3.addWidget(self.ForgotPasswordButton)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUiLogin(DialogLogin)
        QtCore.QMetaObject.connectSlotsByName(DialogLogin)

    def retranslateUiLogin(self, DialogLogin):
        _translate = QtCore.QCoreApplication.translate
        DialogLogin.setWindowTitle(_translate("DialogLogin", "Login"))
        self.EmailLabel.setText(_translate("DialogLogin", "Email"))
        self.PasswordLabel.setText(_translate("DialogLogin", "Password"))
        self.GO_button.setText(_translate("DialogLogin", "Go"))
        self.ForgotPasswordButton.setText(_translate("DialogLogin", "Forgot Password?Click here."))
     
    
    def setupUiSignIn(self, DialogSignin):
        DialogSignin.setObjectName("DialogSignin")
        DialogSignin.resize(900, 422)
        DialogSignin.setMinimumSize(QtCore.QSize(900, 422))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo other without back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("logo other without back.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        DialogSignin.setWindowIcon(icon)
        DialogSignin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(DialogSignin)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(DialogSignin)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 880, 402))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelup = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelup.setText("")
        self.labelup.setObjectName("labelup")
        self.verticalLayout_5.addWidget(self.labelup)
        self.logo_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.logo_label.setMinimumSize(QtCore.QSize(225, 258))
        self.logo_label.setStyleSheet("background-image: url(logo other without back.png);")
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.verticalLayout_5.addWidget(self.logo_label)
        self.labeldown = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labeldown.setText("")
        self.labeldown.setObjectName("labeldown")
        self.verticalLayout_5.addWidget(self.labeldown)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.NameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.NameLabel.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.NameLabel.setObjectName("NameLabel")
        self.verticalLayout.addWidget(self.NameLabel)
        self.EmailLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.EmailLabel.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.EmailLabel.setObjectName("EmailLabel")
        self.verticalLayout.addWidget(self.EmailLabel)
        self.CreatePasswordLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.CreatePasswordLabel.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.CreatePasswordLabel.setObjectName("CreatePasswordLabel")
        self.verticalLayout.addWidget(self.CreatePasswordLabel)
        self.ConfirmPasswordLAbel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ConfirmPasswordLAbel.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.ConfirmPasswordLAbel.setObjectName("ConfirmPasswordLAbel")
        self.verticalLayout.addWidget(self.ConfirmPasswordLAbel)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.NameEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.NameEdit.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"")
        self.NameEdit.setObjectName("NameEdit")
        self.verticalLayout_2.addWidget(self.NameEdit)
        self.EmailEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.EmailEdit.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"")
        self.EmailEdit.setObjectName("EmailEdit")
        self.verticalLayout_2.addWidget(self.EmailEdit)
        self.CreatePasswordEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.CreatePasswordEdit.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"")
        self.CreatePasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CreatePasswordEdit.setObjectName("CreatePasswordEdit")
        self.verticalLayout_2.addWidget(self.CreatePasswordEdit)
        self.ConfirmPasswordEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.ConfirmPasswordEdit.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"")
        self.ConfirmPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ConfirmPasswordEdit.setObjectName("ConfirmPasswordEdit")
        self.verticalLayout_2.addWidget(self.ConfirmPasswordEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Info_label1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Info_label1.setText("")
        self.Info_label1.setObjectName("Info_label1")
        self.verticalLayout_3.addWidget(self.Info_label1)
        self.Info_label2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Info_label2.setText("")
        self.Info_label2.setObjectName("Info_label2")
        self.verticalLayout_3.addWidget(self.Info_label2)
        self.GO_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.GO_button.setStyleSheet("#GO_button{\n"
"    font: 14pt \"MS Reference Sans Serif\";\n"
"\n"
"background-color: rgb(146,223,243);\n"
"\n"
"}\n"
"\n"
"#GO_button:hover{\n"
"font: 14pt \"MS Reference Sans Serif\";\n"
"color:rgb(255, 255, 255);\n"
"    background-color: rgb(68, 68, 102);\n"
"border-width:5px;\n"
"border-style:dotted;\n"
"border-color:rgb(170, 170, 127);\n"
"}")
        self.GO_button.setObjectName("GO_button")
        self.verticalLayout_3.addWidget(self.GO_button)
        self.GO_button.clicked.connect(self.check)
        self.LoginButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.LoginButton.setStyleSheet("color: rgb(0,33,100);\n"
"font: 75 12pt \"MS Serif\";")
        self.LoginButton.setObjectName("LoginButton")
        self.LoginButton.clicked.connect(self.Login2)
        self.verticalLayout_3.addWidget(self.LoginButton)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUiSignIn(DialogSignin)
        QtCore.QMetaObject.connectSlotsByName(DialogSignin)

    def retranslateUiSignIn(self, DialogSignin):
        _translate = QtCore.QCoreApplication.translate
        DialogSignin.setWindowTitle(_translate("DialogSignin", "Sign Up Page"))
        self.NameLabel.setText(_translate("DialogSignin", "Name"))
        self.EmailLabel.setText(_translate("DialogSignin", "Email"))
        self.CreatePasswordLabel.setText(_translate("DialogSignin", "Create Password"))
        self.ConfirmPasswordLAbel.setText(_translate("DialogSignin", "Confirm Password"))
        self.GO_button.setText(_translate("DialogSignin", "Go"))
        self.LoginButton.setText(_translate("DialogSignin", "Already Have an Account?Click here."))

    def checkmistaes(self):
        if self.Noa_box.isChecked() == True and self.H_box.isChecked() == True or self.C_box.isChecked() == True or self.P_box.isChecked() == True:
            self.WarningLabel.setStyleSheet("color:red; font: 12pt'MS Sans Serif'")
            self.WarningLabel.setText("Please Select None of the above or the other cormobidities!!")
            if self.Name_box.text == "" or self.Age_box.value() == 0 or self.Weight_box.value() == 0 or self.Height_box.value == 0 or self.PPG_box.value == 0 or self.FPG_box.value == 0 or self.HbA1c_box.value == 0:
                self.LabelWarning2.setStyleSheet("color:red; font: 12pt'MS Sans Serif'")
                self.LabelWarning2.setText("Please fill all the details!!")
        else:
            self.LabelWarning2.setText("Valid Inputs Given!!!")
            self.call2()

    def call2(self):
        self.LabelWarning2.setText("")
        self.WarningLabel.setText("")
        if __name__ == '__main__':
            print("Into this shit")
            
            self.Name_box_text = self.Name_box.text()
            self.Age_box_text = self.Age_box.value()
            self.Weight_box_text = self.Weight_box.value()
            self.Height_box_text = self.Height_box.value()
            self.PPG_box_text = self.PPG_box.value()
            self.FPG_box_text = self.FPG_box.value()
            self.HbA1c_box_text = self.HbA1c_box.value()
            print("calling Lastpage")
            self.winn = QtWidgets.QMainWindow()
            
            self.setup(self.winn)
            self.winn.show()            
            self.a = self.Age(self.Age_box_text)
            self.listo = self.cormobidities()
            self.hei = self.height_entered(self.Height_box_text)
            self.Bmi = self.BMI(self.hei,self.Weight_box_text)
            self.b = self.BMI_check(self.Bmi)
            
            self.np1 = [self.a,self.b,self.HbA1c_box_text,self.FPG_box_text,self.PPG_box_text,self.listo]
            print("Performing evrythong!")
            m = self.np1.pop(-1)
            self.np1 = self.np1 + m
            self.np1 = np.asarray(self.np1)
            self.np1 = self.np1.reshape(1,-1)      
            self.Name_box.setText("")
            self.Age_box.setValue(0)
            self.Weight_box.setValue(0)
            self.Height_box.setValue(0)
            self.PPG_box.setValue(0)
            self.FPG_box.setValue(0)
            self.HbA1c_box.setValue(0)

            import pickle
            model = pickle.load(open('Model File.sav','rb'))
            y_predrf = model.predict(self.np1)
            self.Name_box.setText("")
            #y_predrf = bag.predict(self.np1)
            if y_predrf[0] == 0:
                out = "You don't require a long term treatment,just follow the following...."
            elif y_predrf[0] == 1:
                out = "The Duration for the treatment would be 6 months to 3 years depending on your health"
            elif y_predrf[0] == 2:
                out = "The Duration for the treatment would be 3-10 years"
            elif y_predrf[0] == 3:
                out = "The Duration for the treatment would be 11-20 years or more than that"
            
            classifiersk = pickle.load(open('Model File Treatment.sav','rb'))
            y_predPres = classifiersk.predict(self.np1)
            for i in y_predPres:
                break
            bmi_out = str(self.Bmi)
            out = "Your BMI is " + bmi_out + "\n" + out + "\nYou will have to follow the following\n" + i
            self.O_label.setText(out)
            
             
    def setup(self, LastPage):
        LastPage.setObjectName("LastPage")
        LastPage.resize(794, 525)
        LastPage.setMinimumSize(QtCore.QSize(794, 525))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo other without back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("logo other without back.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        LastPage.setWindowIcon(icon)
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
        self.O_label.setStyleSheet("background-color: rgb(146,223,243);\n"
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
"border-color:rgb(0,33,100);\n"
"font: 14pt \"MS Reference Sans Serif\";")
        self.R_q.setObjectName("R_q")
        self.gridLayout_3.addWidget(self.R_q, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Yes = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Yes.setStyleSheet("background-color: rgb(146,223,243);\n"
"font: 14pt \"MS Reference Sans Serif\";")
        self.Yes.setObjectName("Yes")
        self.horizontalLayout.addWidget(self.Yes)
        self.No = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.No.setStyleSheet("background-color: rgb(146,223,243);\n"
"font: 14pt \"MS Reference Sans Serif\";")
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
"{background-color: rgb(146,223,243);\n"
"font: 14pt \"MS Reference Sans Serif\";\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"border-color:rgb(0, 33,100);\n"
"}\n"
"#New_button:hover{\n"
"background-color: rgb(0, 170, 170);\n"
"}")
        self.New_button.setObjectName("New_button")
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
        self.actionNew = QtWidgets.QAction(LastPage)
        self.actionNew.setObjectName("actionNew")
        self.actionAbout = QtWidgets.QAction(LastPage)
        self.actionAbout.setObjectName("actionAbout")
        self.menuMENU.addAction(self.actionNew)
        self.menuMENU.addSeparator()
        self.menuMENU.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMENU.menuAction())

        self.retranslate(LastPage)
        QtCore.QMetaObject.connectSlotsByName(LastPage)

    def retranslate(self, LastPage):
        _translate = QtCore.QCoreApplication.translate
        LastPage.setWindowTitle(_translate("LastPage", "MainWindow"))
        self.R_q.setText(_translate("LastPage", "Was the Question Helpful?"))
        self.Yes.setText(_translate("LastPage", "YES"))
        self.No.setText(_translate("LastPage", "NO"))
        self.New_button.setText(_translate("LastPage", "New"))
        self.menuMENU.setTitle(_translate("LastPage", "MENU"))
        self.actionNew.setText(_translate("LastPage", "New"))
        self.actionAbout.setText(_translate("LastPage", "About"))

    
    def Age(self,age):
        
        age = int(age)
        try:
            if age <= 25:
               age = 12.5
               return age            
            elif age >= 26 and age <= 35:
                age = 30.5
                return age
            elif age >= 36 and age <= 50:
                age = 43.0
                return age
            elif age >= 51 and age <= 150:
                age = 75.5
                return age
            else:
                print("Invalid Age please enter valid age!!")
                
        except Exception as e:
            return e
    
    def height_entered(self,Height):        
        self.Height = Height
        if self.Inches_button.isChecked() == True:
            return float(self.Height * 0.0254)
        elif self.Foot_button.isChecked() == True:
            return float(self.Height * 0.3048)
        elif self.Cms_button.isChecked() == True:
            return float(self.Height)

    def BMI(self,height,Weight):
        bmi =  Weight/height ** 2
        return bmi

    def cormobidities(self):
        list_of_cormobidities = []
        
        if self.H_box.isChecked() == True and self.D_box.isChecked() == True and self.C_box.isChecked() == True and self.P_box.isChecked() == True:
            list_of_cormobidities = [1,1,1,1]
        elif self.H_box.isChecked() == True and self.D_box.isChecked() == True and self.C_box.isChecked() == True and self.P_box.isChecked() == False:
            list_of_cormobidities = [1,1,1,0]
        elif self.H_box.isChecked() == True and self.D_box.isChecked() == True and self.C_box.isChecked() == False and self.P_box.isChecked() == False:
            list_of_cormobidities = [1,1,0,0]
        elif self.H_box.isChecked() == True and self.D_box.isChecked() == False and self.C_box.isChecked() == False and self.P_box.isChecked() == False:
            list_of_cormobidities = [1,0,0,0]
        elif self.H_box.isChecked() == False and self.D_box.isChecked() == False and self.C_box.isChecked() == False and self.P_box.isChecked() == False:
            list_of_cormobidities = [0,0,0,0]
        elif self.H_box.isChecked() == True and self.D_box.isChecked() == True and self.C_box.isChecked() == False and self.P_box.isChecked() == True:
            list_of_cormobidities = [1,1,0,1]
        elif self.H_box.isChecked() == True and self.D_box.isChecked() == False and self.C_box.isChecked() == False and self.P_box.isChecked() == True:
            list_of_cormobidities = [1,0,0,1]
        elif self.H_box.isChecked() == False and self.D_box.isChecked() == False and self.C_box.isChecked() == False and self.P_box.isChecked() == True:
            list_of_cormobidities = [0,0,0,1]
        elif self.H_box.isChecked() == True and self.D_box.isChecked() == False and self.C_box.isChecked() == True and self.P_box.isChecked() == True:
            list_of_cormobidities = [1,0,1,1]
        elif self.H_box.isChecked() == False and self.D_box.isChecked() == False and self.C_box.isChecked() == True and self.P_box.isChecked() == True:
            list_of_cormobidities = [0,0,1,1]
        elif self.H_box.isChecked() == False and self.D_box.isChecked() == True and self.C_box.isChecked() == True and self.P_box.isChecked() == True:
            list_of_cormobidities = [0,1,1,1]
        elif self.H_box.isChecked() == False and self.D_box.isChecked() == True and self.C_box.isChecked() == True and self.P_box.isChecked() == False:
            list_of_cormobidities = [0,1,1,0]
        elif self.H_box.isChecked() == False and self.D_box.isChecked() == True and self.C_box.isChecked() == False and self.P_box.isChecked() == True:
            list_of_cormobidities = [0,1,0,1]
        elif self.H_box.isChecked() == False and self.D_box.isChecked() == False and self.C_box.isChecked() == True and self.P_box.isChecked() == False:
            list_of_cormobidities = [0,0,1,0]
        elif self.H_box.isChecked() == False and self.D_box.isChecked() == True and self.C_box.isChecked() == False and self.P_box.isChecked() == False:
            list_of_cormobidities = [0,1,0,0]
        elif self.H_box.isChecked() == True and self.D_box.isChecked() == False and self.C_box.isChecked() == True and self.P_box.isChecked() == False:
            list_of_cormobidities = [1,0,1,0]
            
        return list_of_cormobidities

    def BMI_check(self,bmi):
        if bmi < 18.5:
            return 0
        elif bmi >= 18.5 and bmi <= 24.9:
            return 1
        elif bmi > 24.9 and bmi <= 29.9:
            return 2
        elif bmi > 29.9  and bmi <= 39.9:
            return 3
        elif bmi >= 40:
            return 4
        
    def setupUimain(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 722)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo other without back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("logo other without back.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 826, 661))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(20, 10, 5, 10)
        self.gridLayout_2.setHorizontalSpacing(50)
        self.gridLayout_2.setVerticalSpacing(30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Name_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Name_label.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Name_label.setObjectName("Name_label")
        self.gridLayout_2.addWidget(self.Name_label, 0, 0, 1, 1)
        self.Name_box = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.Name_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"")
        self.Name_box.setObjectName("Name_box")
        self.gridLayout_2.addWidget(self.Name_box, 0, 1, 1, 1)
        
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(20, 10, 10, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Age_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Age_label.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Age_label.setObjectName("Age_label")
        self.horizontalLayout_3.addWidget(self.Age_label)
        self.Age_box = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.Age_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"")
        self.Age_box.setObjectName("Age_box")
        self.horizontalLayout_3.addWidget(self.Age_box)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(20, 10, 10, 10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Weight_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Weight_label.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Weight_label.setObjectName("Weight_label")
        self.horizontalLayout_7.addWidget(self.Weight_label)
        self.Weight_box = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.Weight_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"")
        self.Weight_box.setMaximum(1000)
        self.Weight_box.setObjectName("Weight_box")
        self.horizontalLayout_7.addWidget(self.Weight_box)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(15, 10, 10, 10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Height_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Height_label.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Height_label.setObjectName("Height_label")
        self.horizontalLayout_5.addWidget(self.Height_label)
        self.Height_box = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.Height_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"")
        self.Height_box.setMaximum(19999.99)
        self.Height_box.setObjectName("Height_box")
        self.horizontalLayout_5.addWidget(self.Height_box)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Inches_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Inches_button.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0, 33,100);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Inches_button.setObjectName("Inches_button")
        self.horizontalLayout.addWidget(self.Inches_button)
        self.Cms_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Cms_button.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0, 33,100);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Cms_button.setObjectName("Cms_button")
        self.horizontalLayout.addWidget(self.Cms_button)
        self.Foot_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Foot_button.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0, 33,100);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Foot_button.setObjectName("Foot_button")
        self.horizontalLayout.addWidget(self.Foot_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.HbA1c_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.HbA1c_label.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-bottom-color: rgb(0, 33,100);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);")
        self.HbA1c_label.setObjectName("HbA1c_label")
        self.gridLayout_3.addWidget(self.HbA1c_label, 0, 2, 1, 1)
        self.PPG_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.PPG_label.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-bottom-color: rgb(0, 33,100);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);\n"
"")
        self.PPG_label.setObjectName("PPG_label")
        self.gridLayout_3.addWidget(self.PPG_label, 0, 1, 1, 1)
        self.FPG_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.FPG_label.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-bottom-color: rgb(0, 33,100);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);")
        self.FPG_label.setObjectName("FPG_label")
        self.gridLayout_3.addWidget(self.FPG_label, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.FPG_box = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.FPG_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"")
        self.FPG_box.setMaximum(1000)
        self.FPG_box.setObjectName("FPG_box")
        self.horizontalLayout_6.addWidget(self.FPG_box)
        self.PPG_box = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.PPG_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"")
        self.PPG_box.setMaximum(1000)
        self.PPG_box.setObjectName("PPG_box")
        self.horizontalLayout_6.addWidget(self.PPG_box)
        self.HbA1c_box = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.HbA1c_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0,33,100);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"")
        self.HbA1c_box.setMaximum(1999.99)
        self.HbA1c_box.setObjectName("HbA1c_box")
        self.horizontalLayout_6.addWidget(self.HbA1c_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(10, 10, 10, 5)
        self.gridLayout_6.setSpacing(10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Q_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q_label.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0, 33,100);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Q_label.setObjectName("Q_label")
        self.gridLayout_6.addWidget(self.Q_label, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_5.setHorizontalSpacing(20)
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.H_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.H_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);\n"
"")
        self.H_box.setObjectName("H_box")
        self.horizontalLayout_2.addWidget(self.H_box)
        self.D_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.D_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);")
        self.D_box.setObjectName("D_box")
        self.horizontalLayout_2.addWidget(self.D_box)
        self.C_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.C_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);")
        self.C_box.setObjectName("C_box")
        self.horizontalLayout_2.addWidget(self.C_box)
        self.P_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.P_box.setMinimumSize(QtCore.QSize(160, 28))
        self.P_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);")
        self.P_box.setObjectName("P_box")
        self.horizontalLayout_2.addWidget(self.P_box)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.Noa_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Noa_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(146,223,243);")
        self.Noa_box.setObjectName("Noa_box")
        self.gridLayout_5.addWidget(self.Noa_box, 0, 0, 1, 1)
        self.WarningLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.WarningLabel.setText("")
        self.WarningLabel.setObjectName("WarningLabel")
        self.gridLayout_5.addWidget(self.WarningLabel, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LabelWarning2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.LabelWarning2.setText("")
        self.LabelWarning2.setObjectName("LabelWarning2")
        self.horizontalLayout_4.addWidget(self.LabelWarning2)
        self.Go_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Go_Button.setStyleSheet("#Go_Button{\n"
"    font: 14pt \"MS Reference Sans Serif\";\n"
"\n"
"background-color: rgb(146,223,243);\n"
"\n"
"}\n"
"\n"
"#Go_Button:hover{\n"
"font: 14pt \"MS Reference Sans Serif\";\n"
"color:rgb(255, 255, 255);\n"
"    background-color: rgb(68, 68, 102);\n"
"border-width:5px;\n"
"border-style:dotted;\n"
"border-color:rgb(170, 170, 127);\n"
"}")
        self.Go_Button.setObjectName("Go_Button")
        self.horizontalLayout_4.addWidget(self.Go_Button)
        self.Go_Button.clicked.connect(self.checkmistaes)
        self.Noa_box.setChecked(True)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 21))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuMENU = QtWidgets.QMenu(self.menubar)
        self.menuMENU.setObjectName("menuMENU")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # self.actionNew = QtWidgets.QAction(MainWindow)
        # self.actionNew.setObjectName("actionNew")
        # self.actionData = QtWidgets.QAction(MainWindow)
        # self.actionData.setObjectName("actionData")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        # self.menuMENU.addAction(self.actionNew)
        self.menuMENU.addSeparator()
        self.menuMENU.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMENU.menuAction())

        self.retranslateUimain(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionAbout.triggered.connect(lambda:self.aboutpage())
       
         
    def aboutpage(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUiAbout(self.Dialog)
        self.Dialog.show()
        
      
    def retranslateUimain(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "D's"))
        self.Name_label.setText(_translate("MainWindow", "Name*"))
        self.Age_label.setText(_translate("MainWindow", "Age*"))
        self.Weight_label.setText(_translate("MainWindow", "Weight(kgs)*"))
        self.Height_label.setText(_translate("MainWindow", "Height(Choose the Unit below)*"))
        self.Inches_button.setText(_translate("MainWindow", "Inches"))
        self.Cms_button.setText(_translate("MainWindow", "Metres"))
        self.Foot_button.setText(_translate("MainWindow", "Feet"))
        self.HbA1c_label.setText(_translate("MainWindow", "HbA1c* :-"))
        self.PPG_label.setText(_translate("MainWindow", "PPG* :-"))
        self.FPG_label.setText(_translate("MainWindow", " FPG* :- "))
        self.Q_label.setText(_translate("MainWindow", "Does the patient has any other cormobidities?*"))
        self.H_box.setText(_translate("MainWindow", "Hypertension"))
        self.D_box.setText(_translate("MainWindow", "Dislipedia"))
        self.C_box.setText(_translate("MainWindow", "Chronic kidney disease"))
        self.P_box.setText(_translate("MainWindow", "Pregnancy"))
        self.Noa_box.setText(_translate("MainWindow", "None of the Above"))
        self.Go_Button.setText(_translate("MainWindow", "Go"))
        self.menuMENU.setTitle(_translate("MainWindow", "MENU"))
        # self.actionNew.setText(_translate("MainWindow", "Home"))
        # self.actionData.setText(_translate("MainWindow", "Database"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogSignin = QtWidgets.QDialog()
    ui = Ui_DialogSignin()
    ui.setupUiSignIn(DialogSignin)
    DialogSignin.show()
    sys.exit(app.exec_())
