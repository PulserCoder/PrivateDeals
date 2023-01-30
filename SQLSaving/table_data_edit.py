from table_creating import table


class table_data_edit(table):
    def data_add(self, columns, values):
        query = '''
                INSERT INTO Students (?)
                VALUES (?)
                '''
        self._table_open(query, (columns, values,))

    def data_edit(self, column: str, value: str):
        query = '''
                UPDATE Students
                SET ? = ?
                '''
        self._table_open(query, (column, value,))


    def data_delete(self, column, values):
        query = '''
                DELETE FROM Students
                WHERE ? = ?
                '''
        self._table_open(query, (column, values,))
