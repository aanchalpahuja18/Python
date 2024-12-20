#PyQy5 Labels

import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

from PyQt5.QtGui import QIcon, QFont

from PyQt5.QtCore import Qt

# main window is the class which inherits from the qmainwindow parent class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setWindowIcon(QIcon(""))
        self.setGeometry(800,300,500,500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: blue;"
                            "background-color: yellow;"
                            "font-weight: 200;"
                            "text-decoration: underline;"
                            "font-style: italic;")
        
        # label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()