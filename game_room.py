"""

Модуль управляет поведением игровой комнаты(рассадки за столом), в которой начнется игра.

"""
from random import shuffle

class GameRoom:
    def __init__(self):
        self.players = []

    def append_player(self, player):
        self.players.append(player)

    def delete_player(self, row):
        self.players.pop(row)

    #Метод перемешиваем всех игроков по их позиции за игровым столом.
    def shake_players(self):
        shuffle(self.players)
