import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtGui import QColor

from interface import start_window as _start_window
from interface import work_window as _work_window
from interface import play_window as _play_window

import player

from PyQt5 import QtGui


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
        self.setup_play_window_signals()


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

        "Кнопка добавить игрока на голосование"
        self.play_window.btn_addvote.clicked.connect(self.player_add_vote)
        self.play_window.btn_voteend.clicked.connect(self.end_vote)

        pass

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

        #Передадим всех игроков в PlayWindow через мастера
        self.master.set_player_playroom()

        #Выведем на виджет с игроками полученных игроков
        player_number = 0
        for player in self.master.game_room.get_players():  #game_room берем из него, так как в нем сидят игроки на следующую игру
            self.play_window.table_players.insertRow(self.play_window.table_players.rowCount())

            self.play_window.table_players.setItem(player_number, 0, QTableWidgetItem(player.nick_name))
            self.play_window.table_players.setItem(player_number, 1, QTableWidgetItem("Нет роли"))
            self.play_window.table_players.setItem(player_number, 2, QTableWidgetItem("В игре"))

            player_number += 1



        self.play_window.show() #Покажем форму игры
        self.work_window.hide() #И спрячем форму настроек




        """СЛОТЫ PLAYROOM"""
    #btn_add_vote
    def player_add_vote(self):  #Параметр для метода берется из выделенного игрока таблицы с игроками
        # Узнаем номер выделенного игрока из таблицы с игроками
        selectedPlayer = self.play_window.table_players.selectedIndexes()
        playerNumber = selectedPlayer[0].row()

        #Ищем игрока в памяти добавленных игроков по его никнейму в памяти мастера
        findNick = selectedPlayer[0].data()
        foundPlayer = None

        for player in self.master.play_room.players:
            if player.nick_name == findNick:
                foundPlayer = player

        #Теперь добавляем в память игроков на голосование ссылку на игрока что был выставлен
        self.master.play_room.add_vote(foundPlayer)

        #Добавляем игрока на виджет таблицы голосования из памяти мастера
        rowCount = self.play_window.table_vote.rowCount()
        self.play_window.table_vote.insertRow(rowCount) #Вставляем новую строку в таблице

        #Формируем строку которую вставим в таблицу
        stringAtTable = "{}.{}".format(playerNumber + 1, foundPlayer.nick_name)
        self.play_window.table_vote.setItem(rowCount, 0, QTableWidgetItem(stringAtTable))
    #btn_endvote
    def end_vote(self): #Кнопка закончить голосование
        #Получим список игроков из таблицы голосования
        player_li = []

        for i in range(self.play_window.table_vote.rowCount()):
            player_name = self.play_window.table_vote.item(i, 0).text()
            player_name = player_name.split('.')[1] #Отсчечем номер игрока от строки (Особенности программы)
            voteCount = int(self.play_window.table_vote.item(i, 1).text())

            nextPlayer = [player_name, voteCount]
            player_li.append(nextPlayer)

        #Сортируем
        def byVote_key(player):
            return player[1]

        player_li = sorted(player_li, key = byVote_key, reverse = True)

        #Смотрим сколько игроков проиграло на голосовании (Может быть автокотострофа)
        vote_down_players = []
        maxVote = player_li[0][1]

        for player in player_li:
            player_vote = player[1]
            if player_vote == maxVote:
                vote_down_players.append(player[0])

        #Теперь в vote_down_player игроки, которых нужно подсветить для ведущего, сделаем это при помощи изменения цвета клетки
        #Получим заранее все ники из памяти мастера

        #Осмотрим все ники из таблицы с игроками, и сравним их с vote_down_players. Найдем совпадение - подсветим.
        table_nicknames = []
        for nextRow in range(self.play_window.table_vote.rowCount()):
            next_item = self.play_window.table_vote.item(nextRow, 0)
            next_nick = next_item.text()
            next_nick = next_nick.split(".")[1] #Избавляемся от точки в нике
            if next_nick in vote_down_players:
                self.play_window.table_players.item(nextRow, 0).setBackground(QtGui.QColor(255, 0, 0)) #Подсветим в таблице списка игроков


















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











