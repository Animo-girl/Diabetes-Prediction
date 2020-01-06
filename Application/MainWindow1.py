
from PyQt5 import QtCore, QtGui, QtWidgets
from LP import *
import pandas as pd 
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

class Ui_MainWindow(object):
    def call2(self):
        if __name__ == '__main__':
            self.Name_box_text = self.Name_box.text()
            self.Age_box_text = self.Age_box.value()
            self.Weight_box_text = self.Weight_box.value()
            self.Height_box_text = self.Height_box.value()
            self.PPG_box_text = self.PPG_box.value()
            self.FPG_box_text = self.FPG_box.value()
            self.HbA1c_box_text = self.HbA1c_box.value()
            self.winn = QtWidgets.QMainWindow()
            self.obj_n = Ui_LastPage()
            self.obj_n.setup(self.winn)
            self.winn.show()            
            self.a = self.Age(self.Age_box_text)
            self.listo = self.cormobidities()
            self.hei = self.height_entered(self.Height_box_text)
            self.Bmi = self.BMI(self.hei,self.Weight_box_text)
            self.b = self.BMI_check(self.Bmi)
            
            self.np1 = [self.a,self.b,self.HbA1c_box_text,self.FPG_box_text,self.PPG_box_text,self.listo]
            
            
            
            dataframe = pd.read_excel("Preprocessed_data.xlsx")
            
            dat = [dataframe['Age '],dataframe['BMI'],dataframe['Hba1c'],
                   dataframe['FPG'],dataframe['PPG'],dataframe['HTN'],
                   dataframe['DYLP'],dataframe['CKD'],dataframe['Pregn']
                   ]
            X = np.asarray(dat).transpose()
            y = np.asarray(dataframe['Duration lasting till'])
            m = self.np1.pop(-1)
            self.np1 = self.np1 + m
            self.np1 = np.asarray(self.np1)
            self.np1 = self.np1.reshape(1,-1)        
            
            tree = DecisionTreeClassifier()
            bag = BaggingClassifier(tree, n_estimators=100, max_samples=0.8,
            random_state=1)
            bag.fit(X, y)
            
            y_predrf = bag.predict(self.np1)
            if y_predrf[0] == 0:
                out = "You don't require a long term treatment,just follow the following...."
            elif y_predrf[0] == 1:
                out = "The Duration for the treatment would be 6 months to 3 years depending on your health"
            elif y_predrf[0] == 2:
                out = "The Duration for the treatment would be 3-10 years"
            elif y_predrf[0] == 3:
                out = "The Duration for the treatment would be 11-20 years or more than that"
            
            y_treatment = np.asarray(dataframe['Diabetes treatment'])
    
            classifiersk = DecisionTreeClassifier()
            classifiersk.fit(X,y_treatment)
    
            y_predPres = classifiersk.predict(self.np1)
            for i in y_predPres:
                break
            bmi_out = str(self.Bmi)
            out = "Your BMI is " + bmi_out + "\n" + out + "\nYou will have to follow the following\n" + i
            self.obj_n.O_label.setText(out)
             
        
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
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 722)
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
"background-color: rgb(85, 255, 127);\n"
"border-color: rgb(0, 191, 92);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Name_label.setObjectName("Name_label")
        self.gridLayout_2.addWidget(self.Name_label, 0, 0, 1, 1)
        self.Name_box = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.Name_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0, 191, 92);\n"
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
"background-color: rgb(85, 255, 127);\n"
"border-color: rgb(0, 191, 92);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Age_label.setObjectName("Age_label")
        self.horizontalLayout_3.addWidget(self.Age_label)
        self.Age_box = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.Age_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0, 191, 92);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"\n"
"")
        self.Age_box.setObjectName("Age_box")
        self.horizontalLayout_3.addWidget(self.Age_box)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(20, 10, 10, 10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Weight_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Weight_label.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(85, 255, 127);\n"
"border-color: rgb(0, 191, 92);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Weight_label.setObjectName("Weight_label")
        self.horizontalLayout_7.addWidget(self.Weight_label)
        self.Weight_box = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.Weight_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0, 191, 92);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"\n"
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
"background-color: rgb(85, 255, 127);\n"
"border-color: rgb(0, 191, 92);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Height_label.setObjectName("Height_label")
        self.horizontalLayout_5.addWidget(self.Height_label)
        self.Height_box = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.Height_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0, 191, 92);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"\n"
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
"border-color: rgb(0, 191, 92);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Inches_button.setObjectName("Inches_button")
        self.horizontalLayout.addWidget(self.Inches_button)
        self.Cms_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Cms_button.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0, 191, 92);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Cms_button.setObjectName("Cms_button")
        self.horizontalLayout.addWidget(self.Cms_button)
        self.Foot_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Foot_button.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0, 191, 92);\n"
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
"border-bottom-color: rgb(0, 170, 127);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);\n"
"")
        self.HbA1c_label.setObjectName("HbA1c_label")
        self.gridLayout_3.addWidget(self.HbA1c_label, 0, 2, 1, 1)
        self.PPG_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.PPG_label.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-bottom-color: rgb(0, 170, 127);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);")
        self.PPG_label.setObjectName("PPG_label")
        self.gridLayout_3.addWidget(self.PPG_label, 0, 1, 1, 1)
        self.FPG_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.FPG_label.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-bottom-color: rgb(0, 170, 127);\n"
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
"border-color: rgb(0, 191, 92);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"\n"
"")
        self.FPG_box.setMaximum(1000)
        self.FPG_box.setObjectName("FPG_box")
        self.horizontalLayout_6.addWidget(self.FPG_box)
        self.PPG_box = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.PPG_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0, 191, 92);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"\n"
