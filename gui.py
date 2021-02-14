from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle
import os
from doctor import Ui_DoctorWindow
from patient import Ui_PatientWindow
from pharma import Ui_PharmaWindow

class Ui_MainWindow(object):
    def doctorWindow(self):
        self.wind=QtWidgets.QMainWindow()
        self.ui= Ui_DoctorWindow()
        self.ui.setupUi(self.wind)
        self.wind.show()
    def pharmaWindow(self):
        self.wind=QtWidgets.QMainWindow()
        self.ui= Ui_PharmaWindow()
        self.ui.setupUi(self.wind)
        self.wind.show()
    def patientWindow(self):
        self.wind=QtWidgets.QMainWindow()
        self.ui= Ui_PatientWindow()
        self.ui.setupUi(self.wind)
        self.wind.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(321, 249)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 141, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 40, 141, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 130, 141, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 301, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 321, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Page"))
        self.pushButton.setText(_translate("MainWindow", "DOCTOR\n"
"LOGIN"))
        self.pushButton_2.setText(_translate("MainWindow", "PHARMACIST\n"
"LOGIN"))
        self.pushButton_3.setText(_translate("MainWindow", "PATIENT\n"
"LOGIN"))
        self.label.setText(_translate("MainWindow", "SMART HEALTHCARE MANAGEMENT SYSTEM"))
        self.pushButton.clicked.connect(self.doctorWindow)
        self.pushButton_2.clicked.connect(self.pharmaWindow)
        self.pushButton_3.clicked.connect(self.patientWindow)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('styling.css').read())
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())