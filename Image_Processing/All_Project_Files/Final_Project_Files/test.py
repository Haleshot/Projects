# # importing the required module  
# import sys  
  
# # importing the necessary classes for the project  
# from PyQt5.QtCore import Qt, QSize  
# from PyQt5.QtWidgets import QApplication, QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, qApp, QFileDialog, QToolBar, QMenuBar  
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter, QIcon, QKeySequence  
# from PyQt5.QtPrintSupport import QPrintDialog, QPrinter  
  
# # defining the child class of the QMainWindow class  
# class QImageViewer(QMainWindow):  
#     # defining the initializing function  
#     def __init__(self):  
#         super().__init__()  
#                 # creating an object of the QPrinter class  
#         self.printerObj = QPrinter()  
#         # setting the initial scaling factor  
#         self.scale_factor = 0.0  
  
#         # creating an object of the QLabel class to display the label  
#         self.image_label = QLabel()  
#         # setting the background color of the label to display the image using the setBackgroundRole() method and QPalette class  
#         self.image_label.setBackgroundRole(QPalette.Base)  
#         # setting the size policy of the label using the setSizePolicy() method and QSizePolicy class  
#         self.image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)  
#         # setting the setScaledContents() method to True  
#         # to manually adjust the aspect ratio of the image  
#         # in the application  
#         self.image_label.setScaledContents(True)  
  
#         # creating an object of the QScrollArea class to display the scroll bar  
#         self.scroll_area = QScrollArea()  
#         # setting the background color of the scroll bar to display the image using the setBackgroundRole() method and QPalette class  
#         self.scroll_area.setBackgroundRole(QPalette.Dark)  
#         # setting the scrolling area to the image label using the setWidget() method  
#         self.scroll_area.setWidget(self.image_label)  
#         # setting the visibility of the scrolling area with the help of the setVisible() method  
#         self.scroll_area.setVisible(False)  
  
#         # setting the central widget to the scroll area using the setCentral Widget() method  
#         self.setCentralWidget(self.scroll_area)  
  
#         # configuring the title of the window  
#         self.setWindowTitle("Image Viewer - JAVATPOINT")  
#         # configuring the width and height of the window  
#         self.window_width, self.window_height = self.geometry().width(), self.geometry().height()  
#         # setting the Icon of the window  
#         self.setWindowIcon(QIcon('./icons/imageViewer.ico'))  
#         # using the resize() to set the size of the application  
#         self.resize(self.window_width * 2, self.window_height * 2)  
  
#         #--------------------------------------  
#         # Creating a File Menu  
#         #--------------------------------------  
#         self.filemenu = self.menuBar().addMenu('&File')  
          
#         #--------------------------------------  
#         # Creating a File Toolbar  
#         #--------------------------------------  
#         self.filetoolbar = QToolBar('File')  
#         self.filetoolbar.setIconSize(QSize(30, 30))  
#         self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.filetoolbar)  
  
#         # creating the menu options like open, save, save as, and print  
  
#         # calling the user-defined makeAction() method to create the action to open the file...  
#         self.open_doc_opt = self.makeAction(self, './icons/openImage.ico', 'Open Image...', 'Open Image...', self.openImage)  
#         # using the setShortcut() method to set a shortcut to execute the 'Open' command  
#         self.open_doc_opt.setShortcut(QKeySequence.Open)  
  
#         # calling the user-defined makeAction() method to create the action to print the file  
#         self.print_opt = self.makeAction(self, './icons/printer.ico', 'Print', 'Print', self.printImage)  
#         # using the setShortcut() method to set a shortcut to execute the 'Print' command  
#         self.print_opt.setShortcut(QKeySequence.Print)  
#         # initially disabling the action by setting the value of setEnabled() method to False  
#         self.print_opt.setEnabled(False)  
  
#         # using the addActions() method to add all the created actions to the 'File' menu and toolbar  
#         self.filemenu.addActions([self.open_doc_opt, self.print_opt])  
#         self.filetoolbar.addActions([self.open_doc_opt, self.print_opt])  
  
#         # adding the separator  
#         self.filemenu.addSeparator()  
  
#         # calling the user-defined makeAction() method to create the action to close the application  
#         self.exit_opt = self.makeAction(self, '', 'Exit', 'Exit', self.close)  
#         # using the setShortcut() method to set a shortcut to execute the 'Close' command  
#         self.print_opt.setShortcut(QKeySequence.Close)  
  
