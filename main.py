import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from database import Database
from forms import *

list_header_table_service = ("Ф.И.О.", "Отдел", "Должность", "Опыт работы", "Образование", "Дата начала работы", \
                             "Дата окончания работы", "Телефон")


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.database = Database()
        self.list_positions = []
        self.list_departments = []

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.form_login = FormLogin()
        self.form_main_page = MainPage()
        self.form_main_page.link_add_employee.linkActivated.connect(self.new_tab_add_employee)
        self.form_main_page.link_position.linkActivated.connect(self.new_tab_positions)
        self.form_add_employee = FormAddEmployee()

        self.tab_widget = QTabWidget()
        self.tab_widget.setMovable(True)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.tab_widget.addTab(self.form_main_page, 'Главная страница')
        self.tab_bar = self.tab_widget.tabBar()
        self.tab_bar.tabButton(0, QTabBar.RightSide).resize(0, 0)

        self.central_widget.addWidget(self.form_login)
        self.central_widget.addWidget(self.tab_widget)

        self.central_widget.setCurrentIndex(1)
        self.resize(640, 480)

    def new_tab_add_employee(self):
        form = FormAddEmployee()
        form.setAttribute(Qt.WA_DeleteOnClose)
        form.button_save.clicked.connect(lambda: self.save_new_employee(form))

        self.list_positions = self.database.get_positions()
        self.list_departments = self.database.get_departments()

        form.combobox_position.addItems([i[1] for i in self.list_positions])
        form.combobox_department.addItems(i[1] for i in self.list_departments)

        index = self.tab_widget.addTab(form, "Добавить сотрудника")
        self.tab_widget.setCurrentIndex(index)

    def new_tab_positions(self):
        form = FormTablePositions()
        index = self.tab_widget.addTab(form, "Должности")
        self.tab_widget.setCurrentIndex(index)

    def save_new_employee(self, form: FormAddEmployee):
        name = form.edit_name.text()
        department = self.list_departments[form.combobox_department.currentIndex()][0]
        position = self.list_positions[form.combobox_position.currentIndex()][0]
        experience = form.edit_experience.value()
        education = form.edit_education.text()
        start_date = form.edit_start_date.text()
        phone = form.edit_phone.text()

        if not name:
            form.edit_name.setFocus()
            return

        if department == -1:
            form.combobox_department.setFocus()
            return

        if position == -1:
            form.combobox_position.setFocus()
            return

        if not education:
            form.edit_education.setFocus()
            return

        if len(phone) != 18:
            form.edit_phone.setFocus()
            return

        birth = form.edit_birth.text()
        passport = None if form.edit_passport.text().isspace() else form.edit_passport.text()
        address = form.edit_address.text() if form.edit_address.text() else None
        address_registration = form.edit_registration_address.text() if form.edit_address.text() else None

        id_emp = self.database.new_employee_service(name, department, position, experience, education,
                                                    start_date, phone)
        if id_emp:
            self.database.new_employee_personal(id_emp, birth, passport, address, address_registration)

    def reboot_form_add_employee(self, form: FormAddEmployee):
        pass

    def close_tab(self, index):
        self.tab_widget.removeTab(index)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
