from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import os
from PIL.ImageFilter import *
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image, ImageFilter, ImageEnhance


def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap


app = QApplication([])
window = QWidget()
window.resize(700,500)
app.setStyleSheet("""     QWidget {
        background: #ccdaed;     }
     QPushButton {        background: #e9edf2;
        border-style: outset;        min-height: 30px;
        min-width: 100px;     }
     QListWidget {         background: #ccdbd5;
     }     QTextEdit { 
        background: #e1ede8;     }
      QPushButton {
        color: green;        font-size: 15px;
        font-family: Impact;        border-width: 2px;
        border-color: red;        border-radius: 5px;
     }
      QPushButton#save_btn {
        color: green;        font-size: 20px;
        font-family: Impact;        border-width: 4px;
        border-color: red;        border-radius: 5px;
      }
 """)

papka_btn = QPushButton("Папка")
left_btn = QPushButton("Вліво")
right_btn = QPushButton("Вправо")
mirror_btn = QPushButton("Дзеркало")
sharpness_btn = QPushButton("Різкість")
rozmitya_btn = QPushButton("Розмиття")
blachwhite_btn = QPushButton("Ч/Б")
k_btn = QPushButton("Контрастність")
n_btn = QPushButton("Насиченість")
files_list = QListWidget()
photo = QLabel("спуйк")

main_line = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()

main_line.addLayout(v1)
main_line.addLayout(v2)
v1.addWidget(papka_btn)
v1.addWidget(files_list)

v2.addWidget(photo)
v2.addLayout(h1)
v2.addLayout(h2)


h1.addWidget(left_btn)
h1.addWidget(right_btn)
h1.addWidget(mirror_btn)
h1.addWidget(sharpness_btn)
h1.addWidget(rozmitya_btn)

h2.addWidget(blachwhite_btn)
h2.addWidget(k_btn)
h2.addWidget(n_btn)
class WorkWithPhoto:
    def __init__(self):
        self.image = None
        self.folder = None
        self.image_name = None

    def load(self):
        full_path = os.path.join(self.folder, self.image_name)
        self.image = Image.open(full_path)

    def show_image(self):
        pixel = pil2pixmap(self.image)
        photo.setPixmap(pixel)

    def rozmitya(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.show_image()
    def sharpness(self):
        self.image = ImageEnhance.Brightness(self.image).enhance(1.5)
        self.show_image()

    def mirror(self):
        self.image =self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.show_image()
    def right(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.show_image()
    def left(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.show_image()
    def blachwhite(self):
        self.image = self.image.convert("L")
        self.show_image()
    def k(self):
        self.image = ImageEnhance.Contrast(self.image).enhance(1.7)
        self.show_image()
    def n(self):
        self.image = ImageEnhance.Color(self.image).enhance(1.9)
        self.show_image()
work_with_photo = WorkWithPhoto()
def show_directory():
    work_with_photo.folder = QFileDialog.getExistingDirectory()
    list_files = os.listdir(work_with_photo.folder)
    files_list.clear()
    for file in list_files:
        if file.endswith("png"):
            files_list.addItem(file)

papka_btn.clicked.connect(show_directory)
def show_photo():
    image_name = files_list.currentItem().text()
    work_with_photo.image_name = image_name
    work_with_photo.load()
    work_with_photo.show_image()
files_list.currentRowChanged.connect(show_photo)
rozmitya_btn.clicked.connect(work_with_photo.rozmitya)
sharpness_btn.clicked.connect(work_with_photo.sharpness)
mirror_btn.clicked.connect(work_with_photo.mirror)
right_btn.clicked.connect(work_with_photo.right)
left_btn.clicked.connect(work_with_photo.left)
blachwhite_btn.clicked.connect(work_with_photo.blachwhite)
k_btn.clicked.connect(work_with_photo.k)
n_btn.clicked.connect(work_with_photo.n)
window.setLayout(main_line)
window.show()
app.exec()