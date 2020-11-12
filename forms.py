from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTranslator
from PyQt5.QtGui import *

list_header_table_service = ("Ф.И.О.", "Отдел", "Должность", "Опыт работы", "Образование", "Дата начала работы",
                             "Дата окончания работы", "Телефон")


class FormID:
    FAP: int = 1  ##Form Add Position
    FAE: int = 2  ##Form Add Employee
    FAD: int = 3  ##Form Add Department
    FMP: int = 4  ##Form Main Page
    FTP: int = 5  ##Form Table Position
    FTD: int = 6  ##Form Table Department


class FormIdMixin:
    form_id = None

    def get_form_id(self):
        return self.form_id


class FormAddPosition(QWidget, FormIdMixin):
    """Форма добавления должности"""

    def __init__(self):
        super().__init__()
        self.form_id = FormID.FAP
        self.setAttribute(Qt.WA_DeleteOnClose)
        main_layout_vbox = QVBoxLayout(self)

        self.edit_name = QLineEdit()
        self.edit_about = QTextEdit()

        form_layout = QFormLayout()
        form_layout.addRow("Должность <span style='color: red;'>*</span>", self.edit_name)
        form_layout.addRow("Описание", self.edit_about)

        self.button_save = QPushButton("Сохранить")
        self.button_cancel = QPushButton("Отмена")
        hbox_button = QHBoxLayout()
        hbox_button.addStretch(1)
        hbox_button.addWidget(self.button_save)
        hbox_button.addWidget(self.button_cancel)

        main_layout_vbox.addLayout(form_layout)
        main_layout_vbox.addWidget(QLabel("<span style='color: red;'>*</span> – поля, обязательные к заполнению"))
        main_layout_vbox.addStretch(1)
        main_layout_vbox.addLayout(hbox_button)

    def clear(self):
        self.edit_name.clear()
        self.edit_about.clear()


class FormAddDepartment(QWidget, FormIdMixin):
    """Форма добавления отделов"""

    def __init__(self):
        super().__init__()
        self.form_id = FormID.FAD
        self.setAttribute(Qt.WA_DeleteOnClose)
        main_layout_vbox = QVBoxLayout(self)
        self.edit_department = QLineEdit()
        self.edit_chief = QLineEdit()
        self.edit_phone = QLineEdit()

        form_layout = QFormLayout()
        form_layout.addRow("Отдел <span style='color: red;'>*</span>", self.edit_department)
        form_layout.addRow("Начальник", self.edit_chief)
        form_layout.addRow("Телефон", self.edit_phone)

        self.button_save = QPushButton("Сохранить")
        self.button_cancel = QPushButton("Отмена")
        hbox_button = QHBoxLayout()
        hbox_button.addStretch(1)
        hbox_button.addWidget(self.button_save)
        hbox_button.addWidget(self.button_cancel)

        main_layout_vbox.addLayout(form_layout)
        main_layout_vbox.addWidget(QLabel("<span style='color: red;'>*</span> – поля, обязательные к заполнению"))
        main_layout_vbox.addStretch(1)
        main_layout_vbox.addLayout(hbox_button)

    def clear(self):
        self.edit_department.clear()
        self.edit_chief.clear()
        self.edit_phone.clear()


class FormTest(QWidget, FormIdMixin):
    """Форма добавления работников"""

    def __init__(self):
        super().__init__()
        self.form_id = FormID.FAE
        self.setAttribute(Qt.WA_DeleteOnClose)
        main_layout_vbox = QVBoxLayout(self)

        self.edit_name = QLineEdit()
        self.edit_birth = QDateEdit()
        self.edit_passport = QLineEdit()
        self.edit_passport.setInputMask("99 99 999999;_")
        self.edit_phone = QLineEdit()
        self.edit_phone.setInputMask("+7 (999) 999-99-99;_")
        self.edit_start_date = QDateEdit()
        self.edit_education = QLineEdit()

        form_layout = QFormLayout()
        form_layout.addRow("Ф.И.О", self.edit_name)
        form_layout.addRow("Дата рождения", self.edit_birth)
        form_layout.addRow("Паспорт", self.edit_passport)
        form_layout.addRow("Телефон", self.edit_phone)
        form_layout.addRow("Дата принятия на работу", self.edit_start_date)
        form_layout.addRow("Образование", self.edit_education)



        self.button_save = QPushButton("Сохранить")
        self.button_cancel = QPushButton("Отмена")
        hbox_button = QHBoxLayout()
        hbox_button.addStretch(1)
        hbox_button.addWidget(self.button_save)
        hbox_button.addWidget(self.button_cancel)

        group_information = QGroupBox("Личные данные")
        group_information.setLayout(form_layout)


        vbox_button_post = QVBoxLayout()
        button_new = QPushButton("+")
        button_new.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.button_del = QPushButton("X")
        self.button_del.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        vbox_button_post.addWidget(button_new)
        vbox_button_post.addWidget(self.button_del)
        vbox_button_post.addStretch(1)

        self.table_post = QTableWidget()
        self.table_post.setColumnCount(2)
        self.table_post.verticalHeader().setVisible(False)
        self.table_post.setRowCount(1)

        hbox_post = QHBoxLayout()
        hbox_post.addLayout(vbox_button_post, 1)
        hbox_post.addWidget(self.table_post, 3)

        group_post = QGroupBox()
        group_post.setLayout(hbox_post)

        main_layout_vbox.addWidget(group_information)
        main_layout_vbox.addWidget(QLabel("<span style='color: red;'>*</span> – поля, обязательные к заполнению"))
        main_layout_vbox.addWidget(group_post)
        main_layout_vbox.addLayout(hbox_button)
        main_layout_vbox.addStretch(1)


