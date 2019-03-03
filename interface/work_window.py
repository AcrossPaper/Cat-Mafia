import sys
from interface import settings
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication, QLabel, QFrame, QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, QDesktopWidget)
#QStringListModel

class Work_Window(QWidget):
    def __init__(self):
        super().__init__()

        self.list_players_in_room = QListWidget()
        self.list_players_in_game = QListWidget()

        self.btn_del_in_room = QPushButton("Удалить")

        self.btn_add_player_room = QPushButton("Добавить игрока")
        self.btn_add_all_players = QPushButton("Зарегестрировать всех игроков")
        self.edit_player_name = QLineEdit("")
        self.edit_player_place = QLineEdit("1")

        self.btn_del_in_game = QPushButton("Удалить")
        self.btn_shake = QPushButton("Перемешать")
        self.btn_start_game = QPushButton("Начать игру")
        self.btn_register = QPushButton("Зарегестрировать игрока")

        self.btn_swap_player = QPushButton("Переместить игрока на место")

        self.label_players_in_room = QLabel("Зарегестрированные игроки")
        self.label_players_in_game = QLabel("Игроки на следующую игру")

        self.customise()

    def move_to_center(self):
        # Перенесем окошко в центр
        form_rectangle = self.frameGeometry()
        window_center = QDesktopWidget().availableGeometry().center()
        form_rectangle.moveCenter(window_center)
        self.move(form_rectangle.topLeft())


    def customise(self):
        self.setWindowTitle("Настройка игры")
        self.resize(settings.WORK_WINDOW_WIDTH, settings.WORK_WINDOW_HEIGHT)  # Устанавливаем размер окна

        self.move_to_center()   #Перенесем окно в центр

        #Зададим начальное значение для поля добавить игрока (слева)
        self.edit_player_name.setText("Введите никнейм игрока")


        #Создадим главный слой для всего окна
        main_layer = QHBoxLayout(self)

        #Разделим окно на два слоя
        player_in_room_frame = QFrame()
        player_in_game_frame = QFrame()

        player_in_room_layer = QVBoxLayout(player_in_room_frame)
        player_in_game_layer = QVBoxLayout(player_in_game_frame)

        #Заполяем левый фрейм виджетами
        player_in_room_layer.addWidget(self.label_players_in_room)
        player_in_room_layer.addWidget(self.list_players_in_room)
        player_in_room_layer.addWidget(self.edit_player_name)
        player_in_room_layer.addWidget(self.btn_add_player_room)
        player_in_room_layer.addWidget(self.btn_del_in_room)

        # Добавим немного красоты для правой части окна, сделаем фрейм с свапом игроков местами в отдельном фрейме
        swap_frame = QFrame()
        swap_layer = QHBoxLayout(swap_frame)

        swap_layer.addWidget(self.btn_swap_player)
        swap_layer.addWidget(self.edit_player_place)

        #Заполняем правый фрейми виджетами
        player_in_game_layer.addWidget(self.label_players_in_game)
        player_in_game_layer.addWidget(self.list_players_in_game)
        player_in_game_layer.addWidget(self.btn_register)
        player_in_game_layer.addWidget(self.btn_add_all_players)
        player_in_game_layer.addWidget(self.btn_del_in_game)
        player_in_game_layer.addWidget(self.btn_shake)
        player_in_game_layer.addWidget(self.btn_start_game)

        player_in_game_layer.addWidget(swap_frame)  #Добавляем красоты


        #Соберем все вместе
        main_layer.addWidget(player_in_room_frame)
        main_layer.addWidget(player_in_game_frame)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    obj = Work_Window()
    obj.show()
    sys.exit(app.exec_())
