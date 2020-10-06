from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

from datetime import datetime

list_header_table_service = ("Ф.И.О.", "Отдел", "Должность", "Опыт работы", "Образование", "Дата начала работы",
                             "Дата окончания работы", "Телефон")


class FormAddPosition(QWidget):
    """Форма добавления должности"""

    def __init__(self):
        super().__init__()
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


class FormAddDepartment(QWidget):
    """Форма добавления отделов"""

    def __init__(self):
        super().__init__()
        main_layout_vbox = QVBoxLayout(self)
        self.edit_department = QLineEdit()
        self.combobox_chief = QComboBox()
        self.edit_phone = QLineEdit()

        form_layout = QFormLayout()
        form_layout.addRow("Отдел <span style='color: red;'>*</span>", self.edit_department)
        form_layout.addRow("Начальник <span style='color: red;'>*</span>", self.combobox_chief)
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


class FormAddEmployee(QWidget):
    """Форма добавления работников"""

    def __init__(self):
        super().__init__()

        # widget = QWidget()
        main_layout_vbox = QVBoxLayout(self)
        # main_layout_vbox.setContentsMargins(0, 0, 0, 0)
        self.edit_name = QLineEdit()
        self.combobox_department = QComboBox()
        self.combobox_position = QComboBox()
        self.edit_experience = QSpinBox()
        self.edit_education = QLineEdit()
        self.edit_start_date = QDateEdit()
        self.edit_end_date = QDateEdit()
        self.edit_phone = QLineEdit()
        self.edit_phone.setInputMask("+7 (999) 999-99-99;_")

        form_layout_service = QFormLayout()
        form_layout_service.addRow("Имя <span style='color: red;'>*</span>", self.edit_name)
        form_layout_service.addRow("Отдел <span style='color: red;'>*</span>", self.combobox_department)
        form_layout_service.addRow("Должность <span style='color: red;'>*</span>", self.combobox_position)
        form_layout_service.addRow("Опыт работы <span style='color: red;'>*</span>", self.edit_experience)
        form_layout_service.addRow("Образование <span style='color: red;'>*</span>", self.edit_education)
        form_layout_service.addRow("Дата начала работы <span style='color: red;'>*</span>", self.edit_start_date)
        # form_layout_service.addRow("Дата завершения работы", self.edit_end_date)
        form_layout_service.addRow("Номер телефона <span style='color: red;'>*</span>", self.edit_phone)

        self.edit_birth = QDateEdit()
        self.edit_passport = QLineEdit()
        self.edit_passport.setInputMask("99 99 999999;_")
        self.edit_address = QLineEdit()
        self.edit_registration_address = QLineEdit()

        form_layout_personal = QFormLayout()
        form_layout_personal.addRow("Дата рождения", self.edit_birth)
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

        # self.setWidget(widget)
        # self.setWidgetResizable(True)


class FormLogin(QWidget):
    def __init__(self):
        super().__init__()
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


class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        vbox_main = QVBoxLayout(self)
        vbox_main.setContentsMargins(1, 1, 1, 1)

        grid_main = QGridLayout(self)
        grid_main.setContentsMargins(1, 1, 1, 1)

        self.link_service_information = QLabel("<a href='#'>Сотрудники. Служебная информация</a>")
        self.link_add_employee = QLabel("<a href='#'>Добавить сотрудника</a>")
        self.link_personal_information = QLabel("<a href='#'>Сотрудники. Личная информация</a>")
        self.link_department = QLabel("<a href='#'>Отделы</a>")
        self.link_add_department = QLabel("<a href='#'>Добавить отдел</a>")
        self.link_position = QLabel("<a href='#'>Должности</a>")
        self.link_add_postion = QLabel("<a href='#'>Добавить должность</a>")

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


class PageTableService(QWidget):
    def __init__(self):
        super().__init__()
        main_vbox = QVBoxLayout(self)
        self.table_service = QTableWidget()
        self.table_service.setColumnCount(len(list_header_table_service))
        self.table_service.setHorizontalHeaderLabels(list_header_table_service)
        main_vbox.addWidget(self.table_service)


class VToolBar(QToolBar):
    def __init__(self):
        super().__init__()
        self.action_add = self.addAction("Создать")
        self.action_add.setIcon(QIcon("icons/add.ico"))
        self.action_edit = self.addAction("Редактировать")
        self.action_edit.setIcon(QIcon("icons/edit.ico"))
        self.action_edit.setDisabled(True)
        self.action_del = self.addAction("Удалить")
        self.action_del.setIcon(QIcon("icons/del.ico"))
        self.action_del.setDisabled(True)
        self.setFloatable(True)


class FormTablePositions(QWidget):
    def __init__(self):
        super().__init__()
        vbox_main = QVBoxLayout(self)

        self.tool_bar = VToolBar()
        self.table_position = QTableWidget()
        self.table_position.setColumnCount(3)
        self.table_position.setHorizontalHeaderLabels(("Код должности", "Должность", "Описание"))
        # self.table_position.setSelectionBehavior(QAbstractItemView.SelectRows)
        try:
            self.table_position.cellPressed.connect(self.change_state_actions)
        except Exception as e:
            print(e)
        self.table_position.setRowCount(1)
        self.table_position.setItem(0, 0, QTableWidgetItem("1"))
        self.table_position.setItem(0, 1, QTableWidgetItem("Директор"))

        vbox_main.addWidget(self.tool_bar)
        vbox_main.addWidget(self.table_position)

    def change_state_actions(self, row=None, col=None):
        row = self.table_position.currentRow()
        col = self.table_position.currentColumn()
        print(row, col)
        if row != -1 and col != -1:
            self.tool_bar.action_del.setDisabled(False)
            self.tool_bar.action_edit.setDisabled(False)
