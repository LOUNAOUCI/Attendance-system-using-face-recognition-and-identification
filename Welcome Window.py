import sys
from PyQt5.QtWidgets import *
from start_win import *
from test import MyForm

class Start_window(QMainWindow ,Ui_start_MainWindow):
    def __init__(self,parent=None):
        super(Start_window, self).__init__(parent)
        self.ui = Ui_start_MainWindow()
        self.ui.setupUi(self)

# Start push button
        self.ui.Start_window.clicked.connect(self.start)

#the function start used to open the main window face recognition when we click on Start push button
    def start(self):
        self.hide()
        self.window = MyForm()
        self.window.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Start_window()
    w.show()
    sys.exit(app.exec_())