#         # using the addActions() method to add all the created actions to the 'File' menu and toolbar  
#         self.filemenu.addActions([self.exit_opt])  
  
#         #--------------------------------------  
#         # Creating a View Menu  
#         #--------------------------------------  
#         self.viewmenu = self.menuBar().addMenu('&View')  
          
#         #--------------------------------------  
#         # Creating an View Tool bar  
#         #--------------------------------------  
#         self.viewtoolbar = QToolBar('Edit')  
#         self.viewtoolbar.setIconSize(QSize(30, 30))  
#         self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.viewtoolbar)  
  
#         # calling the user-defined makeAction() method to create the action to zoom in the image  
#         self.zoomIN_opt = self.makeAction(self, './icons/zoomIn.ico', 'Zoom In (25%)', 'Zoom In (25%)', self.zoom_in)  
#         # using the setShortcut() method to set a shortcut to execute the 'Zoom In' command  
#         self.zoomIN_opt.setShortcut(QKeySequence.ZoomIn)  
#         # initially disabling the action by setting the value of setEnabled() method to False  
#         self.zoomIN_opt.setEnabled(False)  
          
#         # calling the user-defined makeAction() method to create the action to zoom out the image  
#         self.zoomOUT_opt = self.makeAction(self, './icons/zoomOut.ico', 'Zoom Out (25%)', 'Zoom Out (25%)', self.zoom_out)  
#         # using the setShortcut() method to set a shortcut to execute the 'Zoom Out' command  
#         self.zoomOUT_opt.setShortcut(QKeySequence.ZoomOut)  
#         # initially disabling the action by setting the value of setEnabled() method to False  
#         self.zoomOUT_opt.setEnabled(False)  
  
#         # calling the user-defined makeAction() method to create the action to set the normal size of the image  
#         self.normalSize_opt = self.makeAction(self, '', 'Normal Size', 'Normal Size', self.normal_size)  
#         # using the setShortcut() method to set a shortcut to execute the 'Normal Size' command  
#         self.normalSize_opt.setShortcut(QKeySequence("Ctrl+S"))  
#         # initially disabling the action by setting the value of setEnabled() method to False  
#         self.normalSize_opt.setEnabled(False)  
#         # setting the initial value of the setCheckable() method to True  
#         self.normalSize_opt.setCheckable(True)  
  
#         # using the addActions() method to add all the created actions to the 'View' menu and toolbar  
#         self.viewmenu.addActions([self.zoomIN_opt, self.zoomOUT_opt, self.normalSize_opt])  
#         self.viewtoolbar.addActions([self.zoomIN_opt, self.zoomOUT_opt])  
  
#         # adding the separator  
#         self.viewmenu.addSeparator()  
#         self.viewtoolbar.addSeparator()  
  
#         # calling the user-defined makeAction() method to create the action to set the image to window size  
#         self.fitToWindow_opt = self.makeAction(self, './icons/fitToWindow.ico', 'Fit To Window', 'Fit To Window', self.fit_to_window)  
#         # using the setShortcut() method to set a shortcut to execute the 'Fit to Window' command  
#         self.fitToWindow_opt.setShortcut(QKeySequence("Ctrl+F"))  
#         # initially disabling the action by setting the value of setEnabled() method to False  
#         self.fitToWindow_opt.setEnabled(False)  
  
#         # using the addActions() method to add all the created actions to the 'View' menu and toolbar  
#         self.viewmenu.addActions([self.fitToWindow_opt])  
#         self.viewtoolbar.addActions([self.fitToWindow_opt])  

  
#     # defining the required methods of the class  
  
#     # defining the method to open the image file   
#     def openImage(self):  
#         # creating an object of the QFileDialog.Options class  
#         selections = QFileDialog.Options()  
#         # calling the getOpenFileName() method to browse the image from the directory  
#         file_name, _ = QFileDialog.getOpenFileName(  
#             self,  
#             'QFileDialog.getOpenFileName()',  
#             '',  
#             'Images (*.png *.jpeg *.jpg *.bmp *.gif)',  
#             options = selections  
#             )  
#         # if the file name is not an empty string  
#         if file_name:  
#             # creating an object of the QImage class by passing the file name as its parameter  
#             image = QImage(file_name)  
#             # if the image file is empty, returning the message box displaying information  
#             if image.isNull():  
#                 QMessageBox.information(self, "Image Viewer", "Cannot load %s." % file_name)  
#                 return  
  
