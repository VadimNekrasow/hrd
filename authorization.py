import sqlite3


class NoDataError(Exception):
    pass


class Login:
    __login = None
    __password = None
    __right = None
    __connect: sqlite3.Connection = None
    __cursor: sqlite3.Cursor = None
    __table: str = None
    is_login = False

    def __init__(self, *args):
        try:
            self.__login = args[0]
            self.__password = args[1]

        except IndexError as error:
            print("Login.__init__()", error)

    def authorization(self):
        if not all([self.__login, self.__password, self.__connect, self.__table]):
            raise NoDataError("Perhaps one of the fields (login, password, connection, table) is not specified")

        try:
            self.__cursor.execute("SELECT * FROM {} WHERE Login = ? AND Password = ?".format(self.__table),
                                  (self.__login, self.__password))
            self.__connect.commit()
        except sqlite3.Error as error:
            print("Login.authorization()", error)
        else:
            data = self.__cursor.fetchone()
            if self.__password == data[2]:
                self.is_login = False
            return self.is_login

    def set_table(self, table: str):
        self.__table = table

    def set_connect(self, connect: sqlite3.Connection):
        self.__connect = connect
        self.__cursor = connect.cursor()

    def set_password(self, password: str):
        self.__password = password

    def set_login(self, login: str):
        self.__login = login

    def get_status_auth(self):

        return self.is_login


connect = sqlite3.connect("hrd_database.db")

a = Login("user", "1111")
a.set_connect(connect)
#a.set_table("authorization")
a.authorization()
raise IndexError(123)
