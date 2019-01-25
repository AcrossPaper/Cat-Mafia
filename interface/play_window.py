"""

Самое сложное окно всей программы. Здесь происходит вся игра.

"""
from interface import settings
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QPushButton
from PyQt5.QtCore import QTimer

class Play_Window(QWidget):
    def __init__(self):
        super().__init__()

        #Создадим все необходимые виджеты

        """      Clock_Timer главный виджет игры
                 Он отображает все игровые события и управляет ими.
                 Ограничивает время игроков и делает еще массу полезных штук                               
                                                
                                                """
        self.clock_timer = QTimer()






        #Настроим их
        self.customise()




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

        left_part_frame = QFrame()
        left_part_layout = QHBoxLayout(left_part_frame)

        #Эти два фрейма добавим в left_part_frame. Сверху вниз.
        player_AND_master_choose_frame = QFrame()
        player_AND_master_choose_layout = QVBoxLayout(player_AND_master_choose_frame)

        players_control_WITH_master_role_AND_settings_frame = QFrame()
        players_control_WITH_master_role_AND_settings_layout = QVBoxLayout(player_AND_master_choose_frame)

        players_frame = QFrame()
        players_layout = QHBoxLayout(players_frame)

        players_control_frame = QFrame()
        players_control_layout = QHBoxLayout(players_control_frame)

        #К слою что выше еще сделаем деление для выбора ролей и настроек
        master_role_frame = QFrame()
        master_role_layout = QHBoxLayout(master_role_frame)

        master_settings_frame = QFrame()
        master_settings_layout = QHBoxLayout(master_settings_frame)

        master_role_AND_setting_frame = QFrame()
        master_role_AND_setting_layout = QHBoxLayout()


        #Здесь ничего делить не надо, все тривиально
        right_part_frame = QFrame()
        right_part_layout = QHBoxLayout(right_part_frame)


        vote_frame = QFrame()
        vote_layout = QHBoxLayout(vote_frame)

        hint_frame = QFrame()
        hint_layout = QHBoxLayout(hint_frame)


        #Соберем всю верхние фреймы
        left_part_layout.addWidget(player_AND_master_choose_frame)   #Игроки выбор игрока мастером
        left_part_layout.addWidget(players_control_WITH_master_role_AND_settings_frame)  #Котроль над игроками, присваивание роли и настройки


        right_part_layout.addWidget(vote_frame)
        right_part_layout.addWidget(hint_frame)






        """
        
        Расстановка нижней части окна
        
        """
        bottom_frame = QFrame()
        botom_layout = QVBoxLayout(bottom_frame)


        """Собираем верхнюю часть слоев"""
        top_layout.addWidget(left_part_frame)
        top_layout.addWidget(right_part_frame)

        left_part_layout.addWidget(player_AND_master_choose_frame)  #Еще один уровень деления

        player_AND_master_choose_layout.addWidget(players_frame)
        player_AND_master_choose_layout.addWidget(players_control_frame)
        #Добавили игроков и окно выбора игрока мастером


        left_part_layout.addWidget(players_control_WITH_master_role_AND_settings_frame) #Здесь еще один уровень деления

        players_control_WITH_master_role_AND_settings_layout.addWidget(players_control_frame)
        players_control_WITH_master_role_AND_settings_layout.addWidget(master_role_AND_setting_frame)#И еще один уровень деления

        master_role_AND_setting_layout.addWidget(master_role_frame)
        master_role_AND_setting_layout.addWidget(master_settings_frame)
        #Добавили Контроль над игроками И назначение ролей с настрйоками




        """Собираем нижнюю часть слоев"""


        main_layout.addWidget(top_frame)
        main_layout.addWidget(bottom_frame)

        # И теперь показываем все собранное на экран
        main_layout.addWidget(left_part_frame)
        

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