#             # using the setPixmap() method to create the off-screen image representation that can be used as a paint device  
#             self.image_label.setPixmap(QPixmap.fromImage(image))  
#             # setting the scale factor to 1.0  
#             self.scale_factor = 1.0  
  
#             # enabling the visibility of the scroll area  
#             self.scroll_area.setVisible(True)  
#             # enabling the "Print" action  
#             self.print_opt.setEnabled(True)  
#             # calling the fit_to_window() method  
#             self.fit_to_window()  
#             # enabling the "Fit To Window" action  
#             self.fitToWindow_opt.setEnabled(True)  
#             # calling the update_actions() method  
#             self.update_actions()  
  
#             # if the "Fit To Window" action is not checked  
#             if not self.fitToWindow_opt.isChecked():  
#                 # calling the adjustSize() method to adjust the size of the image  
#                 self.image_label.adjustSize()  
  
#     # defining the method to print the image  
#     def printImage(self):  
#         # creating an object of the QPrintDialog class  
#         print_dialog = QPrintDialog(self.printerObj, self)  
#         # if the print action is executed  
#         if print_dialog.exec_():  
#             # creating an object of the QPainter class by passing the object of the QPrinter class  
#             the_painter = QPainter(self.printerObj)  
#             # creating a rectangle to place the image  
#             rectangle = the_painter.viewport()  
#             # defining the size of the image  
#             the_size = self.image_label.pixmap().size()  
#             # scaling the image to the Aspect Ratio  
#             the_size.scale(rectangle.size(), Qt.KeepAspectRatio)  
#             # setting the view port of the image by calling the setViewport() method  
#             the_painter.setViewport(rectangle.x(), rectangle.y(), the_size.width(), the_size.height())  
#             # calling the setWindow() method  
#             the_painter.setWindow(self.image_label.pixmap().rect())  
#             # calling the drawPixmap() method  
#             the_painter.drawPixmap(0, 0, self.image_label.pixmap())  
  
#     # defining the method to zoom in on the image  
#     def zoom_in(self):  
#         # calling the user-defined scale_image() method passing 1.25 as the scaling factor  
#         self.scale_image(1.25)  
  
#     # defining the method to zoom out of the image  
#     def zoom_out(self):  
#         # calling the user-defined scale_image() method passing 0.8 as the scaling factor  
#         self.scale_image(0.8)  
  
#     # defining the method to set the normal size of the image  
#     def normal_size(self):  
#         # calling the adjustSize() method to adjust the size of the image  
#         self.image_label.adjustSize()  
#         # calling the user-defined scale_image() method passing 1.0 as the scaling factor  
#         self.scale_factor = 1.0  
  
#     # defining the method to set the size of the image fitting to the window  
#     def fit_to_window(self):  
#         # retrieving the Boolean value from the "Fit To Window" action  
#         fitToWindow = self.fitToWindow_opt.isChecked()  
#         # configuring the scroll area to resizable  
#         self.scroll_area.setWidgetResizable(fitToWindow)  
#         # if the retrieved value is False, calling the user-defined normal_size() method   
#         if not fitToWindow:  
#             self.normal_size()  
#         # calling the user-defined update_actions() method  
#         self.update_actions()  
  
#     # defining the method to update the actions  
#     def update_actions(self):  
#         # enabling the "Zoom In", "Zoom Out", and "Normal Size" actions,  
#         # if the "Fit To Window" is unchecked  
#         self.zoomIN_opt.setEnabled(not self.fitToWindow_opt.isChecked())  
#         self.zoomOUT_opt.setEnabled(not self.fitToWindow_opt.isChecked())  
#         self.normalSize_opt.setEnabled(not self.fitToWindow_opt.isChecked())  
  
#     # defining the method to scale the image  
#     def scale_image(self, sf):  
#         # defining the scaling factor of the image  
#         self.scale_factor *= sf  
#         # using the resize() method to resize the image as per the scaling factor  
#         self.image_label.resize(self.scale_factor * self.image_label.pixmap().size())  
  
