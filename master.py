"""

Модуль управляет поведением мастера.

Ведущий(мастер) управляет поведением всей игры и программы.

"""

import sys
from PyQt5.QtWidgets import QApplication
from player import Player

from wait_room import WaitRoom
from game_room import GameRoom      #Эти модули отвечают за логику внутри комнат
from play_room import PlayRoom

import game_event
import game_history



class Master:
    def __init__(self, nickname):
        self.master_player = Player(nickname)
        self.date = None

        #Создадим объекты внутри мастера, отвечающие за игровые события и историю
        self.event = game_event.GameEvent()
        self.history = game_history.History()

        #Мастер создает игровую комнату ожидания
        self.wait_room = WaitRoom()

        #Мастер создает игровую комнату набора игроков в игру
        self.game_room = GameRoom()

        #И игровая комната
        self.play_room = PlayRoom()

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

    def set_player_playroom(self):
        #Метод получает всех игроков из настройки игры GameRoom в PlayRoom
        players = self.game_room.get_players()
        self.play_room.set_players(players)

    """Функциональные Методы playroom"""
    def add_vote(self, nickname):
        for player in self.play_room.players:
            if nickname == player.nick_name:
                self.play_room.players_at_vote.append(player)

    def return_vote(self, nickname):
        for player in self.play_room.players:
            if nickname == self.play_room.players_at_vote:
                self.play_room.players_at_vote.remove(player)

    def shoot_player(self, nickname):   #Застреливаем игрока (Меняем его статус на "Застрелян")
        #Ищем игрока
        for player in self.play_room.players:
            if player.nick_name == nickname:
                player.condition = "Застрелян"

    def vote_player(self, nickname):    #Заголосуем игрока (Меняем его статус на "Заголосован")
        # Ищем игрока
        for player in self.play_room.players:
            if player.nick_name == nickname:
                player.condition = "Заголосован"

    def lift_player(self, nickname):
        # Ищем игрока
        for player in self.play_room.players:
            if player.nick_name == nickname:
                player.condition = "Поднят"

    def back_player(self, nickname):
        # Ищем игрока
        for player in self.play_room.players:
            if player.nick_name == nickname:
                player.drop_condition()






if __name__ == "main":
    pass