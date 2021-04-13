# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

#GUI of Student info

class Ui_add_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 437)
        MainWindow.setStyleSheet("background-color: rgb(230, 226, 221);\n"
"font: 8pt \"Lato\";")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 461, 331))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("font: 87 12pt \"Lato Black\";")

        # GroupBox where we will display camera
        self.groupBox_2.setObjectName("groupBox_2")
        self.display_camera = QtWidgets.QLabel(self.groupBox_2)
        self.display_camera.setGeometry(QtCore.QRect(10, 20, 441, 301))
        self.display_camera.setText("")
        self.display_camera.setObjectName("display_camera")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 340, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("font: 87 12pt \"Lato Black\";")

        #GroupBox3 contain lineEdit and two push buttons
        self.groupBox_3.setObjectName("groupBox_3")
        self.addstudent = QtWidgets.QLineEdit(self.groupBox_3)
        self.addstudent.setGeometry(QtCore.QRect(10, 20, 251, 21))
        self.addstudent.setStyleSheet("font: 10pt \"Lato\";")
        self.addstudent.setInputMask("")
        self.addstudent.setText("")

        #LineEdit to enter the name of student
        self.addstudent.setObjectName("addstudent")
        self.start_camera = QtWidgets.QPushButton(self.centralwidget)
        self.start_camera.setGeometry(QtCore.QRect(290, 350, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.start_camera.setFont(font)
        self.start_camera.setStyleSheet("background-color: rgb(164, 151, 142);\n"
"font: 87 10pt \"Lato Black\";")

        #Start_Camera push_Button to start camera
        self.start_camera.setObjectName("start_camera")
        self.take_picture = QtWidgets.QPushButton(self.centralwidget)
        self.take_picture.setGeometry(QtCore.QRect(390, 350, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.take_picture.setFont(font)
        self.take_picture.setStyleSheet("background-color: rgb(164, 151, 142);\n"
"font: 87 10pt \"Lato Black\";")

        # Take Picture push_Button to take a picture of new student
        self.take_picture.setObjectName("take_picture")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(490, 0, 261, 401))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("\n"
"font: 87 12pt \"Lato Black\";")



        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 360, 241, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(164, 151, 142);\n"
"font: 87 10pt \"Lato Black\";")

        #Name push button to search by name
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.date = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.date.setFont(font)
        self.date.setStyleSheet("background-color: rgb(164, 151, 142);\n"
"font: 87 10pt \"Lato Black\";\n"
"")
        # Date push button to search by date attendance students
        self.date.setObjectName("date")
        self.horizontalLayout.addWidget(self.date)
        self.date_or_name = QtWidgets.QLineEdit(self.groupBox)
        self.date_or_name.setGeometry(QtCore.QRect(10, 320, 241, 31))
        self.date_or_name.setStyleSheet("font: 10pt \"Lato\";")
        self.date_or_name.setInputMask("")
        self.date_or_name.setText("")

        #LineEdit Where we write the name or Date
        self.date_or_name.setObjectName("date_or_name")
        self.room_textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.room_textEdit.setGeometry(QtCore.QRect(10, 20, 241, 291))
        self.room_textEdit.setStyleSheet("font: 10pt \"Lato\";")

        # Room Text Edit where we will get the answer
        self.room_textEdit.setObjectName("room_textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Information"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Display Camera"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Student name"))
        self.start_camera.setText(_translate("MainWindow", "Start Camera"))
        self.take_picture.setText(_translate("MainWindow", "Take picture"))
        self.groupBox.setTitle(_translate("MainWindow", "Student Information"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.date.setText(_translate("MainWindow", "Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_add_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