class FormAddEmployee(QWidget, FormIdMixin):
    """Форма добавления работников"""

    def __init__(self):
        super().__init__()
        self.form_id = FormID.FAE
        self.setAttribute(Qt.WA_DeleteOnClose)
        main_layout_vbox = QVBoxLayout(self)
        # main_layout_vbox.setContentsMargins(0, 0, 0, 0)
        self.edit_name = QLineEdit()
        self.combobox_department = QComboBox()
        self.button_add_department = ButtonIcon('icons/new.ico')
        self.combobox_position = QComboBox()
        self.button_add_position = ButtonIcon('icons/new.ico')
        self.edit_experience = QSpinBox()
        self.edit_education = QLineEdit()
        self.edit_start_date = QDateEdit()
        self.button_open_calendar_dialog_start = ButtonIcon('icons/calendar.ico')
        self.button_open_calendar_dialog_start.setObjectName("start")
        self.edit_end_date = QDateEdit()
        self.edit_phone = QLineEdit()
        self.edit_phone.setInputMask("+7 (999) 999-99-99;_")

        hbox_line_position = QHBoxLayout()
        hbox_line_position.addWidget(self.combobox_position, 1)
        hbox_line_position.addWidget(self.button_add_position, 0)
        hbox_line_position.setSpacing(1)

        hbox_line_department = QHBoxLayout()
        hbox_line_department.addWidget(self.combobox_department, 1)
        hbox_line_department.addWidget(self.button_add_department, 0)
        hbox_line_department.setSpacing(1)

        hbox_line_start_date = QHBoxLayout()
        hbox_line_start_date.setSpacing(0)
        hbox_line_start_date.addWidget(self.edit_start_date, 1)
        hbox_line_start_date.addWidget(self.button_open_calendar_dialog_start, 0)

        form_layout_service = QFormLayout()
        form_layout_service.addRow("Имя <span style='color: red;'>*</span>", self.edit_name)
        form_layout_service.addRow("Отдел <span style='color: red;'>*</span>", hbox_line_department)
        form_layout_service.addRow("Должность <span style='color: red;'>*</span>", hbox_line_position)
        form_layout_service.addRow("Опыт работы <span style='color: red;'>*</span>", self.edit_experience)
        form_layout_service.addRow("Образование <span style='color: red;'>*</span>", self.edit_education)
        form_layout_service.addRow("Дата начала работы <span style='color: red;'>*</span>", hbox_line_start_date)
        # form_layout_service.addRow("Дата завершения работы", self.edit_end_date)
        form_layout_service.addRow("Номер телефона <span style='color: red;'>*</span>", self.edit_phone)

        self.edit_birth = QDateEdit()
        self.button_open_calendar_dialog_birth = ButtonIcon('icons/calendar.ico')
        self.button_open_calendar_dialog_birth.setObjectName('birth')
        self.edit_passport = QLineEdit()
        self.edit_passport.setInputMask("99 99 999999;_")
        self.edit_address = QLineEdit()
        self.edit_registration_address = QLineEdit()

        hbox_line_birth = QHBoxLayout()
        hbox_line_birth.setSpacing(0)
        hbox_line_birth.addWidget(self.edit_birth, 1)
        hbox_line_birth.addWidget(self.button_open_calendar_dialog_birth, 0)

        form_layout_personal = QFormLayout()
        form_layout_personal.addRow("Дата рождения", hbox_line_birth)
        form_layout_personal.addRow("Номер паспорта", self.edit_passport)
        form_layout_personal.addRow("Адрес проживания", self.edit_address)
        form_layout_personal.addRow("Адрес регистрации", self.edit_registration_address)

        self.button_save = QPushButton("Сохранить")
        self.button_cancel = QPushButton("Отмена")
        hbox_button = QHBoxLayout()
        hbox_button.addStretch(1)
        hbox_button.addWidget(self.button_save)
        hbox_button.addWidget(self.button_cancel)

        group_service_information = QGroupBox("Служебная информация")
        group_service_information.setLayout(form_layout_service)

        group_personal_information = QGroupBox("Личная информация")
        group_personal_information.setLayout(form_layout_personal)

        main_layout_vbox.addWidget(group_service_information)
        main_layout_vbox.addWidget(QLabel("<span style='color: red;'>*</span> – поля, обязательные к заполнению"))
        main_layout_vbox.addWidget(group_personal_information)
        main_layout_vbox.addLayout(hbox_button)
        main_layout_vbox.addStretch(1)

    def clear(self):
        self.edit_name.clear()
        self.combobox_department.setCurrentIndex(0)
        self.combobox_position.setCurrentIndex(0)
        self.edit_experience.clear()
        self.edit_education.clear()
        self.edit_start_date.clear()
        self.edit_phone.clear()

        self.edit_birth.clear()
        self.edit_passport.clear()
        self.edit_address.clear()
        self.edit_registration_address.clear()


class FormLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        vboxLogin = QVBoxLayout(self)
        self.editLogin = QLineEdit()
        self.editLogin.setMinimumWidth(150)
        self.editLogin.setPlaceholderText("Логин")
        self.editPassword = QLineEdit()
        self.editPassword.setMinimumWidth(150)
        self.editPassword.setPlaceholderText("Пароль")
        self.editPassword.setEchoMode(QLineEdit.Password)
        self.buttonLogin = QPushButton("Вход")
        self.buttonLogin.setMinimumWidth(150)
        self.checkBox = QCheckBox("Запомнить меня")
        self.labelErrorAboutLogin = QLabel("Неверный логин или пароль\n")
        self.labelErrorAboutLogin.setAlignment(Qt.AlignHCenter)
        self.labelErrorAboutLogin.setStyleSheet("color: red;")
        self.labelErrorAboutLogin.setVisible(False)
        vboxLogin.addStretch(5)
        vboxLogin.addWidget(self.editLogin, 0, Qt.AlignCenter)
        vboxLogin.addWidget(self.editPassword, 0, Qt.AlignCenter)
        vboxLogin.addWidget(self.buttonLogin, 0, Qt.AlignCenter)
        vboxLogin.addWidget(self.checkBox, 0, Qt.AlignCenter)
        vboxLogin.addWidget(self.labelErrorAboutLogin, 0, Qt.AlignCenter)
        vboxLogin.addStretch(5)


class MainPage(QWidget, FormIdMixin):
    def __init__(self):
        super().__init__()

        self.form_id = FormID.FMP
        self.setAttribute(Qt.WA_DeleteOnClose)

        vbox_main = QVBoxLayout(self)
        vbox_main.setContentsMargins(1, 1, 1, 1)

        self.link_service_information = QLabel("<a href='#' >Сотрудники. Служебная информация</a>")
        self.link_add_employee = QLabel("<a href='#' >Добавить сотрудника</a>")
        self.link_personal_information = QLabel("<a href='#' >Сотрудники. Личная информация</a>")
        self.link_department = QLabel("<a href='#' >Отделы</a>")
        self.link_add_department = QLabel("<a href='#' >Добавить отдел</a>")
        self.link_position = QLabel("<a href='#' >Должности</a>")
        self.link_add_postion = QLabel("<a href='#' >Добавить должность</a>")

        vbox_main.setSpacing(10)
        vbox_main.addWidget(self.link_service_information)
        vbox_main.addWidget(self.link_add_employee)
        vbox_main.addWidget(self.link_personal_information)
        vbox_main.addWidget(self.link_department)
        vbox_main.addWidget(self.link_add_department)
        vbox_main.addWidget(self.link_position)
        vbox_main.addWidget(self.link_add_postion)
        vbox_main.addStretch(1)

        # grid_main.addWidget(self.link_service_information, 0, 0)
        # grid_main.addWidget(self.link_add_employee, 0, 1, Qt.AlignLeft)
        # grid_main.addWidget(self.link_personal_information, 1, 0)
        # grid_main.addWidget(self.link_department, 2, 0)
        # grid_main.addWidget(self.link_add_department, 2, 1, Qt.AlignLeft)
        # grid_main.addWidget(self.link_position, 3, 0)
        # grid_main.addWidget(self.link_add_postion, 3, 1, Qt.AlignLeft)

        # vbox_main.setSpacing()


