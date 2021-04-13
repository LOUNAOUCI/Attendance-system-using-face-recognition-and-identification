import cv2
import face_recognition
import os
import sys
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate,pyqtSlot
from PyQt5.QtGui import *
from gui_camera import  *
from add_picture import add
import numpy as np
import urllib.request
import threading

#to read all pictures in our database and take name of each picture.
path = 'imageattendance'
images = []
classNames = []
mylist = os.listdir(path)
for cl in mylist:
  curimg = cv2.imread(f'{path}/{cl}')
  images.append(curimg)
  classNames.append(os.path.splitext(cl)[0])


class MyForm(QMainWindow ,Ui_MainWindow):
    global nameliste
    global nameliste2
    global numstudents
    numstudents=[]
    nameliste = []
    nameliste2 = []

    def __init__(self,parent=None):
        super(MyForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


#Current Date and Time
        now = QDate.currentDate()
        current_date = now.toString('ddd dd MMMM yyyy')
        current_time = datetime.now().strftime("%I: %M  %p")

#Display the current Date and Time in the GUI
        self.ui.Date_label.setText(current_date)
        self.ui.Time_label.setText(current_time)

#Push button action
        self.ui.start.clicked.connect(self.start)
        self.ui.end.clicked.connect(self.thread_function)
        self.ui.exit.clicked.connect(self.exit)
        self.ui.add_student.clicked.connect(self.on_pushButton_clicked)

#Font of room text and size
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ui.room_textEdit.setFont(font)

#The function Start to start the first camera of enter
    def start(self):
        video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        encodelistknown = self.findencoding(images)
        while True:
            success, img = video.read()
            if success == True:
                self.Displayy_start(img,encodelistknown,classNames)
                cv2.waitKey(1)
            else :
                print('else')

# The function Start to start the first camera of exit
    def end(self):
        Url="http://192.168.10.103:8080/shot.jpg"
        encodelistknown = self.findencoding(images)
        while True:
            img_array= np.array(bytearray(urllib.request.urlopen(Url).read()), dtype=np.uint8)
            img=cv2.imdecode(img_array,-1)
            self.Displayy_end(img,encodelistknown,classNames)
            cv2.waitKey(1)

#The fuction to display Enter Camera
    def Display_start(self, img, label):
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        frameb = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(frameb)
        resized = pix.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio)
        label.setPixmap(resized)

# The fuction to display Exit Camera
    def Display_end(self, img, label):
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        frameb = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(frameb)
        resized = pix.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio)
        label.setPixmap(resized)


# The function Display_end to detect the face and identify the student in Exit door
    @pyqtSlot(QImage)
    def Displayy_end(self, frame,encodelistknown,classNames):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        facecurframe = face_recognition.face_locations(image)
        encodescurframe = face_recognition.face_encodings(image, facecurframe)
        for encodeface, faceloc in zip(encodescurframe, facecurframe):
            matches = face_recognition.compare_faces(encodelistknown, encodeface)
            facedis = face_recognition.face_distance(encodelistknown, encodeface)
            print('facedis:',facedis)
            matchIndex = np.argmin(facedis)
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                print(name)
                print(faceloc)
                y1, x2, y2, x1 = faceloc
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                if name in nameliste:
                    nameliste.remove(name)
                    print("the new lengh is :",len(nameliste))
                    self.ui.num_student.display(str(len(nameliste)))
            else:
                y1, x2, y2, x1 = faceloc
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (255, 0, 0), cv2.FILLED)
                cv2.putText(frame, 'Unknown', (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        self.Display_end(frame,self.ui.label_frame_2)

# The function Display_start to detect the face and identify the student in Enter door
    def Displayy_start(self, frame,encodelistknown,classNames):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        facecurframe = face_recognition.face_locations(image)
        encodescurframe = face_recognition.face_encodings(image, facecurframe)
        for encodeface, faceloc in zip(encodescurframe, facecurframe):
            matches = face_recognition.compare_faces(encodelistknown, encodeface)
            facedis = face_recognition.face_distance(encodelistknown, encodeface)
            print('facedis:',facedis)
            matchIndex = np.argmin(facedis)
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                print(name)
                print(faceloc)
                y1, x2, y2, x1 = faceloc
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                if name not in nameliste:
                    self.markattendace(name)
                    self.markattendace_sheet(name)
            else:
                y1, x2, y2, x1 = faceloc
                # y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (255, 0, 0), cv2.FILLED)
                cv2.putText(frame, 'Unknown', (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        self.Display_start(frame,self.ui.label_frame)

# The function markattendance to dispaly name and time of student attendance in GUI
    def markattendace(self,name):
        nameliste.append(name)
        now = datetime.now()
        dtstring = now.strftime('%H:%M:%S')
        self.ui.room_textEdit.setTextColor(QColor(0, 0, 255))
        self.ui.room_textEdit.append("Student Name: " + name + "   Start Time: " + dtstring)
        self.ui.num_student.display(str(len(nameliste)))
        numstudents.append(int(len(nameliste)))
        print('number', numstudents)
        print("Values of A:", nameliste)
        print("Values of B:",nameliste2)

# The function markattendance_sheet to save all student names in sheet
    def markattendace_sheet(self,name):
        with open('Attendance.csv', 'a+') as f:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S,%d %b %Y')
            f.writelines(f'\n{name},{dtstring}')

# The function findencoding to encode the images which has faces
    def findencoding(self,images):
        encodelist = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodelist.append(encode)
        return encodelist

# The function exit to close the window
    def exit(self):
        self.close()
#Thread function used to display the two camera in the same time
    def thread_function(self):
        x = threading.Thread(target=self.end)
        x.start()

# The function on_pushButton_clicked to open new window of student information
    def on_pushButton_clicked(self):
        self.window = add()
        self.window.show()



if __name__=="__main__":
    app = QApplication(sys.argv)
    winn=MyForm()
    winn.show()

    sys.exit(app.exec_())
