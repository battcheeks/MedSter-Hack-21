# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pharma.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PharmaWindow(object):
    def setupUi(self, PharmaWindow):
        PharmaWindow.setObjectName("PharmaWindow")
        PharmaWindow.resize(410, 81)
        self.centralwidget = QtWidgets.QWidget(PharmaWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 10, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 10, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        PharmaWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PharmaWindow)
        self.statusbar.setObjectName("statusbar")
        PharmaWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PharmaWindow)
        QtCore.QMetaObject.connectSlotsByName(PharmaWindow)

    def retranslateUi(self, PharmaWindow):
        _translate = QtCore.QCoreApplication.translate
        PharmaWindow.setWindowTitle(_translate("PharmaWindow", "MainWindow"))
        self.pushButton.setText(_translate("PharmaWindow", "Pharmacist\n"
"Login"))
        self.pushButton_2.setText(_translate("PharmaWindow", "Pharmacist\n"
"Sign-up"))
        self.pushButton_3.setText(_translate("PharmaWindow", "Export Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PharmaWindow = QtWidgets.QMainWindow()
    ui = Ui_PharmaWindow()
    ui.setupUi(PharmaWindow)
    PharmaWindow.show()
    sys.exit(app.exec_())