from PyQt5.QtWidgets import (
    QApplication, QWidget, QListWidget, 
    QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QFileDialog )
import os
from imageproccesor import ImageProccesor
app = QApplication([])
window = QWidget()
window.setWindowTitle("Easy editor")
window.resize(800,800)

main_line = QHBoxLayout()

line1 = QVBoxLayout()
btn_folder = QPushButton("Folder")
list_widget = QListWidget()

line1.addWidget(btn_folder)
line1.addWidget(list_widget)

main_line.addLayout(line1)

line2 = QVBoxLayout()
image = QLabel("image")

button_line = QHBoxLayout()
btn1 = QPushButton('1')
btn1.setStyleSheet('''
background-color: #ff00ff;
''')
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

window.setLayout(main_line)

def filter (files):
    img_files = []
    filters = ['png', 'jpg', 'jpeg', 'gif']

    for file in files:
        if file.split('.')[-1] in filters:
            img_files.append(file)

    return img_files
workdir = ''

def showFolder():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    filenames = filter(os.listdir(workdir))

    list_widget.addItems(filenames)

def left():
    print(workdir)


btn_folder.clicked.connect(showFolder)
workImage = ImageProccesor()
def showChowItem() :
    filename = list_widget.currentItem().text()
    workImage.loadImage(filename) 
    workImage.showImage(os.path.join(workdir, filename), image) 

list_widget.currentRowChanged.connect(showChowItem)
window.show()

app.exec_()