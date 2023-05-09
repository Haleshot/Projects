# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LPF_Image_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import cv2
import numpy as np


class Ui_Dialog_5(object):
    def setupUi(self, Dialog_5):
        Dialog_5.setObjectName("Dialog_5")
        Dialog_5.resize(1366, 800)
        self.lineEdit = QtWidgets.QLineEdit(Dialog_5)
        self.lineEdit.setGeometry(QtCore.QRect(530, 620, 301, 81))
        self.lineEdit.setStyleSheet("border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 11.5pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(Dialog_5)
        self.label_5.setGeometry(QtCore.QRect(410, 730, 581, 41))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.Open_Image_Button = QtWidgets.QPushButton(Dialog_5)
        self.Open_Image_Button.setGeometry(QtCore.QRect(70, 620, 401, 81))
        self.Open_Image_Button.setObjectName("Open_Image_Button")
        self.label = QtWidgets.QLabel(Dialog_5)
        self.label.setGeometry(QtCore.QRect(10, 20, 571, 561))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog_5)
        self.label_4.setGeometry(QtCore.QRect(870, 640, 281, 41))
        self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Dialog_5)
        self.label_3.setGeometry(QtCore.QRect(590, 260, 61, 31))
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog_5)
        self.label_2.setGeometry(QtCore.QRect(690, 20, 571, 561))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog_5)
        QtCore.QMetaObject.connectSlotsByName(Dialog_5)

    def retranslateUi(self, Dialog_5):
        _translate = QtCore.QCoreApplication.translate
        Dialog_5.setWindowTitle(_translate("Dialog_5", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog_5", "Enter Mask Size..."))
        self.Open_Image_Button.setText(_translate("Dialog_5", "Open Image"))
        self.label_4.setText(_translate("Dialog_5", "Output Image"))
        self.label_3.setText(_translate("Dialog_5", "=>"))



        self.Open_Image_Button.clicked.connect(self.File_Select)


    def File_Select(self):
        Mask_Size = self.lineEdit.text() # Accessing the value entered by the user.
        
        if not (int(Mask_Size.isdigit())):
            self.label_5.setText("Please enter an integer value!")

        if not (int(Mask_Size) % 2 == 1):
            self.label_5.setText("Mask Size can only be odd!")
        else:
            self.label_5.setText("")
            # fname = QFileDialog.getOpenFileName(self, "Open File", "All_Project_Files\Final_Project_Files\Cam_Media", "Images (*.png *.xpm *.jpg)")
            # # Opening the Image
            # self.pixmap = QPixmap(fname[0]) # This returns a tuple and hence we mention [0].
            # # Adding the picture to the Label.
            # self.label.setPixmap(self.pixmap)
            Mask_Size = int(self.lineEdit.text())
            file_name, _ = QFileDialog.getOpenFileName(None, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif *.png)")
            self.label.setPixmap(QPixmap(file_name))
            img = cv2.imread(file_name, 0)
            m, n = img.shape
            print("The original size of the image is ", m, " x ", n)

            # Averaging/Low Pass Filtering without using the Formula:
            size_of_mask = Mask_Size
            LPF_Image = img.copy()
            m, n = img.shape
            print("You have requested for ", size_of_mask ,"x", size_of_mask)
            a = size_of_mask//2

            for i in range(a, m - a):
                for j in range(a, n - a):
                    temp = np.sum(img[i - a:i + a + 1, j - a:j + a + 1])
                    LPF_Image[i, j] = temp//size_of_mask**2

            
            m, n = LPF_Image.shape
            print("The new size of the image is ", m, " x ", n)

            
            cv2.imwrite(r"All_Project_Files\Final_Project_Files\Cam_Media\LPF_Img\LPF_Image.png", LPF_Image)
            LPF_Image_File_Name = r"All_Project_Files\Final_Project_Files\Cam_Media\LPF_Img\LPF_Image.png"
            self.label_2.setPixmap(QPixmap(LPF_Image_File_Name))


            # If you want these to display these in separate windows other than GUI.
            # cv2.imshow("Negative Image", negative_img)


            # cv2.imshow("Image", img)
            # cv2.waitKey(0)
    
            # # closing all open windows
            # cv2.destroyAllWindows()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_5 = QtWidgets.QDialog()
    ui = Ui_Dialog_5()
    ui.setupUi(Dialog_5)
    Dialog_5.show()
    sys.exit(app.exec_())