"")
        self.PPG_box.setMaximum(1000)
        self.PPG_box.setObjectName("PPG_box")
        self.horizontalLayout_6.addWidget(self.PPG_box)
        self.HbA1c_box = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.HbA1c_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0, 191, 92);\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-radius:20px;\n"
"\n"
"")
        self.HbA1c_box.setMaximum(1999.99)
        self.HbA1c_box.setObjectName("HbA1c_box")
        self.horizontalLayout_6.addWidget(self.HbA1c_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_6.setSpacing(10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Q_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q_label.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"border-color: rgb(0, 191, 92);\n"
"border-style:solid;\n"
"border-width:10px;\n"
"border-radius:20px;\n"
"")
        self.Q_label.setObjectName("Q_label")
        self.gridLayout_6.addWidget(self.Q_label, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(10, 10, 10, 20)
        self.gridLayout_5.setHorizontalSpacing(20)
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.H_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.H_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(85, 255, 127);")
        self.H_box.setObjectName("H_box")
        self.horizontalLayout_2.addWidget(self.H_box)
        self.D_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.D_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(85, 255, 127);")
        self.D_box.setObjectName("D_box")
        self.horizontalLayout_2.addWidget(self.D_box)
        self.C_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.C_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(85, 255, 127);")
        self.C_box.setObjectName("C_box")
        self.horizontalLayout_2.addWidget(self.C_box)
        self.P_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.P_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(85, 255, 127);")
        self.P_box.setObjectName("P_box")
        self.horizontalLayout_2.addWidget(self.P_box)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.Noa_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Noa_box.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(85, 255, 127);")
        self.Noa_box.setObjectName("Noa_box")
        self.gridLayout_5.addWidget(self.Noa_box, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.Go_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Go_Button.setStyleSheet("#Go_Button{\n"
"    font: 14pt \"MS Reference Sans Serif\";\n"
"\n"
"background-color: rgb(85, 255, 127);\n"
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
        self.Go_Button.clicked.connect(self.call2)
        self.horizontalLayout_4.addWidget(self.Go_Button)
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
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionData = QtWidgets.QAction(MainWindow)
        self.actionData.setObjectName("actionData")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuMENU.addAction(self.actionNew)
        self.menuMENU.addSeparator()
        self.menuMENU.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMENU.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "D's"))
        self.Name_label.setText(_translate("MainWindow", "Name"))
        self.Age_label.setText(_translate("MainWindow", "Age"))
        self.Weight_label.setText(_translate("MainWindow", "Weight(kgs)"))
        self.Height_label.setText(_translate("MainWindow", "Height(Choose the Unit below)"))
        self.Inches_button.setText(_translate("MainWindow", "Inches"))
        self.Cms_button.setText(_translate("MainWindow", "Centimetres"))
        self.Foot_button.setText(_translate("MainWindow", "Foot"))
        self.HbA1c_label.setText(_translate("MainWindow", "HbA1c :-"))
        self.PPG_label.setText(_translate("MainWindow", "PPG :-"))
        self.FPG_label.setText(_translate("MainWindow", " FPG :- "))
        self.Q_label.setText(_translate("MainWindow", "Does the patient has any other cormobidities?"))
        self.H_box.setText(_translate("MainWindow", "Hypertension"))
        self.D_box.setText(_translate("MainWindow", "Dislipedia"))
        self.C_box.setText(_translate("MainWindow", "Chronic kidney disease"))
        self.P_box.setText(_translate("MainWindow", "Pregnancy"))
        self.Noa_box.setText(_translate("MainWindow", "None of the Above"))
        self.Go_Button.setText(_translate("MainWindow", "Go"))
        self.menuMENU.setTitle(_translate("MainWindow", "MENU"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionData.setText(_translate("MainWindow", "Database"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

