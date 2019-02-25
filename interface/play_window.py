"""

Самое сложное окно всей программы. Здесь происходит вся игра.

"""
from collections import OrderedDict
from interface import settings
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QPushButton, QListWidget
from PyQt5.QtCore import QTimer

class Play_Window(QWidget):
    def __init__(self):
        super().__init__()

        #Создадим все необходимые виджеты

        """      Clock_Timer главный виджет игры
                 Он отображает все игровые события и управляет ими.
                 Ограничивает время игроков и делает еще массу полезных штук                               
                                                
                                                """
        self.player_list = QListWidget()
        self.master_choose = OrderedDict([(QPushButton("Следующий игрок"),"next_player"), (QPushButton("Прудыдущий игрок"),"prev_player")])
        self.player_control = OrderedDict([(QPushButton("Заголосован"), "voted"), (QPushButton("Отстрелян"), "shooted"), (QPushButton("Удален"), "deleted"), (QPushButton("Вернуть игрока"), "return")])
        self.master_role = OrderedDict([(QPushButton("Начначить гражданина"), "citizen"), (QPushButton("Начначить мафиози"), "mafia"), (QPushButton("Начначить шерифа"), "sherif"), (QPushButton("Начначить дона"), "don")])
        self.settings = OrderedDict( [(QPushButton("Скрыть цвета"), "hide"), (QPushButton("Включить голос на острел мафии"), "vote_voice"), (QPushButton("Включить остальные игровые звуки"), "sound")] )


        #Настроим их
        self.customise2()




    def customise(self):
        """    Метод расставляет виджеты для работы    """
        pass

        # Настроим разрешение и положение окна
        self.resize(settings.PLAY_WINDOW_WIDTH, settings.PLAY_WINDOW_HEIGHT)
        self.move_to_center()

        #Создадим главный слой. Он разделит окно на две части по горзонтали
        main_layout = QHBoxLayout(self)

        """
        
        Расстановка верхней части окна
        
        """
        top_frame = QFrame()
        top_layout = QVBoxLayout(top_frame)

        #Добавляем к main_layout
        main_layout.addWidget(top_frame)

        """
        * * * * * * * * * * * * * * *
        *      * Mast *             *
        * Play * Choo *   Vote      *
        *      *      *             *
        * * * * * * * * * * * * * * *             
        *      * Mast *             *
        *      * Role *  Hints      *
        * Play ********             *
        * Contr* Sett *             *
        * * * * * * * * * * * * * * *             
        
        """

        top_left_part_frame = QFrame()
        top_left_part_layout = QHBoxLayout(top_left_part_frame)

        #Добавляем к top_layout
        top_layout.addWidget(top_left_part_frame)   #Левая часть


        #Эти два фрейма добавим в left_part_frame. Сверху вниз.
        player_AND_master_choose_frame = QFrame()
        player_AND_master_choose_layout = QVBoxLayout(player_AND_master_choose_frame)

        top_left_part_layout.addWidget(player_AND_master_choose_frame)  #В player_AND_master_choose_frame вставляем виджеты с списком игроков и их выбором [1]

        players_frame = QFrame()
        players_layout = QHBoxLayout(players_frame)
        #И вставим фрейм c игроками в [1]
        player_AND_master_choose_layout.addWidget(players_frame)

        master_choose_frame = QFrame()
        master_choose_layout = QHBoxLayout(master_choose_frame)
        #И вставим фрейми с присвоением игрока в [1]
        player_AND_master_choose_layout.addWidget(master_choose_frame)



        #Теперь разберемся с управлением игроком и еще одним горизонтальным слоем (MASTER ROLE и Settings)
        player_control_with_master_role_and_setting_frame = QFrame()
        player_control_with_master_role_and_setting_layout = QVBoxLayout(player_control_with_master_role_and_setting_frame)

        #Вставляем в него фрейм с контролем игроков
        player_control_frame = QFrame()
        player_control_layout = QHBoxLayout(player_control_frame)

        player_control_with_master_role_and_setting_layout.addWidget(player_control_frame)

        #И вставим в него слой с фреймами выбора ролей и настроек
        master_role_and_setting_frame = QFrame()
        master_role_and_setting_layout = QHBoxLayout(master_role_and_setting_frame)

        #Но перед вставкой добавим в вставляемый слой еще фреймы
        master_role_frame = QFrame()
        master_role_layout = QHBoxLayout(master_role_frame)
        settings_frame = QFrame()
        settings_layout = QHBoxLayout(settings_frame)

        master_role_and_setting_layout.addWidget(master_role_frame)
        master_role_and_setting_layout.addWidget(settings_frame)

        #И наконец вставим разбитый еще на 2 слой
        top_left_part_layout.addWidget(player_control_with_master_role_and_setting_frame)


        #Теперь вставим виджеы в верхнюю левую часть окна
        players_layout.addWidget(self.player_list)

        for btn in self.master_choose:
            master_choose_layout.addWidget(btn)

        for btn in self.player_control:
            player_control_layout.addWidget(btn)    #Не работает

    def customise2(self):
        # Настроим разрешение и положение окна
        self.resize(settings.PLAY_WINDOW_WIDTH, settings.PLAY_WINDOW_HEIGHT)
        self.move_to_center()

        #Начнем с левой части окна, виджеты будем вставлять по часовой стрелке рекурсионно(от малого к большему)
        player_control_frame = QFrame(self)
        player_control = QVBoxLayout(player_control_frame)

        player_control.addWidget(self.player_list)

        for btn in self.player_control:
            player_control.addWidget(btn)

        #Делаем слой выше, чтобы вставить в него то что уже имеем выше плюс что-то новое
        first_top_frame = QFrame(self)
        first_top = QHBoxLayout(first_top_frame)
        self.setLayout(first_top)

        #Вставляем что получили выше
        first_top.addWidget(player_control_frame)

        #Теперь разметим новое место для следующих виджетов
        role_control_frame = QFrame(self)
        role_control = QVBoxLayout(role_control_frame)

        for btn in self.master_choose:
            role_control.addWidget(btn)

        #И вставляем что-то новое
        first_top.addWidget(role_control_frame)









        

    def sayHello(self):
        print("Hello world!")









    def move_to_center(self):
        """   Метод переносит окошко в центр  """
        form = self.frameGeometry()
        window_center = QDesktopWidget().availableGeometry().center()
        form.moveCenter(window_center)
        self.move(form.topLeft())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Play_Window()
    window.show()
    sys.exit(app.exec_())