"""


Окно start_window запрашивает у пользователя имя игрового вечера, его дату, и может быть что-нибудь еще, посмотрим.


"""

import sys
from interface import settings
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication, QDateTimeEdit, QDesktopWidget, QGridLayout, QLabel, QFrame, QHBoxLayout, QVBoxLayout)

from PyQt5.QtCore import QDate, QTime, QDateTime


class Start_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(settings.START_WINDOW_WIDTH, settings.START_WINDOW_HEIGHT) #Устанавливаем размер окна

        self.work_frame = QFrame(self)

        self.create_evening_game_button = QPushButton("Создать игровой вечер")
        self.date_edit = QDateTimeEdit()
        self.ask_date_label = QLabel("Введите дату игрового вечера")

        self.customise()

    def move_to_center(self):
        # Перенесем окошко в центр
        form_rectangle = self.frameGeometry()
        window_center = QDesktopWidget().availableGeometry().center()
        form_rectangle.moveCenter(window_center)
        self.move(form_rectangle.topLeft())

    def customise(self):
        """Метод настраивает виджеты для работы"""
        self.setWindowTitle("Mafia-Driver") #Название программы
        self.work_frame.setFrameStyle(QFrame.Box)

        self.move_to_center()

        #Внесем текущую дату с компьютера
        now_date = QDate.currentDate()
        now_time = QTime.currentTime()

        self.date_edit.setDate(now_date)
        self.date_edit.setTime(now_time)


        #Перенесем фрейм в центр
        form_horizontalLayout = QHBoxLayout(self)
        form_horizontalLayout.setContentsMargins(settings.START_WINDOW_SHIFT, settings.START_WINDOW_SHIFT, settings.START_WINDOW_SHIFT ,settings.START_WINDOW_SHIFT)

        form_horizontalLayout.addWidget(self.work_frame)


        #Настроим макет и виджеты внутри фрейма
        work_frame_horizontallLayout = QHBoxLayout()
        work_frame_veritcallLayout = QVBoxLayout(self.work_frame)

        work_frame_horizontallLayout.addWidget(self.date_edit)
        work_frame_horizontallLayout.addWidget(self.ask_date_label)

        work_frame_veritcallLayout.addLayout(work_frame_horizontallLayout)
        work_frame_veritcallLayout.addWidget(self.create_evening_game_button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    obj = Start_Window()
    obj.show()
    sys.exit(app.exec_())