class FormTableService(QWidget, FormIdMixin):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        main_vbox = QVBoxLayout(self)
        self.table_service = QTableWidget()
        self.table_service.setColumnCount(len(list_header_table_service))
        self.table_service.setHorizontalHeaderLabels(list_header_table_service)
        main_vbox.addWidget(self.table_service)


class VToolBar(QToolBar):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.action_add = self.addAction("Создать")
        self.action_add.setIcon(QIcon("icons/add.ico"))
        self.action_edit = self.addAction("Редактировать")
        self.action_edit.setIcon(QIcon("icons/edit.ico"))
        self.action_edit.setDisabled(True)
        self.action_del = self.addAction("Удалить")
        self.action_del.setIcon(QIcon("icons/del.ico"))
        self.action_del.setDisabled(True)
        self.setFloatable(True)


class FormTablePositions(QWidget, FormIdMixin):
    def __init__(self):
        super().__init__()
        self.form_id = FormID.FTP
        self.setAttribute(Qt.WA_DeleteOnClose)
        vbox_main = QVBoxLayout(self)
        self.tool_bar = VToolBar()
        self.table_position = QTableWidget()
        self.table_position.setColumnCount(3)
        self.table_position.setHorizontalHeaderLabels(("Код должности", "Должность", "Описание"))
        self.table_position.itemSelectionChanged.connect(self.change_state_actions)
        self.table_position.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.table_position.setSortingEnabled(True)

        vbox_main.addWidget(self.tool_bar)
        vbox_main.addWidget(self.table_position)

    def change_state_actions(self, row=None, col=None):
        if self.table_position.selectedItems():
            self.tool_bar.action_del.setDisabled(False)
            self.tool_bar.action_edit.setDisabled(False)
        else:
            self.tool_bar.action_del.setDisabled(True)
            self.tool_bar.action_edit.setDisabled(True)


class FormTableDepartments(QWidget, FormIdMixin):
    def __init__(self):
        super().__init__()
        self.form_id = FormID.FTD
        self.tool_bar = VToolBar()
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Код отдела", "Отдел", "Начальник", "Телефон"))
        self.table.itemSelectionChanged.connect(self.change_state_actions)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.tool_bar)
        vbox.addWidget(self.table)

    def change_state_actions(self, row=None, col=None):
        if self.table.selectedItems():
            self.tool_bar.action_del.setDisabled(False)
            self.tool_bar.action_edit.setDisabled(False)
        else:
            self.tool_bar.action_del.setDisabled(True)
            self.tool_bar.action_edit.setDisabled(True)


class EditPositionDialog(QDialog):
    def __init__(self, position=None, about=None):
        super().__init__()
        self.setWindowTitle("Редактирование '{}'".format(position))
        vbox = QVBoxLayout(self)
        self.form = FormAddPosition()
        self.form.edit_name.setText(position)
        self.form.edit_about.setText(about)
        self.form.button_save.clicked.connect(self.click_button_save)
        self.form.button_cancel.clicked.connect(self.reject)
        vbox.addWidget(self.form)

    def click_button_save(self):
        if self.return_position():
            self.accept()
        else:
            self.form.edit_name.setFocus()

    def return_position(self):
        return self.form.edit_name.text()

    def return_about(self):
        return self.form.edit_about.toPlainText()


class EditDepartmentDialog(QDialog):
    def __init__(self, department=None, chief=None, phone=None):
        super().__init__()
        self.setWindowTitle("Редактирование '{}'".format(department))
        self.form = FormAddDepartment()
        self.form.edit_department.setText(department)
        self.form.edit_chief.setText(chief)
        self.form.edit_phone.setText(phone)

    def click_button_save(self):
        if self.get_department():
            self.accept()
        else:
            self.form.edit_department.setFocus()

    def get_department(self):
        return self.form.edit_department.text()

    def get_chief(self):
        return self.form.edit_chief.text()

    def get_phone(self):
        return self.form.edit_phone.text()


class ButtonIcon(QPushButton):
    def __init__(self, icon_path, text='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setIcon(QIcon(icon_path))
        self.setText(text)
        self.setFlat(True)
        self.setCursor(QCursor(Qt.PointingHandCursor))


class CalendarDialog(QDialog):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.setWindowTitle("Выберите дату")
        vbox = QVBoxLayout(self)
        self.calendar = QCalendarWidget()
        button_save = QPushButton("Ок")
        button_save.clicked.connect(self.accept)
        button_cancel = QPushButton('Отмена')
        button_cancel.clicked.connect(self.reject)
        vbox.addWidget(self.calendar)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(button_save)
        hbox.addWidget(button_cancel)
        vbox.addLayout(hbox)

    def get_date(self):
        return self.calendar.selectedDate()
