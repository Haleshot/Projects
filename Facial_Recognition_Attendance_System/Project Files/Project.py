# IS-1 Project.

import sys


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

import cv2


class Welcome_screen(QWidget):
    def __init__(self):
        super(Welcome_screen, self).__init__()

        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.Stop_BTN = QPushButton("Stop")
        self.Stop_BTN.clicked.connect(self.Stop_Camera)
        self.VBL.addWidget(self.Stop_BTN)

        self.Processing = Processing()

        self.Processing.start()
        self.Processing.ImageUpdate.connect(self.Frame_Update)
        self.setLayout(self.VBL)

    def Frame_Update(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def Stop_Camera(self):
        self.Processing.stop()

class Processing(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
                
    def stop(self):
        self.ThreadActive = False
        self.quit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    welcome = Welcome_screen()
    welcome.show()
    sys.exit(App.exec())