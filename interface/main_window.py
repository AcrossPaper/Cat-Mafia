import sys
from PyQt5.QtWidgets import QApplication, QWidget

from interface import start_window as _start_window
from interface import work_window as _work_window
from interface import play_window as _play_window

#Класс Main_Window инициализирует и управляет всеми созданными окнами для работы приложения. Работает со слотами и сигналами
class Main_Window:
    def __init__(self, master):
        self.master = master

        self.start_window = _start_window.Start_Window()
        self.work_window = _work_window.Work_Window()
        self.play_window = _play_window.Play_Window()

        #Настроим сигналы стартового окна
        self.setup_start_window_signals()

        #Настроим сигналы рабочего окна настроек
        self.setup_work_window_signals()

        #Настроим сигналы игрового окна


    def setup_start_window_signals(self):
        """

        Метод настраивает поведение кнопки "Создать игровой вечер"

        """
        self.start_window.create_evening_game_button.clicked.connect(self.btn_press_create_eveninig_game)

    def setup_work_window_signals(self):
        """

        Метод настривает работу всех виджетов с окна WORK_WINDOW

        """

        #Первым делом настроим левую часть окна, а именно кнопки добавить и удаить игроков

        #Кнопка добавить игрока
        self.work_window.btn_add_player_room.clicked.connect(self.btn_press_add_player_room)

        #Кнопка удалить игрока
        self.work_window.btn_del_in_room.clicked.connect(self.btn_press_delete_player_room)

        """     Дальше пошла правая часть окна                    """

        #Кнопка зарегестрировать игрока
        self.work_window.btn_register.clicked.connect(self.btn_press_register_player)

        #Кнопка удалить игрока справа
        self.work_window.btn_del_in_game.clicked.connect(self.btn_press_delete_in_game)

        #Кнока зарегестрировать всех игроков
        self.work_window.btn_add_all_players.clicked.connect(self.btn_press_add_all_players)

        #Кнопка перемешать всех игроков
        self.work_window.btn_shake.clicked.connect(self.btn_press_shake)

        #Кнопка начать игру
        self.work_window.btn_start_game.clicked.connect(self.btn_press_start)

        #Кнопка переместить игрока
        self.work_window.btn_swap_player.clicked.connect(self.btn_press_swap)

    def setup_play_window_signals(self):
        """
        Настраивает работу виджетов playwindow



        """

        """Дальше идет описание слотов(функций при срабатывании сигнала нажатия на кнопку)"""

    def btn_press_add_player_room(self):    #Если нажата кнопка добавить игрока (слева)
        #Получим введеный ник
        input_nick = self.work_window.edit_player_name.text()

        #Добавим его в комнату ожидания
        self.master.add_player_to_wait_room(input_nick)

        #Отразим изменения на экране, перед этим очистим виджет
        self.work_window.list_players_in_room.clear()

        for player in self.master.wait_room.players:
            self.work_window.list_players_in_room.addItem(player.nick_name)

        #Вернем фокус на виджет поля для удобства
        self.work_window.edit_player_name.setFocus()



    def btn_press_delete_player_room(self): #Если нажата кнопка удалить игрока (слева)
        #Посмотрим какой столбец был выбран в списке сверху (Надеюсь что с такой настройкой виджета можно будет всегда выбрать только один)
        selected_row = self.work_window.list_players_in_room.selectedIndexes()

        #И удалим его из комнаты ожидания мастера
        self.master.delete_player_from_wait_room(selected_row[0].row())

        # Отразим изменения на экране, перед этим очистим виджет
        self.work_window.list_players_in_room.clear()

        for player in self.master.wait_room.players:
            self.work_window.list_players_in_room.addItem(player.nick_name)

    """                       Теперь здесь все идет, что оказалось справа окна            """
    def btn_press_register_player(self):    #Если нажата кнопка зарегестрировать игрока (Справа)
        #Посмотрим, какой игрок выделен в списке с левой части окна
        selected_row = self.work_window.list_players_in_room.selectedIndexes()

        #Добавим его в игровую комнату мастера
        self.master.register_player_to_game_room(selected_row[0].data())

        # Отразим изменения на экране, перед этим очистим виджет
        self.work_window.list_players_in_game.clear()


        for player in self.master.game_room.players:
            self.work_window.list_players_in_game.addItem(player.nick_name)



        #Очистим комнату ожидания от игроков, уже добавленных в игру при помощи разности множеств с сохранением порядка
        self.master.wait_room.players = self.diff(self.master.wait_room.players, self.master.game_room.players)

        # Отразим изменения на экране, перед этим очистим виджет
        self.work_window.list_players_in_room.clear()


        for player in self.master.wait_room.players:
            self.work_window.list_players_in_room.addItem(player.nick_name)

        # Установим игрокам их номера
        self.set_pos_game_room()



    def btn_press_delete_in_game(self): #Если нажата кнопка удалить игрока (Справа)
        #Посмотрим, какой игрок выделен в списке в ПРАВОЙ части окна
        selected_row = self.work_window.list_players_in_game.selectedIndexes()

        # Вернем игрока к ожидающим
        self.master.add_player_to_wait_room(self.master.game_room.players[selected_row[0].row()].nick_name)

        #Удалим его из игровой комнаты мастера по его позиции в списке
        self.master.delete_from_game_room(selected_row[0].row())



        # Отобразим изменения на экране, перед этим очистим виджеты
        self.work_window.list_players_in_room.clear()
        self.work_window.list_players_in_game.clear()

        for player in self.master.wait_room.players:
            self.work_window.list_players_in_room.addItem(player.nick_name)

        for player in self.master.game_room.players:
            # Отформатируем строку чтобы узнать номер игркоа за столом
            self.work_window.list_players_in_game.addItem(player.nick_name)

        # Установим игрокам их номера
        self.set_pos_game_room()


    def btn_press_add_all_players(self):    #При нажатии на кнопку Зарегестрировать всех игроков
        #Перенесем всех игроков из комнаты ожидания в игровую комнату
        for wait_player in self.master.wait_room.players:
            self.master.register_player_to_game_room(wait_player.nick_name)

        #Удалим всех добавленных игроков из комнаты ожидания
        self.master.wait_room.players.clear()

        # Отобразим изменения на экране, перед этим очистим виджеты
        self.work_window.list_players_in_room.clear()
        self.work_window.list_players_in_game.clear()

        for player in self.master.wait_room.players:
              self.work_window.list_players_in_room.addItem(player.nick_name)

        for player in self.master.game_room.players:
             self.work_window.list_players_in_game.addItem(player.nick_name)

        # Установим игрокам их номера
        self.set_pos_game_room()


    def btn_press_create_eveninig_game(self):#При нажатии на кнопку создать игровой вечер
        #Запомним значение из поля даты
        self.master.date = self.start_window.date_edit.date(), self.start_window.date_edit.time()

        #Закроем окошко от посторонних глаз
        self.start_window.hide()

        #Откроем следующее окно, в котором настраивается следующая игра
        self.work_window.show()

    def btn_press_shake(self):  #При нажатии на кнопку перемешать игроков
        self.master.shake_player_at_game_room()

        #Отобразим изменения на экране, перед этим очистим виджеты
        self.work_window.list_players_in_game.clear()

        for player in self.master.game_room.players:
             self.work_window.list_players_in_game.addItem(player.nick_name)

        # Установим игрокам их номера
        self.set_pos_game_room()

    def btn_press_swap(self):    #При нажатии на кнопку переместить на место
        #Получаем индекс выбранного элемента
        chosen_index = self.work_window.list_players_in_game.selectedIndexes()[0].row()

        #Получаем индекс из поля
        place_index = int(self.work_window.edit_player_place.text()) - 1

        #Меняем местами два элемента списка по полученным индексам
        self.master.game_room.players[chosen_index], self.master.game_room.players[place_index] = self.master.game_room.players[place_index], self.master.game_room.players[chosen_index]

        # Отобразим изменения на экране, перед этим очистим виджеты
        self.work_window.list_players_in_game.clear()

        for player in self.master.game_room.players:
            self.work_window.list_players_in_game.addItem(player.nick_name)

        # Установим игрокам их номера
        self.set_pos_game_room()

    def btn_press_start(self):
        #Кнопка начать игру в WorkWindow
        self.play_window.show() #Покажем форму игры
        self.work_window.hide() #И спрячем форму настроек

    def diff(self, first, second):  #Разница списков с сохранением порядка
        second = set(second)
        return [item for item in first if item not in second]

    def set_pos_game_room(self):
        #Метод устанавливает номер игрока за столом
        pos = 0

        for i in range(self.work_window.list_players_in_game.count()):
            self.work_window.list_players_in_game.insertItem(pos, "{}. {}".format(pos + 1, self.work_window.list_players_in_game.item(pos).text()))
            #Удалим предыдущиее значение
            self.work_window.list_players_in_game.takeItem(pos + 1)

            pos = pos + 1











