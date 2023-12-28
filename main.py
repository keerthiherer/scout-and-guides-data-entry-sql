import sys
import pyttsx3
from PyQt5.QtWidgets  import *
from PyQt5 import *
from PyQt5 import QtCore 
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import *
import pyautogui
from PyQt5 import QtGui , QtWidgets
import pymysql
import pymysql.cursors
from PyQt5.QtCore import *

mycon = pymysql.connect(host = "localhost", user = "root", password = "your password", database = "select your database",cursorclass=pymysql.cursors.DictCursor) 
cursor = mycon.cursor()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
      # print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def updateRecord(ss,tt,uu,vv,ww,xx,bb):
      mycon = pymysql.connect(host = "localhost", user = "root", password = "your password", database = "select your database") 
      cursor = mycon.cursor()
      do = "insert into keeth values(" + "'"+ss+"'" +","+"'"+tt+"'"+"," +"'"+ uu +"'" +","+ "'"+vv+"'" + ","+"'"+ww+"'" + ","+"'" +xx+"'" ",""'"+bb+"'" +");"
      print(do)
      cursor.execute(do)
      mycon.commit()
      speak("successfully data updated")
      msg = QMessageBox() 
      msg.setIcon(QMessageBox.Information)  
      msg.setText("Data successfully updated")
      msg.setWindowTitle("Done MessageBox") 
      msg.setStandardButtons(QMessageBox.Ok ) 
      retval = msg.exec_()

def deleteRecord(bsss):
      mycon = pymysql.connect(host = "localhost", user = "root", password = "Your passowrd", database = "select your database") 
      cursor = mycon.cursor()
      do = "delete from keeth where BS_G_id = " "'"+bsss+"'"+ ";"
      print(do)
      cursor.execute(do)
      mycon.commit()
      speak("successfully Deleted data")
      msg = QMessageBox() 
      msg.setIcon(QMessageBox.Information)  
      msg.setText("Data successfully removed")
      msg.setWindowTitle("Done MessageBox") 
      msg.setStandardButtons(QMessageBox.Ok ) 
      retval = msg.exec_()
      mycon.close()

def find_record(finee):
      mycon = pymysql.connect(host = "localhost", user = "root", password = "your password", database = "select your database")
      cursor = mycon.cursor()
      doo = "select * from keeth where BS_G_id =" +"'"+ finee +"';"
      print(doo)
      cursor.execute(doo)
      mycon.commit()
      data = cursor.fetchone()
      count = cursor.rowcount
      for row in data:
            print(row)
      speak("here the data which you are looking for. It is printed over here")

def speak(audio):
      engine.say(audio)
      engine.runAndWait()

