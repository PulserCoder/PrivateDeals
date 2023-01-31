from ExcelSaving.excel_class import ExcelStudent
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt6 import uic
import sys
from OSSaving.create_student import Student


text_gender = 'М'

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('temp/PrivatesDeals.ui', self)
        self.add_student.clicked.connect(self.take_data)
        self.male_radiobutton.toggled.connect(self.onClicked)
        self.female_radiobutton.toggled.connect(self.onClicked)
        self.load_file.clicked.connect(self.take_image_from_user)

    def onClicked(self):
        global text_gender
        radiobutton = self.sender()
        if radiobutton.isChecked():
            text_gender = radiobutton.text()

    def take_data(self):
        name = self.textname.toPlainText()
        age = self.age.toPlainText()
        textschool = self.textschool.toPlainText()
        number = self.number.toPlainText()
        email = self.email.toPlainText()
        member = self.member.toPlainText()
        number_father = self.number_father.toPlainText()
        number_mother = self.number_mather.toPlainText()
        place_jobs = self.place_jobs.toPlainText()

        self.textname.setText('')
        self.age.setText('')
        self.textschool.setText('')
        self.number.setText('')
        self.email.setText('')
        self.member.setText('')
        self.number_father.setText('')
        self.number_mather.setText('')
        self.place_jobs.setText('')


        self.save_data_in_excel(name, age, textschool, number, fname, email, member, number_mother, number_father, place_jobs, place_jobs, text_gender, 'ИТ-21')

    def take_image_from_user(self):
        global fname
        fname = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "c:\\gui\\images",
            "All Files (*);;Python Files (*.py);; PNG Files (*.png)",
        )

    def save_data_in_excel(self, fullname: str, age: int,
                 school: str, phone_number: str, photo: str, email: str, family: str, mom_number: str,
                 dad_number: str, mom_work: str, dad_work: str, floor: str, group: str):
        excel = ExcelStudent(fullname, age, school, phone_number, photo, email, family, mom_number, dad_number, mom_work, dad_work, floor, group).run()

    # def save_data_in_files(self, fullname: str, age: int,
    #              school: str, phone_number: str, photo: str, email: str, family: str, mom_number: str,
    #              dad_number: str, mom_work: str, dad_work: str, floor: str, group: str):
    #     excel = Student(fullname, age, school, phone_number, photo, email, family, mom_number, dad_number, mom_work, dad_work, floor, group).run()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()

    sys.exit(app.exec())