#         # calling the user-defined adjust_scroll_bar() method to adjust the scrollbar as per the scaling factor  
#         self.adjust_scroll_bar(self.scroll_area.horizontalScrollBar(), sf)  
#         self.adjust_scroll_bar(self.scroll_area.verticalScrollBar(), sf)  
  
#         # toggling the "Zoom In" and "Zoom Out" actions as per the scaling factor   
#         self.zoomIN_opt.setEnabled(self.scale_factor < 3.0)  
#         self.zoomOUT_opt.setEnabled(self.scale_factor > 0.333)  
  
#     # defining the method to adjust the scroll bar  
#     def adjust_scroll_bar(self, scroll_bar, scaleFactor):  
#         # using the setValue() method to adjust length of the scrollbar according to the scaling factor  
#         scroll_bar.setValue(int(scaleFactor * scroll_bar.value() + ((scaleFactor - 1) * scroll_bar.pageStep() / 2)))  
  
#     # defining the method to create the actions of the menu and toolbar  
#     def makeAction(self, parent_obj, icon_destination, name_of_action, status_tip, triggered_method):  
#         # creating an object of the QAction() class  
#         act = QAction(QIcon(icon_destination), name_of_action, parent_obj)  
#         # updating the message in the status bar  
#         act.setStatusTip(status_tip)  
#         # calling the different functions designated to different actions  
#         act.triggered.connect(triggered_method)  
#         # returning the action  
#         return act  
  
# # main function  
# if __name__ == '__main__':  
  
#     # creating an object of the QApplication class  
#     the_app = QApplication(sys.argv)  
      
#     # creating an object of the Application class  
#     imageViewerApp = QImageViewer()  
  
#     # using the show() method to display the window  
#     imageViewerApp.show()  
  
#     # using the exit() function of the sys module to close the application  
#     sys.exit(the_app.exec_())





























from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog, QWidget, QHBoxLayout


