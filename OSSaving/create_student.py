import os


class Student:
    def __init__(self, fullname: str, age: int, gender: str,
                 school: str, group: str, phone_number: str, photo: str, email: str, family: str, mom_number: str,
                 dad_number: str, work: str):
        """Инициализация всех параметров"""
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.school = school
        self.group = group
        self.phone_number = phone_number
        self.photo = photo
        self.email = email
        self.family = family
        self.mom_number = mom_number
        self.dad_number = dad_number
        self.work = work

    def create_dirs(self):
        """Создание папок"""
        if not os.path.isdir("./students"):
            os.mkdir("./students")
        if not os.path.isdir("./students/IT-1-22"):
            os.mkdir("./students/IT-1-22")
        if not os.path.isdir(f"./students/IT-1-22/{self.fullname}"):
            os.mkdir(f"./students/IT-1-22/{self.fullname}")

    def create_file(self):
        """Создание файла (внутри созданной папки) с информацией студента"""
        with open(f"./students/IT-1-22/{self.fullname}/info.txt", "w") as self.file:
            self.file.write(f"Fullname: {self.fullname}\n"
                            f"Age: {self.age}\n"
                            f"Sex: {self.gender}\n"
                            f"School: {self.school}\n"
                            f"Number: {self.phone_number}\n"
                            f"Photo: {self.photo}\n"
                            f"Email: {self.email}\n"
                            f"Family: {self.family}\n"
                            f"Phone number of mom: {self.mom_number}\n"
                            f"Phone number of dad: {self.dad_number}\n"
                            f"work: {self.work}\n"
                            f"Group: {self.group}\n")


student = Student("Boronov Roman", 16, "male", "Singularity", "IT-1-22", "+79674727177", "photo",
                  "r.boronov@it-park.tech", "two parents, two sons", "+79093048072", "+79093048073", "akkond")
student.create_dirs()
student.create_file()
