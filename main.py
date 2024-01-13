from PyQt5.QtWidgets import (QApplication, QWidget, QListWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout, QFileDialog )
import os
app = QApplication([])
window = QWidget() 
window.setWindowTitle("Easy editor") 
window.resize (800,800)
main_line = QHBoxLayout()
line1 = QVBoxLayout() 
btn_folder = QPushButton("Folder")
list_widget = QListWidget() 
line1.addWidget(btn_folder) 
line1.addWidget(list_widget) 

main_line.addLayout(line1) 


window.setLayout(main_line) 
line2 = QVBoxLayout() 
image = QLabel() 
button_line = QHBoxLayout() 
btn1 = QPushButton('1') 
btn2 = QPushButton('2') 
btn3 = QPushButton('3') 
btn4 = QPushButton('4') 
btn5 = QPushButton('5') 
button_line.addWidget(btn1) 
button_line.addWidget(btn2) 
button_line.addWidget(btn3) 
button_line.addWidget(btn4) 
button_line.addWidget(btn5) 
line2.addWidget(image) 
line2.addLayout(button_line) 
main_line.addLayout(line2)  

def filter  (files): 
    img_files = []

    for file in files: 
        if file.split('.')[-1] == "png": 
            img_files.append(file) 
            filters = ['png','jpg','jpeg','gif'] 
            return img_files 
        workdir = ''
def showfolder(): 
    global workdir
    workdir = QFileDialog.getExistingDirectory() 
    filenames = filter(os.listdir(workdir)) 

btn_folder.clicked.connect(showfolder)

window.show()

app.exec_()