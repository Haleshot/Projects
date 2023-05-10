# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Laplace_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
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


class Ui_Dialog_8(object):
    def setupUi(self, Dialog_8):
        Dialog_8.setObjectName("Dialog_8")
        Dialog_8.resize(1366, 800)
        self.Open_Image_Button = QtWidgets.QPushButton(Dialog_8)
        self.Open_Image_Button.setGeometry(QtCore.QRect(70, 620, 401, 81))
        self.Open_Image_Button.setObjectName("Open_Image_Button")
        self.label_2 = QtWidgets.QLabel(Dialog_8)
        self.label_2.setGeometry(QtCore.QRect(690, 20, 571, 561))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog_8)
        self.label_3.setGeometry(QtCore.QRect(610, 330, 61, 31))
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog_8)
        self.label_4.setGeometry(QtCore.QRect(870, 640, 281, 41))
        self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Dialog_8)
        self.label.setGeometry(QtCore.QRect(10, 20, 571, 561))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Dialog_8)
        self.label_5.setGeometry(QtCore.QRect(410, 730, 581, 41))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog_8)
        QtCore.QMetaObject.connectSlotsByName(Dialog_8)

    def retranslateUi(self, Dialog_8):
        _translate = QtCore.QCoreApplication.translate
        Dialog_8.setWindowTitle(_translate("Dialog_8", "Dialog"))
        self.Open_Image_Button.setText(_translate("Dialog_8", "Open Image"))
        self.label_3.setText(_translate("Dialog_8", "=>"))
        self.label_4.setText(_translate("Dialog_8", "Output Image"))


        self.Open_Image_Button.clicked.connect(self.File_Select)


    def laplacian_filter(self, img, kernel_size=3):
        # Define the Laplacian kernel
        kernel = np.array([
            [0, 1, 0],
            [1, -4, 1],
            [0, 1, 0]
        ], dtype=np.float32)
        
        # Pad the image with zeros
        padded_img = np.pad(img, pad_width=kernel_size//2, mode='constant')
        
        # Apply the Laplacian filter to the image
        filtered_img = np.zeros_like(img, dtype=np.float32)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                filtered_img[i, j] = np.sum(padded_img[i:i+kernel_size, j:j+kernel_size] * kernel)
        
        # Normalize the filtered image to the range [0, 255]
        filtered_img = cv2.normalize(filtered_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        
        return filtered_img


    def File_Select(self):
        file_name, _ = QFileDialog.getOpenFileName(None, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif *.png)")
        self.label.setPixmap(QPixmap(file_name))
        img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

        # Apply the Laplacian filter to the image
        filtered_img = self.laplacian_filter(img)

        cv2.imwrite(r"Image_Processing\All_Project_Files\Final_Project_Files\Cam_Media\Laplacian_Images\Laplacian_Image.png", filtered_img)
        Laplacian_File_Name = r"Image_Processing\All_Project_Files\Final_Project_Files\Cam_Media\Laplacian_Images\Laplacian_Image.png"
        self.label_2.setPixmap(QPixmap(Laplacian_File_Name))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_8 = QtWidgets.QDialog()
    ui = Ui_Dialog_8()
    ui.setupUi(Dialog_8)
    Dialog_8.show()
    sys.exit(app.exec_())
