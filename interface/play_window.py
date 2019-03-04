from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QHeaderView, QTableWidgetItem

from PyQt5 import QtGui



class Play_Window(QWidget):
        def __init__(self):
            super().__init__()
            #Выводим форму на весь экран
            uic.loadUi('interface//play_window.ui', self)
            self.customise()
            #При загрузке окно автоматически открывается, скрою его
            self.hide()

        #Здесь я не стал вручную компоновать виджеты, а сделал через Designer. Так что здесь просто проведу немного космитичеких улучшений
        def customise(self):
            #перенесем окошко в центр
            form_rectangle = self.frameGeometry()
            window_center = QDesktopWidget().availableGeometry().center()
            form_rectangle.moveCenter(window_center)
            self.move(form_rectangle.topLeft())

            #Сделаем окно во весь экран
            self.showMaximized()

            #Настроим ресайз таблицы голосования


            # Настроим ресайз таблицы выбора игроков
            self.table_vote.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.table_vote.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)





        def form_player_string(self):
            #Метод отвечает за формирование строки с информацией о игроках в таблице с игроками
            pass


if __name__ == "__main__":
    #import sys
    pass
    #from PyQt5.QtWidgets import QApplication

    #app = QApplication(sys.argv)
    #window = Play_Window()
    #window.show()
    #sys.exit(app.exec_())

