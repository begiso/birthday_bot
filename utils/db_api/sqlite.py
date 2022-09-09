import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    def create_table_birthdays(self2):
        sql2 = """
        CREATE TABLE Birthdays (
            name_f varchar(255) NOT NULL,
            year_b int(4) NOT NULL,
            month_b int(2) NOT NULL,
            day_b int(2) NOT NULL,
            id int NOT NULL
            );
"""
        self2.execute(sql2, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name) VALUES(1, 'John')"

        sql = """
        INSERT INTO Users(id, Name) VALUES(?, ?)
        """
        self.execute(sql, parameters=(id, name), commit=True)

    def add_birthday(self, name_f: str, year_b: int, month_b: int, day_b: int, id: int):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name) VALUES(1, 'John')"

        sql = """
        INSERT INTO Birthdays(name_f, day_b, month_b, year_b, id) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(name_f, day_b, month_b, year_b, id), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_all_birthdays(self):

        sql = """
        SELECT * FROM Birthdays
        """

        return self.execute(sql, fetchall=True)

    def select_user_birthday_by_date(self, day, month):

        sql = f"""
                SELECT name_f, year_b, id FROM Birthdays Where day_b={day} AND month_b={month}
        """

        return self.execute(sql, fetchall=True)


    def select_user_birthday(self, id):

        sql = f"""
        SELECT name_f, day_b, month_b, year_b FROM Birthdays Where id={id}
        """

        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)
        self.execute("DELETE FROM Birthdays WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
