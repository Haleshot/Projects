# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Attendance_System.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_bgWidget(object):
    def setupUi(self, bgWidget):
        if not bgWidget.objectName():
            bgWidget.setObjectName(u"bgWidget")
        bgWidget.resize(1200, 800)
        font = QFont()
        font.setPointSize(20)
        bgWidget.setFont(font)
        self.centralwidget = QWidget(bgWidget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Enter_ID = QTextEdit(self.centralwidget)
        self.Enter_ID.setObjectName(u"Enter_ID")
        self.Enter_ID.setGeometry(QRect(750, 180, 271, 61))
        self.Enter_ID.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.New_Registrations = QLabel(self.centralwidget)
        self.New_Registrations.setObjectName(u"New_Registrations")
        self.New_Registrations.setGeometry(QRect(750, 110, 261, 61))
        self.New_Registrations.setFont(font)
        self.New_Registrations.setAlignment(Qt.AlignCenter)
        self.Enter_Name = QTextEdit(self.centralwidget)
        self.Enter_Name.setObjectName(u"Enter_Name")
        self.Enter_Name.setGeometry(QRect(750, 360, 271, 61))
        self.Enter_Name.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.Generate_Images = QPushButton(self.centralwidget)
        self.Generate_Images.setObjectName(u"Generate_Images")
        self.Generate_Images.setGeometry(QRect(750, 480, 271, 71))
        font1 = QFont()
        font1.setPointSize(8)
        self.Generate_Images.setFont(font1)
        self.Generate_Images.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.Save_Profile = QPushButton(self.centralwidget)
        self.Save_Profile.setObjectName(u"Save_Profile")
        self.Save_Profile.setGeometry(QRect(750, 580, 271, 71))
        self.Save_Profile.setFont(font1)
        self.Save_Profile.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        self.Current_Users = QLabel(self.centralwidget)
        self.Current_Users.setObjectName(u"Current_Users")
        self.Current_Users.setGeometry(QRect(80, 10, 211, 61))
        self.Current_Users.setFont(font)
        self.Current_Users.setAlignment(Qt.AlignCenter)
        self.Attendance = QLabel(self.centralwidget)
        self.Attendance.setObjectName(u"Attendance")
        self.Attendance.setGeometry(QRect(40, 160, 191, 41))
        self.Quit_Button = QPushButton(self.centralwidget)
        self.Quit_Button.setObjectName(u"Quit_Button")
        self.Quit_Button.setGeometry(QRect(90, 580, 271, 71))
        self.Quit_Button.setStyleSheet(u"background-color: rgb(255, 0, 4);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.Register_Attendance = QPushButton(self.centralwidget)
        self.Register_Attendance.setObjectName(u"Register_Attendance")
        self.Register_Attendance.setGeometry(QRect(40, 80, 301, 61))
        self.Register_Attendance.setFont(font1)
        self.Register_Attendance.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        self.Error_Message = QLabel(self.centralwidget)
        self.Error_Message.setObjectName(u"Error_Message")
        self.Error_Message.setGeometry(QRect(390, 690, 471, 41))
        self.Error_Message.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Error_Message.setAlignment(Qt.AlignCenter)
        self.Attendance_Log = QTableWidget(self.centralwidget)
        if (self.Attendance_Log.columnCount() < 4):
            self.Attendance_Log.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.Attendance_Log.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Attendance_Log.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Attendance_Log.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Attendance_Log.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.Attendance_Log.setObjectName(u"Attendance_Log")
        self.Attendance_Log.setGeometry(QRect(40, 220, 611, 321))
        bgWidget.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(bgWidget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 51))
        bgWidget.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(bgWidget)
        self.statusbar.setObjectName(u"statusbar")
        bgWidget.setStatusBar(self.statusbar)

        self.retranslateUi(bgWidget)

        QMetaObject.connectSlotsByName(bgWidget)
    # setupUi

    def retranslateUi(self, bgWidget):
        bgWidget.setWindowTitle(QCoreApplication.translate("bgWidget", u"MainWindow", None))
        self.Enter_ID.setPlaceholderText(QCoreApplication.translate("bgWidget", u"Enter ID...", None))
        self.New_Registrations.setText(QCoreApplication.translate("bgWidget", u"New Registrations", None))
        self.Enter_Name.setPlaceholderText(QCoreApplication.translate("bgWidget", u"Enter Name...", None))
        self.Generate_Images.setText(QCoreApplication.translate("bgWidget", u"Generate Images", None))
        self.Save_Profile.setText(QCoreApplication.translate("bgWidget", u"Save Profile", None))
        self.Current_Users.setText(QCoreApplication.translate("bgWidget", u"Current Users", None))
        self.Attendance.setText(QCoreApplication.translate("bgWidget", u"Attendance :", None))
        self.Quit_Button.setText(QCoreApplication.translate("bgWidget", u"Quit", None))
        self.Register_Attendance.setText(QCoreApplication.translate("bgWidget", u"Register Attendance", None))
        self.Error_Message.setText("")
        ___qtablewidgetitem = self.Attendance_Log.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("bgWidget", u"ID", None));
        ___qtablewidgetitem1 = self.Attendance_Log.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("bgWidget", u"Name", None));
        ___qtablewidgetitem2 = self.Attendance_Log.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("bgWidget", u"Date", None));
        ___qtablewidgetitem3 = self.Attendance_Log.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("bgWidget", u"Time", None));
    # retranslateUi

