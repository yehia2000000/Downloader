##############################################################################
##############################################################################
#####################    yehia ahmed Ibrahim      ############################
#####################    Link Dowloader           ############################
#####################    12/20/2021               ############################
##############################################################################
##############################################################################

###########################Define the library##################################
import ntpath
import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PyQt5.uic import loadUiType
import sys
import os
import urllib.request
###########################Define the QT design ###############################

FormClass,_ = loadUiType (ntpath.join(ntpath.dirname(__file__),"Dowloader.ui"))

###########################Define the main Window by class####################

class MainAPP (QWidget,FormClass):
    def __init__(self,parent = None):
        super(MainAPP,self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.Handle_UI()
        self.Handle_Buttons()

    def Handle_UI (self):
        self.setWindowTitle("Link Downloader")
        self.setFixedSize(462,215)


    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.Handle_Dowload)
        self.pushButton_2.clicked.connect (self.Handle_Brows)
    def Handle_Brows (self):
        save_place = QFileDialog.getSaveFileName(self,caption="Save As",directory=".",filter="All Files (*.*)")
        save_place =str(save_place)
        text = save_place.split('\'')[1]
        self.lineEdit_2.setText(text)


    def Handle_progress(self,BlockNum,BlockSize,TotalSize):
        ReadValue = BlockNum*BlockSize
        if TotalSize > 0 :
            percent = (ReadValue/TotalSize)*100
            percent = int (percent)
            self.progressBar.setValue(percent)
            QApplication.processEvents()
    def Handle_Dowload (self) :
        url = self.lineEdit.text()
        SaveLocation = self.lineEdit_2.text()
        try :
            urllib.request.urlretrieve(url,SaveLocation,self.Handle_progress)
            QMessageBox.information (self , "Completed Download","the download is finished")
        except :
            QMessageBox.warning (self , "Not Completed Download","the download is not finished")

        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')





def main ():
    app = QApplication(sys.argv)
    Window_Loop = MainAPP()
    Window_Loop.show()
    app.exec()

if __name__ == '__main__':
    main()



