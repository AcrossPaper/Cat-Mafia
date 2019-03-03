#Модуль работает с игровыми событиями во время игры.

import player

class GameEvent:
    def __init__(self):
        self.voted_players = [] #Игроки, которые вконце дня будут голосоваться

    #btn_addvote
    def add_vote(self, player):
        self.voted_players.append(player)

    #bnt_shoot
    def shoot_player(self, player):
        #Метод отстреливает игрока, меняя его состоянии на ОТСТРЕЛЯН. Данный игрок больше не принимает участия в игре
        player.shoot_player()

    #btn_voted
    def vote_player(self, player):
        #Метод выводит из игры игрока голосованием
        player.vote_player()

    #btn_disc
    def disc_player(self, player):
        #Метод выводит игрока через нарушения правил игры ведущим.
        player.disc_player()

    #btn returnvote
    def vote_return(self):
        #Отозвать игрока от голосования
        player.drop_condition()


    #btn_backplayer
    def return_player(self):
        #Если ведущий по ошибке удалил игрока его можно вернуть в игру
        player.drop_condition()

    #btn_addfall
    def add_fall(self):
        #Событие добавления фолла игркоа
        player.add_fall()

    #btn_nexttalk
    def player_end_talk(self):
        #Событие при котором игрок заканчивает свою речь
        #В событии нужно регестрировать время, которое игрок говорил для ИСТОРИИ







