import cv2
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from add import *
import csv
import pyqtgraph as pg



class add(QMainWindow,Ui_add_MainWindow):
    def __init__(self,parent=None):
        super(add,self).__init__(parent)
        self.ui = Ui_add_MainWindow()
        self.ui.setupUi(self)

        self.logic=0
        #self.ui.button_graph.clicked.connect(self.graphic_view)
        self.ui.start_camera.clicked.connect(self.dis)
        self.ui.take_picture.clicked.connect(self.capture)
        self.ui.name.clicked.connect(self.search_by_name)
        self.ui.date.clicked.connect(self.search_by_date)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.ui.room_textEdit.setFont(font)

    def exit(self):
        vid.release()
        self.close()


#The function dis to run the camera and save new Picture to dataset
    def dis(self):
        global vid
        vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while True:
            success, img = vid.read()
            if success==True:
                self.displayyy(img, self.ui.display_camera)
                cv2.waitKey()
                if (self.logic == 2):
                    path = 'C:/Users/USER/PycharmProjects/attendancea and face recognition/imageattendance'
                    cv2.imwrite(os.path.join(path, name+'.jpg'), img)
                    self.logic=1


#The function capture is to take new student picture
    def capture(self):
        global name
        name = self.ui.addstudent.text()
        self.ui.addstudent.clear()
        self.ui.addstudent.setFocus()
        print('Your name: ' + name)
        self.logic=2


#The function displayyy to display the camera in the GUI
    def displayyy(self,img,label):

        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        frameb = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(frameb)
        resized = pix.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio)
        label.setPixmap(resized)



#The function  search_by_name give back attendance of one student name during all months with graph and average of attendance.
    def search_by_name(self):
        count_jan = 0
        count_feb = 0
        count_mar = 0
        count_avr = 0
        count_mai = 0
        count_jui = 0
        count_jul = 0
        count_aug = 0
        count_Sep = 0
        count_oct = 0
        count_nov = 0
        count_dec = 0
        student_name = self.ui.date_or_name.text()
        self.ui.room_textEdit.clear()
        student_name=str(student_name).upper()
        print('Your name: '+student_name)

        with open('Attendance.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            self.count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    if row[0] == student_name:
                        print('ok')
                        self.count = self.count + 1
                        month = str(row[2])
                        month = month[3:6]
                        if month == 'Jan':
                            count_jan += 1
                        elif month == 'Sep':
                            count_feb += 1
                        elif month == 'Oct':
                            count_mar += 1
                        elif month == 'Nov':
                            count_avr += 1
                        elif month == 'Dec':
                            count_mai += 1
                    line_count += 1
        avg=(self.count*100)/20
        self.ui.room_textEdit.setTextColor(QColor(0, 0, 0))
        self.ui.room_textEdit.append(f"Student Name: " + student_name + " was present: " + str(self.count) + " time(s)\n"
                                     +"average of attendace: "+ str(avg)+"%"
                                     +"\nIn January: "+str(count_jan)
                                     +"\nIn September: "+str(count_feb)
                                     +"\nIn October: "+str(count_mar)
                                     +"\nIn November: "+str(count_avr)
                                     +"\nIn December: "+str(count_mai))


        plot = pg.plot(title="Student attendance number for each month")
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        set = [count_jan, count_jui, count_jui, count_jui, count_jui, count_jui, count_jui, count_jui, count_feb,
               count_mar, count_avr, count_mai]
        graphWidget = pg.BarGraphItem(x=months, height=set, width=0.2, brush='b')
        plot.addItem(graphWidget)

        self.ui.addstudent.clear()
        self.ui.addstudent.setFocus()



# The function search_by_date give back all Students names who Attend in that Day.
    def search_by_date(self):
        self.datee = self.ui.date_or_name.text()
        self.ui.date_or_name.clear()
        self.ui.room_textEdit.clear()
        self.ui.date_or_name.setFocus()
        print('Your date: ' + self.datee)

        with open('Attendance.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            self.count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    if row[2] ==self.datee:
                        self.count = self.count + 1
                        self.ui.room_textEdit.setTextColor(QColor(0, 0, 0))
                        self.ui.room_textEdit.append(" -Student Name: " + row[0] + " was present on: " + self.datee)
                        print('ok')
                    line_count += 1

            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            print(f'Processed {line_count} lines.')
            print("count", self.count)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = add()
    window.show()

    sys.exit(app.exec_())
