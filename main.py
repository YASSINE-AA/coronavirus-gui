from PySide2.QtWidgets import QApplication
from classes import MainWindow
import sys
# Author Yassine Ahmed Ali

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
