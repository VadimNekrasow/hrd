import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from database import Database
from forms import *

list_header_table_service = ("Ф.И.О.", "Отдел", "Должность", "Опыт работы", "Образование", "Дата начала работы", \
                             "Дата окончания работы", "Телефон")

DEBUG = True


def print_d(*element, end='\n'):
    if DEBUG:
        print(*element, end=end)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        #palette = QPalette()
        #palette.setColor(QPalette.Window, QColor(53, 53, 53))
        #palette.setColor(QPalette.WindowText, Qt.white)
        #self.setPalette(palette)

        # self.setStyleSheet("""
        #     color:white;
        #     background-color: rgb(53,53,53);
        #
        # """)

        #qApp.setStyle('window')

        self.database = Database()
        self.list_positions = []
        self.list_departments = []
        self.count_tab_FTP = 0

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.form_login = FormLogin()
        self.form_main_page = MainPage()
        self.form_main_page.link_add_employee.linkActivated.connect(self.new_tab_add_employee)
        self.form_main_page.link_position.linkActivated.connect(self.new_tab_positions)
        self.form_main_page.link_add_postion.linkActivated.connect(self.new_tab_add_positions)
        self.form_main_page.link_add_department.linkActivated.connect(self.new_tab_add_department)
        self.form_add_employee = FormAddEmployee()

        self.tab_widget = QTabWidget()
        self.tab_widget.setMovable(True)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.tab_widget.currentChanged.connect(self.change_current_tab)
        self.tab_widget.addTab(self.form_main_page, 'Главная страница')
        self.tab_bar = self.tab_widget.tabBar()
        self.tab_bar.tabButton(0, QTabBar.RightSide).resize(0, 0)

        self.central_widget.addWidget(self.form_login)
        self.central_widget.addWidget(self.tab_widget)

        self.central_widget.setCurrentIndex(1)
        self.resize(640, 480)



    def new_tab_add_employee(self):
        form = FormAddEmployee()
        form.button_save.clicked.connect(self.save_new_employee)
        form.button_add_department.clicked.connect(self.new_tab_add_department)
        form.button_add_position.clicked.connect(self.new_tab_add_positions)
        form.button_open_calendar_dialog_start.clicked.connect(self.open_calendar_dialog)
        form.button_open_calendar_dialog_birth.clicked.connect(self.open_calendar_dialog)

        # self.list_positions = self.database.get_positions()
        # self.list_departments = self.database.get_departments()

        # form.combobox_position.addItems([i[1] for i in self.list_positions])
        # form.combobox_department.addItems(i[1] for i in self.list_departments)

        index = self.tab_widget.addTab(form, "Добавить сотрудника")
        self.tab_widget.setCurrentIndex(index)

    def new_tab_add_positions(self):  # Новая вкладка. Добавление должности
        form = FormAddPosition()
        form.button_save.clicked.connect(self.save_new_position)
        index = self.tab_widget.addTab(form, "Добавить должность")
        self.tab_widget.setCurrentIndex(index)

    def new_tab_add_department(self):
        form = FormAddDepartment()
        form.button_save.clicked.connect(self.save_new_department)
        index = self.tab_widget.addTab(form, "Добавить отдел")
        self.tab_widget.setCurrentIndex(index)

    def new_tab_positions(self):  # Новая вкладка. Таблица должности
        form = FormTablePositions()
        form.tool_bar.action_edit.triggered.connect(self.open_dialog_edit_position)
        form.tool_bar.action_add.triggered.connect(self.new_tab_add_positions)
        form.tool_bar.action_del.triggered.connect(self.delete_position)
        index = self.tab_widget.addTab(form, "Должности")
        self.tab_widget.setCurrentIndex(index)

    def new_tab_table_departments(self):
        # form = FormTa
        pass

    def open_dialog_edit_position(self, form: FormTablePositions = None):
        form = self.tab_widget.currentWidget()
        index = form.table_position.currentRow()
        dialog = EditPositionDialog(self.list_positions[index][1], self.list_positions[index][2])

        if dialog.exec() == QDialog.Accepted:
            position = dialog.return_position()
            about = dialog.return_about()
            id = self.list_positions[index][0]
            if self.database.change_position(id, position, about):
                self.show_message_box("Редактирование должности", "Запись успешно обновлена", QMessageBox.Information)
                self.reboot_table_positions(form)
            else:
                self.show_message_box("Редактирование должности", "Должность '{}' не обновлена".format(position),
                                      QMessageBox.Warning)

    def reboot_table_positions(self, form: FormTablePositions):  # Обновляет данные в таблице Должности
        print_d('reboot_table_positions(self, form: FormTablePositions)')
        form.table_position.setRowCount(0)
        self.list_positions = self.database.get_positions()
        for line in self.list_positions:
            form.table_position.setRowCount(form.table_position.rowCount() + 1)
            row_count = form.table_position.rowCount()
            form.table_position.setItem(row_count - 1, 0, QTableWidgetItem(str(line[0])))
            form.table_position.setItem(row_count - 1, 1, QTableWidgetItem(str(line[1])))
            form.table_position.setItem(row_count - 1, 2, QTableWidgetItem(str(line[2])))
        form.table_position.resizeColumnsToContents()

    def reboot_form_add_employee(self, form: FormAddEmployee):
        print_d('reboot_form_add_employee(self, form: FormAddEmployee)')
        self.list_positions = self.database.get_positions()
        self.list_departments = self.database.get_departments()
        form.combobox_position.clear()
        form.combobox_department.clear()
        form.combobox_position.addItems([i[1] for i in self.list_positions])
        form.combobox_department.addItems(i[1] for i in self.list_departments)

    def save_new_employee(self, form: FormAddEmployee = None):  # Сохраняет нового работника
        form = self.tab_widget.currentWidget()
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
        form.clear()

    def save_new_position(self, form: FormAddPosition = None):
        form = self.tab_widget.currentWidget()
        position = form.edit_name.text()
        about = form.edit_about.toPlainText()

        if not position:
            self.show_message_box("Внимание", "Заполните поле 'Должность'", QMessageBox.Warning)
            return

        state = self.database.new_position(position, about)
        if state:
            self.show_message_box("Добавление должности", "Должность '{}' добавлена".format(position),
                                  QMessageBox.Information)
            form.clear()
        else:
            self.show_message_box("Ошибка. Добавление должности", "Произошла ошибка", QMessageBox.Warning)

    def save_new_department(self, form: FormAddDepartment = None):
        form = self.tab_widget.currentWidget()
        department = form.edit_department.text()
        chief = form.edit_chief.text() if form.edit_chief.text() else None
        phone = form.edit_phone.text() if form.edit_phone.text() else None

        if not department:
            self.show_message_box("Внимание", "Заполните обязательные поля", QMessageBox.Warning)
            return

        state = self.database.new_department(department, chief, phone)
        if state:
            self.show_message_box("Добавление отдела", "Отдел '{}' добавлен".format(department),
                                  QMessageBox.Information)
            form.clear()
        else:
            self.show_message_box("Ошибка. Добавление отдела", "Произошла ошибка", QMessageBox.Warning)

    def change_current_tab(self, index):
        form = self.tab_widget.widget(index)
        if form.form_id == FormID.FTP:
            print_d('reboot FTP', form.form_id)
            self.reboot_table_positions(form)
        elif form.form_id == FormID.FAE:
            print_d('reboot FAE', form.form_id)
            self.reboot_form_add_employee(form)

    def delete_position(self, form: FormTablePositions = None):
        form = self.tab_widget.currentWidget()
        id = self.list_positions[form.table_position.currentRow()][0]
        title = self.list_positions[form.table_position.currentRow()][1]

        if not self.question_delete_message("Удаление '{}'".format(title),
                                            "Подтвердите действие. \nОтменить удаление будет невозможно"):
            return

        state = self.database.delete_position(id)

        if state:
            self.show_message_box("Удаление '{}'".format(title), "Дожность '{}' удалена".format(title),
                                  QMessageBox.Information)
            self.reboot_table_positions(form)
        else:
            self.show_message_box("Ошибка", "Дожность '{}' не была удалена".format(title),
                                  QMessageBox.Information)

    def close_tab(self, index):
        form = self.tab_widget.widget(index)
        form.close()
        self.tab_widget.removeTab(index)

    def show_message_box(self, title, body, type):
        QMessageBox(type, title, body, QMessageBox.Ok).exec()

    def question_delete_message(self, title, body):
        reply = QMessageBox.question(self, title, body, QMessageBox.Yes | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            return True
        else:
            return False

    def open_calendar_dialog(self):
        form = self.tab_widget.currentWidget()
        dialog = CalendarDialog(self)
        if dialog.exec() == QDialog.Accepted:
            object_name = self.sender().objectName()
            date = dialog.get_date()
            if object_name == 'start':
                form.edit_start_date.setDate(date)
            else:
                form.edit_birth.setDate(date)


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    window = Window()
    window.show()
    sys.exit(app.exec())
