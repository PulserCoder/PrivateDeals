from table_creating import table


class table_caolumn_edit(table):
    def column_add(self, name_of_the_column, type_of_data):
        query = '''
                ALTER TABEL Students
                ADD ? ?
                '''
        self._table_open(query, (name_of_the_column, type_of_data,))

    def column_drop(self, name_of_the_column):
        query = '''
                ALTER TABEL Students
                DROP COLUMN ?
                '''
        self._table_open(query, (name_of_the_column,))
   