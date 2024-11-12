#PyQt5 Images

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

from PyQt5.QtGui import QPixmap

# main window is the class which inherits from the qmainwindow parent class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Images in PyQt5")
        self.setGeometry(800,300,500,500)

        pixmap = QPixmap("pyqt5\\profile_image.jpg")
        label = QLabel(self)
        label.setGeometry(0,0,250,250)
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry(self.width() - label.width(),
                          self.height() - label.height(),
                          label.width(), 
                          label.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()