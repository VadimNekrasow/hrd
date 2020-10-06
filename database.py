import sqlite3


class Database:
    connect = None
    cursor = None
    is_open = False

    def __init__(self):
        try:
            self.connect = sqlite3.connect('hrd_database.db')
            self.cursor = self.connect.cursor()
        except sqlite3.Error as error:
            print('Database.__init__()>>>', error)
        else:
            self.is_open = True

    def get_departments(self):
        try:
            self.cursor.execute("SELECT ID, DEPARTMENT FROM departments ORDER BY DEPARTMENT;")
            self.connect.commit()
        except sqlite3.Error as error:
            print('Database.get_departments()>>>', error)
        else:
            return self.cursor.fetchall()

    def get_positions(self):
        try:
            self.cursor.execute("SELECT ID, NAME FROM positions ORDER BY NAME;")
            self.connect.commit()
        except sqlite3.Error as error:
            print('Database.get_positions()>>>', error)
        else:
            return self.cursor.fetchall()

    def new_employee_service(self, name, id_dep, id_pos, exp, edu, start_date, phone):
        try:
            self.cursor.execute("INSERT INTO service_information (NAME, ID_DEPARTMENT, ID_POSITION, EXPERIENCE, \
            EDUCATION, START_DATE, PHONE) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, id_dep, id_pos, exp, edu, start_date,
                                                                          phone))
            self.connect.commit()
        except sqlite3.Error as error:
            print('Database.new_employee_service() commit 1>>>', error)
            return False

        try:
            self.cursor.execute("SELECT ID FROM service_information WHERE ROWID=last_insert_rowid();")
            self.connect.commit()
        except sqlite3.Error as error:
            print('Database.new_employee_service() commit 2>>>', error)
            return False
        else:
            return self.cursor.fetchone()[0]

    def new_employee_personal(self, id, birth, passport, address, reg_adr):
        try:
            self.cursor.execute("INSERT INTO personal_information (ID_EMPLOYEE, BIRTH, PASSPORT, ADDRESS, \
            REGISTRATION_ADDRESS) VALUES (?, ?, ?, ?, ?)", (id, birth, passport, address, reg_adr))
            self.connect.commit()
        except sqlite3.Error as error:
            print('Database.new_employee_personal() commit 2>>>', error)
