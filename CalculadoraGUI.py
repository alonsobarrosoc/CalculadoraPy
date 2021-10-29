# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalculadorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Calculadora

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 617)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 130, 75, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 130, 75, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 130, 75, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 210, 75, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 210, 75, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(320, 210, 75, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 300, 75, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(190, 300, 75, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(320, 300, 75, 51))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(190, 380, 75, 51))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(320, 380, 75, 51))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(460, 130, 75, 51))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(460, 210, 75, 51))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(460, 300, 75, 51))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(460, 380, 75, 51))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(590, 130, 75, 51))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(590, 210, 75, 51))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(590, 300, 75, 131))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(60, 380, 75, 51))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(460, 460, 75, 51))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(590, 460, 75, 51))
        self.pushButton_21.setObjectName("pushButton_21")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "7"))
        self.pushButton_2.setText(_translate("MainWindow", "8"))
        self.pushButton_3.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "1"))
        self.pushButton_8.setText(_translate("MainWindow", "2"))
        self.pushButton_9.setText(_translate("MainWindow", "3"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_11.setText(_translate("MainWindow", "."))
        self.pushButton_12.setText(_translate("MainWindow", "+"))
        self.pushButton_13.setText(_translate("MainWindow", "-"))
        self.pushButton_14.setText(_translate("MainWindow", "*"))
        self.pushButton_15.setText(_translate("MainWindow", "/"))
        self.pushButton_16.setText(_translate("MainWindow", "AC"))
        self.pushButton_17.setText(_translate("MainWindow", "DEL"))
        self.pushButton_18.setText(_translate("MainWindow", "="))
        self.pushButton_19.setText(_translate("MainWindow", "+/-"))
        self.pushButton_20.setText(_translate("MainWindow", "("))
        self.pushButton_21.setText(_translate("MainWindow", ")"))
        self.pushButton_7.clicked.connect(self.fn_1)
        self.pushButton_8.clicked.connect(self.fn_2)
        self.pushButton_9.clicked.connect(self.fn_3)
        self.pushButton_4.clicked.connect(self.fn_4)
        self.pushButton_5.clicked.connect(self.fn_5)
        self.pushButton_6.clicked.connect(self.fn_6)
        self.pushButton.clicked.connect(self.fn_7)
        self.pushButton_2.clicked.connect(self.fn_8)
        self.pushButton_3.clicked.connect(self.fn_9)
        self.pushButton_10.clicked.connect(self.fn_0)
        self.pushButton_11.clicked.connect(self.fn_punto)
        self.pushButton_19.clicked.connect(self.cambio_signo)
        self.pushButton_12.clicked.connect(self.operando_mas)
        self.pushButton_13.clicked.connect(self.operando_menos)
        self.pushButton_14.clicked.connect(self.operando_mult)
        self.pushButton_15.clicked.connect(self.operando_div)
        self.pushButton_16.clicked.connect(self.fn_ac)
        self.pushButton_17.clicked.connect(self.fn_del)
        self.pushButton_20.clicked.connect(self.fn_parIzq)
        self.pushButton_21.clicked.connect(self.fn_parDer)
        self.pushButton_18.clicked.connect(self.fn_igual)

        self.array = ['(']
        

    def fn_7(self): self.set_numero("7")
    def fn_8(self): self.set_numero("8")
    def fn_9(self): self.set_numero("9")
    def fn_4(self): self.set_numero("4")
    def fn_5(self): self.set_numero("5")
    def fn_6(self): self.set_numero("6")
    def fn_1(self): self.set_numero("1")
    def fn_2(self): self.set_numero("2")
    def fn_3(self): self.set_numero("3")
    def fn_0(self): self.set_numero("0")
    def fn_parIzq(self): self.agregar_par("(")
    def fn_parDer(self): self.agregar_par(")")
    
    def fn_igual(self):
        if self.label.text() != "":
            self.array.append(float(self.label.text()))
        self.array.append(")")
        print(self.array)
        arbol = Calculadora.arbol_jerarquico(self.array)
        if type(arbol).__name__ == "BinaryTree":
            post = Calculadora.recorrido_postorden(arbol.raiz)
            res = Calculadora.evalcion_postfija(post)
            
            if type(res).__name__ != 'bool':
                self.array = ['(' ]
                self.label.setText(str(res))

            else:
                self.label.setText("Error, presiona AC e intenta de nuevo")    
        else:
            self.label.setText("Error, presiona AC e intenta de nuevo")    
        
            
            
        print(self.array)
    
    
    def fn_punto(self): 
        t = self.label.text()
        if "." not in t:
            self.label.setText(t+".")
        
    
    def set_numero(self, n):
        t = self.label.text()
        
        self.label.setText(t+n)
        
    def cambio_signo(self):
        t = self.label.text()
        
        if len(t) == 0 or t[0] != '-':
            self.label.setText("-" + t)
        else:
            self.label.setText(t[1::])
    def operando_mas(self): self.agregar_a_array("+")
    def operando_menos(self): self.agregar_a_array("-")
    def operando_mult(self): self.agregar_a_array("*")
    def operando_div(self): self.agregar_a_array("/")
        
    def agregar_a_array(self, o):

        if self.label.text() != '':
            self.array.append(float(self.label.text()))
            self.array.append(o)
            self.label.setText("")
        print(self.array)
        
    
    def fn_ac(self):
        self.array = ['(']
        self.label.setText("")
    def fn_del(self):
        if self.label.text() != "":
            self.label.setText(self.label.text()[::-2])
    
    def agregar_par(self, p):
        self.array.append(float(self.label.text()))
        if p == "(" and (type(self.array[-1]).__name__ == 'float' or self.array[-1] == ")"):
            self.array.append('*')
        self.array.append(p)
        self.label.setText("")
        print(self.array)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
