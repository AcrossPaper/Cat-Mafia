"""

Модуль управляет поведением мастера.

Ведущий(мастер) управляет поведением всей игры и программы.

"""

import sys
from PyQt5.QtWidgets import QApplication
from player import Player

from wait_room import WaitRoom
from game_room import GameRoom



class Master:
    def __init__(self, nickname):
        self.master_player = Player(nickname)

        #Мастер создает игровую комнату ожидания
        self.wait_room = WaitRoom()

        #Мастер создает игровую комнату набора игроков в игру
        self.game_room = GameRoom()

        self.date = None

    #Мастер добавляет новопришедших игроков на вечер
    def add_player_to_wait_room(self, nick_name):
        player = Player(nick_name)
        self.wait_room.append_player(player)

    def delete_player_from_wait_room(self, row):
        self.wait_room.delete_player(row)

    ###############################################

    def register_player_to_game_room(self, nick_name):
        #Регистрация идет с уже добавленных игроков. Найдем его
        for wait_player in self.wait_room.players:
            if wait_player.nick_name == nick_name:
                self.game_room.append_player(wait_player)


    def delete_from_game_room(self, row):
        self.game_room.delete_player(row)

    def shake_player_at_game_room(self):
        self.game_room.shake_players()






if __name__ == "main":
    pass