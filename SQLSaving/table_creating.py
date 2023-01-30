import sqlite3


class table:
    def __init__(self):
        query = '''
                    CREATE TABLE Students(
                    Id integer PRIMARY KEY AUTOINCREMENT,
                    "fullname" nvachar(30),
                    "age" integer,
                    "sex" nvarchar(10),
                    "group" nvarchar(10),
                    "school" nvarchar(30),
                    "mobile phone" varchar(15),
                    "photo" nvarchar(300),
                    "email" varchar(50),
                    "family" varchar(15),
                    "mobile of mother" varchar(15),
                    "mobile of father" varchar(15),
                    "parents working place" nvarchar(150)
                    )
                '''
        self._table_open(query)

    def _table_open(self, query, arguments=None):
        with sqlite3.connect('students.db') as connection:
            cursor = connection.cursor()
            if arguments == None:
                cursor.execute(query)
            else:
                cursor.execute(query, arguments)


