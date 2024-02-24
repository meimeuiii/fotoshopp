from PyQt6.QtWidgets import *

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
whiteandblack_btn = QPushButton("Ч/Б")
files_list = QListWidget()
photo = QLabel("спуйк")

main_line = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()

main_line.addLayout(v1)
main_line.addLayout(v2)
v1.addWidget(papka_btn)
v1.addWidget(files_list)

v2.addWidget(photo)
v2.addLayout(h1)

h1.addWidget(left_btn)
h1.addWidget(right_btn)
h1.addWidget(mirror_btn)
h1.addWidget(sharpness_btn)
h1.addWidget(whiteandblack_btn)
window.setLayout(main_line)
window.show()
app.exec()