class QImageViewSync(QWidget):
    def __init__(self, window=None):
        super().__init__()

        self.window = window
        self.printer = QPrinter()
        self.scaleFactor = 0.0

        self.imageLabelLeft = QLabel()
        self.imageLabelLeft.setBackgroundRole(QPalette.Base)
        self.imageLabelLeft.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabelLeft.setScaledContents(True)

        self.scrollAreaLeft = QScrollArea()
        self.scrollAreaLeft.setBackgroundRole(QPalette.Dark)
        self.scrollAreaLeft.setWidget(self.imageLabelLeft)
        self.scrollAreaLeft.setVisible(False)

        self.imageLabelRight = QLabel()
        self.imageLabelRight.setBackgroundRole(QPalette.Base)
        self.imageLabelRight.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabelRight.setScaledContents(True)

        self.scrollAreaRight = QScrollArea()
        self.scrollAreaRight.setBackgroundRole(QPalette.Dark)
        self.scrollAreaRight.setWidget(self.imageLabelRight)
        self.scrollAreaRight.setVisible(False)

        self.centralWidget = QWidget()
        self.layout = QHBoxLayout(self.centralWidget)
        self.layout.addWidget(self.scrollAreaLeft)
        self.layout.addWidget(self.scrollAreaRight)

        self.scrollAreaLeft.verticalScrollBar().valueChanged.connect(
            self.scrollAreaRight.verticalScrollBar().setValue)
        self.scrollAreaLeft.horizontalScrollBar().valueChanged.connect(
            self.scrollAreaRight.horizontalScrollBar().setValue)
        self.scrollAreaRight.verticalScrollBar().valueChanged.connect(
            self.scrollAreaLeft.verticalScrollBar().setValue)
        self.scrollAreaRight.horizontalScrollBar().valueChanged.connect(
            self.scrollAreaLeft.horizontalScrollBar().setValue)

        self.scrollAreaLeft.mouseMoveEvent = self.mouseMoveEventLeft
        self.scrollAreaLeft.mousePressEvent = self.mousePressEventLeft
        self.scrollAreaLeft.mouseReleaseEvent = self.mouseReleaseEventLeft

        self.scrollAreaRight.mouseMoveEvent = self.mouseMoveEventRight
        self.scrollAreaRight.mousePressEvent = self.mousePressEventRight
        self.scrollAreaRight.mouseReleaseEvent = self.mouseReleaseEventRight

        self.imageLabelLeft.setCursor(Qt.OpenHandCursor)
        self.imageLabelRight.setCursor(Qt.OpenHandCursor)

    def mousePressEventLeft(self, event):
        self.pressed = True
        self.imageLabelLeft.setCursor(Qt.ClosedHandCursor)
        self.initialPosX = self.scrollAreaLeft.horizontalScrollBar().value() + event.pos().x()
        self.initialPosY = self.scrollAreaLeft.verticalScrollBar().value() + event.pos().y()

    def mouseReleaseEventLeft(self, event):
        self.pressed = False
        self.imageLabelLeft.setCursor(Qt.OpenHandCursor)
        self.initialPosX = self.scrollAreaLeft.horizontalScrollBar().value()
        self.initialPosY = self.scrollAreaLeft.verticalScrollBar().value()

    def mouseMoveEventLeft(self, event):
        if self.pressed:
            self.scrollAreaLeft.horizontalScrollBar().setValue(self.initialPosX - event.pos().x())
            self.scrollAreaLeft.verticalScrollBar().setValue(self.initialPosY - event.pos().y())

    def mousePressEventRight(self, event):
        self.pressed = True
        self.imageLabelRight.setCursor(Qt.ClosedHandCursor)
        self.initialPosX = self.scrollAreaRight.horizontalScrollBar().value() + event.pos().x()
        self.initialPosY = self.scrollAreaRight.verticalScrollBar().value() + event.pos().y()

    def mouseReleaseEventRight(self, event):
        self.pressed = False
        self.imageLabelRight.setCursor(Qt.OpenHandCursor)
        self.initialPosX = self.scrollAreaRight.horizontalScrollBar().value()
        self.initialPosY = self.scrollAreaRight.verticalScrollBar().value()

    def mouseMoveEventRight(self, event):
        if self.pressed:
            self.scrollAreaRight.horizontalScrollBar().setValue(self.initialPosX - event.pos().x())
            self.scrollAreaRight.verticalScrollBar().setValue(self.initialPosY - event.pos().y())

    def open(self):
        options = QFileDialog.Options()
        # fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
        fileName, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '',
                                                  'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)
        if fileName:
            print(fileName)
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fileName)
                return

            self.imageLabelLeft.setPixmap(QPixmap.fromImage(image))
            self.imageLabelRight.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0

            self.scrollAreaLeft.setVisible(True)
            self.scrollAreaRight.setVisible(True)
            self.window.printLeftAct.setEnabled(True)
            self.window.printRightAct.setEnabled(True)
            self.window.fitToWindowAct.setEnabled(True)
            self.updateActions()

            if not self.window.fitToWindowAct.isChecked():
                self.imageLabelLeft.adjustSize()
                self.imageLabelRight.adjustSize()

    def openLeft(self):
        options = QFileDialog.Options()
        # fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
        fileName, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '',
                                                  'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)
        if fileName:
            print(fileName)
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fileName)
                return

            self.imageLabelLeft.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0

            self.scrollAreaLeft.setVisible(True)
            self.window.printLeftAct.setEnabled(True)
            self.window.fitToWindowAct.setEnabled(True)
            self.updateActions()

            if not self.window.fitToWindowAct.isChecked():
                self.imageLabelLeft.adjustSize()

    def openRight(self):
        options = QFileDialog.Options()
        # fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
        fileName, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '',
                                                  'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)
        if fileName:
            print(fileName)
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fileName)
                return

            self.imageLabelRight.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0

            self.scrollAreaRight.setVisible(True)
            self.window.printRightAct.setEnabled(True)
            self.window.fitToWindowAct.setEnabled(True)
            self.updateActions()

            if not self.window.fitToWindowAct.isChecked():
                self.imageLabelRight.adjustSize()

    def printLeft(self):
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.imageLabelLeft.pixmap().size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.imageLabelLeft.pixmap().rect())
            painter.drawPixmap(0, 0, self.imageLabelLeft.pixmap())

    def printRight(self):
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.imageLabelRight.pixmap().size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.imageLabelRight.pixmap().rect())
            painter.drawPixmap(0, 0, self.imageLabelRight.pixmap())

    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)

    def normalSize(self):
        self.imageLabelLeft.adjustSize()
        self.imageLabelRight.adjustSize()
        self.scaleFactor = 1.0

    def about(self):
        QMessageBox.about(self, "Image View in the Main Window",
                          "<p>The <b>Image Viewer</b> example shows how to combine "
                          "QLabel and QScrollArea to display an image. QLabel is "
                          "typically used for displaying text, but it can also display "
                          "an image. QScrollArea provides a scrolling view around "
                          "another widget. If the child widget exceeds the size of the "
                          "frame, QScrollArea automatically provides scroll bars.</p>"
                          "<p>The example demonstrates how QLabel's ability to scale "
                          "its contents (QLabel.scaledContents), and QScrollArea's "
                          "ability to automatically resize its contents "
                          "(QScrollArea.widgetResizable), can be used to implement "
                          "zooming and scaling features.</p>"
                          "<p>In addition the example shows how to use QPainter to "
                          "print an image.</p>")

    def updateActions(self):
        self.window.zoomInAct.setEnabled(not self.window.fitToWindowAct.isChecked())
        self.window.zoomOutAct.setEnabled(not self.window.fitToWindowAct.isChecked())
        self.window.normalSizeAct.setEnabled(not self.window.fitToWindowAct.isChecked())

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageLabelLeft.resize(self.scaleFactor * self.imageLabelLeft.pixmap().size())
        self.imageLabelRight.resize(self.scaleFactor * self.imageLabelRight.pixmap().size())

        self.adjustScrollBar(self.scrollAreaLeft.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollAreaLeft.verticalScrollBar(), factor)
        self.adjustScrollBar(self.scrollAreaRight.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollAreaRight.verticalScrollBar(), factor)

        self.window.zoomInAct.setEnabled(self.scaleFactor < 3.0)
        self.window.zoomOutAct.setEnabled(self.scaleFactor > 0.333)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                               + ((factor - 1) * scrollBar.pageStep() / 2)))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.imageViewSync = QImageViewSync(window=self)
        self.setCentralWidget(self.imageViewSync.centralWidget)

        self.createActions(self.imageViewSync)
        self.createMenus()

        self.setWindowTitle("Image View Sync in the Main Window")
        self.resize(1200, 600)

    def fitToWindow(self):
        fitToWindow = self.fitToWindowAct.isChecked()
        self.imageViewSync.scrollAreaLeft.setWidgetResizable(fitToWindow)
        self.imageViewSync.scrollAreaRight.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.imageViewSync.normalSize()

        self.imageViewSync.updateActions()

    def createActions(self, view):
        self.openLeftAct = QAction("&Open Left...", self, shortcut="Ctrl+O", triggered=view.openLeft)
        self.openRightAct = QAction("&Open Right...", self, shortcut="Shift+Ctrl+O", triggered=view.openRight)
        self.printLeftAct = QAction("&Print Left...", self, shortcut="Ctrl+P", enabled=False, triggered=view.printLeft)
        self.printRightAct = QAction("&Print Right...", self,
                                     shortcut="Shift+Ctrl+P", enabled=False, triggered=view.printRight)
        # self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q", triggered=image.close)
        self.zoomInAct = QAction("Zoom &In (25%)", self, shortcut="Ctrl++", enabled=False, triggered=view.zoomIn)
        self.zoomOutAct = QAction("Zoom &Out (25%)", self, shortcut="Ctrl+-", enabled=False, triggered=view.zoomOut)
        self.normalSizeAct = QAction("&Normal Size", self, shortcut="Ctrl+S", enabled=False, triggered=view.normalSize)
        self.fitToWindowAct = QAction("&Fit to Window", self,
                                      enabled=False, checkable=True, shortcut="Ctrl+F", triggered=self.fitToWindow)
        self.aboutAct = QAction("&About", self, triggered=view.about)
        self.aboutQtAct = QAction("About &Qt", self, triggered=qApp.aboutQt)

    def createMenus(self):
        self.fileMenu = QMenu("&File", self)
        self.fileMenu.addAction(self.openLeftAct)
        self.fileMenu.addAction(self.openRightAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.printLeftAct)
        self.fileMenu.addAction(self.printRightAct)
        self.fileMenu.addSeparator()
        # self.fileMenu.addAction(self.exitAct)

        self.viewMenu = QMenu("&View", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addAction(self.normalSizeAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fitToWindowAct)

        self.helpMenu = QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addMenu(self.viewMenu)
        self.menuBar().addMenu(self.helpMenu)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


