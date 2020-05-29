from PySide2.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton
from PySide2.QtGui import QFont
import data
# Author Yassine Ahmed Ali


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle("Coronacases")
        self.setFixedSize(370,  180)
        self.ui_components()

        self.show()

    def ui_components(self):
        # fonts
        font = QFont("Roboto", 15)

        # 'enter country name' label
        enter_country_label = QLabel("Enter country name: ", self)
        enter_country_label.setFont(font)
        enter_country_label.move(10, 10)
        enter_country_label.adjustSize()

        # 'country name' line edit
        country_name = QLineEdit(self)
        country_name.setFixedSize(200, 25)
        country_name.setFont(font)
        country_name.setPlaceholderText("Ex: Tunisia")
        country_name.move(10, 40)
        country_name_submit = QPushButton("Search", self)
        country_name_submit.setFixedSize(130, 25)
        country_name_submit.move(220, 40)

        # Displays worldwide data as default
        cases_label = QLabel(
            f"Current cases: {data.CoronaCases('').total_cases}", self)
        cases_label.setFont(font)
        cases_label.adjustSize()
        cases_label.move(10, 85)

        deaths_label = QLabel(
            f"Current deaths: {data.CoronaCases('').total_deaths}", self)
        deaths_label.setFont(font)
        deaths_label.adjustSize()
        deaths_label.move(10, 112.8)

        recovered_label = QLabel(
            f"Current recovered: {data.CoronaCases('').total_recovered}", self)
        recovered_label.setFont(font)
        recovered_label.adjustSize()
        recovered_label.move(10, 140)

        # Updates the labels with country specific data.
        def label_updater():
            cases_label.setText(
                f"Current cases: {data.CoronaCases('country/'+country_name.text().lower()).total_cases}")
            deaths_label.setText(
                f"Current deaths: {data.CoronaCases('country/'+ country_name.text().lower()).total_deaths}")
            recovered_label.setText(
                f"Current recovered: {data.CoronaCases('country/'+ country_name.text().lower()).total_recovered}")

        country_name_submit.clicked.connect(label_updater)
