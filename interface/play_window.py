from PyQt5 import uic
from PyQt5.QtWidgets import QWidget



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
            self.table_vote.setRowCount(10)
            self.table_vote.setColumnCount(2)

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

