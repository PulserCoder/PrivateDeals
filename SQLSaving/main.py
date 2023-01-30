from table_column_edit import table_caolumn_edit
from table_data_edit import table_data_edit

class PushingInDataBase(table_data_edit, table_caolumn_edit):
    def __init__(self, fullname: str, age: int,
                 school: str, phone_number: str, photo: str, email: str, family: str, mom_number: str,
                 dad_number: str, mom_work: str, dad_work: str):
        self.fullname = fullname
        self.age = age
        self.school = school
        self.phone_number = phone_number
        self.photo = photo
        self.email = email
        self.family = family
        self.mom_number = mom_number
        self.dad_number = dad_number
        self.mom_work = mom_work
        self.dad_work = dad_work
        self.data_edit_add()

    def column_edit_drop(self, column_name):
        self.column_drop(column_name)

    def column_edit_add(self, column_name, column_type):
        self.column_add(column_name, column_type)

    def data_edit_add(self, columns, values):
        self.data_add(columns, values)

    def data_edit_update(self, columns, values):
        self.data_edit(columns, values)

    def data_edit_delete(self, column, values):
        self.data_delete(column, values)