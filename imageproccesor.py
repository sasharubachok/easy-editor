import os 
from PIL import Image, ImageFilter 
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
class ImageProccesor: 
    def __init__(self):
        self.original = None 
        self.filename = None 
        self.dir = None 
        self.save_dir = 'edited/' 

def loadimage(self, filename): 
    self.filename = filename
    path = os/path.join(self.dir,self.filename) 
    self.original = Image.open(path) 
 
def showimage(self, path, label): 
    label.hide() 
    pixmap = QPixmap(path) 


    w = label.width() 
    h  = label.width() 

    pixmap = pixmap.scaled(w,h,Qt.keepAspectRatio) 
    label.setPixmap(pixmap) 

    def do_bw(self):