speak("welcome to scout and guides sql dataentry app, created my keerthibalan")

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle("THE BHARATH SCOUTS AND GUIDS")
    wsize = 1000
    hsize = 740
    w.setFixedWidth(wsize)
    w.setFixedHeight(hsize)

    bg = QLabel(w)
    #bg.setStyleSheet("background-color : DarkSlateGray;")
    bg.setStyleSheet("background-color:DarkSlateGray;")
    bg.resize(900,900)
    bg.setGeometry(0,0,1600,739)
    bg.show()

    btn = QLabel(w)
    btn.setText("NAME:")
    btn.setGeometry(30,40,180,40)
    btn.setStyleSheet('''
    background-color: grey;
    color: white;
    border-style: outset;
    padding: 2px;
    font: bold 20px;
    border-width: 3px;
    border-radius: 4px;
    border-color: blue;
''')
    btn.show()

    btn1 = QLabel(w)
    btn1.setText("Class:")
    btn1.setGeometry(30,120,180,40)
    btn1.setStyleSheet('''background-color: grey;
    color: white;
    border-style: outset;
    padding: 2px;
    font: bold 20px;
    border-width: 3px;
    border-radius: 4px;
    border-color: blue;''')
    btn1.show()

    btn2 = QLabel(w)
    btn2.setText("Father name:")
    btn2.setGeometry(30,200,180,40)
    btn2.setStyleSheet('''background-color: grey;
    color: white;
    border-style: outset;
    padding: 2px;
    font: bold 20px;
    border-width: 3px;
    border-radius: 4px;
    border-color: blue;''')
    btn2.show()

    btn3 = QLabel(w)
    btn3.setText("Mother name:")
    btn3.setGeometry(30,280,180,40)
    btn3.setStyleSheet('''background-color: grey;
    color: white;
    border-style: outset;
    padding: 2px;
    font: bold 20px;
    border-width: 3px;
    border-radius: 4px;
    border-color: blue;''')
    btn3.show()

    btn4 = QLabel(w)
    btn4.setText("Date of Birth:")
    btn4.setGeometry(30,360,180,40)
    btn4.setStyleSheet('''background-color: grey;
    color: white;
    border-style: outset;
    padding: 2px;
    font: bold 20px;
    border-width: 3px;
    border-radius: 4px;
    border-color: blue;''')
    btn4.show()

    btn5 = QLabel(w)
    btn5.setText("Date of Joining:")
    btn5.setGeometry(30,440,180,40)
    btn5.setStyleSheet('''background-color: grey;
    color: white;
    border-style: outset;
    padding: 2px;
    font: bold 20px;
    border-width: 3px;
    border-radius: 4px;
    border-color: blue;''')
    btn5.show()

    btnbs = QLabel(w)
    btnbs.setText("BS & G UID:")
    btnbs.setGeometry(30,520,180,40)
    btnbs.setStyleSheet('''background-color: grey;
    color: white;
    border-style: outset;
    padding: 2px;
    font: bold 20px;
    border-width: 3px;
    border-radius: 4px;
    border-color: blue;''')
    btnbs.show()    

    btn7 = QPushButton(w)
    btn7.setText("Delete record")
    btn7.setGeometry(300,600,150,50)
    btn7.setStyleSheet("background-color:red; color:white; border-style:outset;padding:2px; font:bold 20px;")
    def dell():
            text,ddu = QtWidgets.QInputDialog.getText(w,"DELETE","Enter the BS&G UID to delete:")
            deleteRecord(text)

    btn7.clicked.connect(dell)
    btn7.show()

    btn8 = QPushButton(w)
    btn8.setText("Find Record")
    btn8.setGeometry(555,600,150,50)
    btn8.setStyleSheet("background-color:violet; color:white; border-style:outset;padding:2px; font:bold 20px;")
    def find():
          text2,ddd = QtWidgets.QInputDialog.getText(w,"Find", "Enter the BS&G UID to find Record of:")
          find_record(text2)
    btn8.clicked.connect(find)
    btn8.show()

    btnn = QPushButton(w)
    btnn.setText("Special commands")
    btnn.setGeometry(760,600,200,50)
    btnn.setStyleSheet("background-color:orange; color:white; border-style:outset;padding:2px; font:bold 20px;")
    def specc():
          pyautogui.hotkey('ctrl','alt','s')
    btnn.clicked.connect(specc)
    btnn.show()

    btn6 = QPushButton(w)
    btn6.setText("UPADTE")
    btn6.setGeometry(45,600,150,50)
    btn6.setStyleSheet('''background-color:green; color:white;
                       border-style: outset;
    padding: 2px;
    font: bold 20px;
  
}
''')
    
    def you():
     #if any(c.isalpha() for c in word) and any(c.isdigit() for c in word):
         s,t,u,v,w,x,bs = in1.text(),in2.text(),in3.text(),in4.text(),in5.text(),in6.text(),in7.text()
         if s == "" or (s.isalnum() and ( not s.isalpha())):
               msg = QMessageBox() 
               msg.setIcon(QMessageBox.Warning)  
               msg.setText("Name cannot be empty or integer")
               msg.setWindowTitle("Alert MessageBox") 
               msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
               retval = msg.exec_() 
                   
         elif t == "" :
               msg = QMessageBox() 
               msg.setIcon(QMessageBox.Warning)  
               msg.setText("Class cannot be empty")
               msg.setWindowTitle("Alert MessageBox") 
               msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
               retval = msg.exec_() 
                    
         elif u =="" or (u.isalnum() and ( not u.isalpha())): 
               msg = QMessageBox() 
               msg.setIcon(QMessageBox.Warning)  
               msg.setText("Father Name cannot be empty or integer")
               msg.setWindowTitle("Alert MessageBox") 
               msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
               retval = msg.exec_()
    
         elif v == "" or (v.isalnum() and ( not v.isalpha())):
               msg = QMessageBox() 
               msg.setIcon(QMessageBox.Warning)  
               msg.setText("Mother Name cannot be empty or integer")
               msg.setWindowTitle("Alert MessageBox") 
               msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
               retval = msg.exec_() 
         elif x == "":
               msg = QMessageBox()
               msg.setIcon(QMessageBox.Warning)
               msg.setText("Date of Joining cannot be empty")
               msg.setWindowTitle("Alert MessageBox")
               msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
               retval = msg.exec_()
                 
         elif w == "" or w.isalpha():
               msg = QMessageBox() 
               msg.setIcon(QMessageBox.Warning)  
               msg.setText("Date of Birth cannot be empty or alphabet")
               msg.setWindowTitle("Alert MessageBox")
               msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
               retval = msg.exec_()

         elif bs == "":
               msg = QMessageBox()
               msg.setIcon(QMessageBox.Warning)
               msg.setText("Bharth scout and guides id can't be empty")
               msg.setWindowTitle("Alert MessageBox")
               msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)      
         updateRecord(s,t,u,v,w,x,bs)   
         in1.clear(),in2.clear(),in3.clear(),in4.clear(),in5.clear(),in6.clear(),in7.clear()
         print(s,t,u,v,w,x,bs)
    btn6.clicked.connect(you)
    btn6.show()
    
    in1 = QLineEdit(w)
    in1.setGeometry(300,40,300,40)
    in1.show()

    in2 = QLineEdit(w)
    in2.setGeometry(300,120,300,40)
    in2.show()

    in3 = QLineEdit(w)
    in3.setGeometry(300,200,300,40)
    in3.show()

    in4 = QLineEdit(w)
    in4.setGeometry(300,280,300,40)
    in4.show()

    in5 = QLineEdit(w)
    in5.setGeometry(300,360,300,40)
    in5.show()

    in6 = QLineEdit(w)
    in6.setGeometry(300,440,300,40)
    in6.show()

    in7 = QLineEdit(w)
    in7.setGeometry(300,520,300,40)
    in7.show()

    w.show()
    sys.exit(app.exec_())
