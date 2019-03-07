#Модуль отвечающий за логику внутри play_window.py

import player

class PlayRoom:
    def __init__(self):
        self.players = []   #Игркои внутри комнаты
        self.players_at_vote = []   #Игроки на следующее голосование

    # btn_addvote
    def add_vote(self, player):
        self.players_at_vote.append(player)

    # bnt_shoot
    def shoot_player(self, player):
        #Метод отстреливает игрока, меняя его состоянии на ОТСТРЕЛЯН. Данный игрок больше не принимает участия в игре
        index = self.players.index(player)
        self.players[index].shoot_player()

    # btn_voted
    def vote_player(self, player):
        # Метод выводит из игры игрока голосованием
        index = self.players.index(player)
        self.players[index].vote_player()

    # btn_disc
    def disc_player(self, player):
        # Метод выводит игрока через нарушения правил игры ведущим.
        index = self.players.index(player)
        self.players[index].disc_player()

    # btn returnvote
    def vote_return(self, player):
        #Отозвать игрока от голосования
        index = self.players.index(player)
        self.players[index].drop_condition()

    # btn_backplayer
    def return_player(self, nick_name):
        #Если ведущий по ошибке удалил игрока его можно вернуть в игру (Изменить его состояние на "В игре")

        #Ищем игрока в списке
        for player in self.players_at_vote:
            if player.nick_name == nick_name:
                player.drop_condition()

    # btn_addfall
    def add_fall(self, player):
        # Событие добавления фолла игркоа
        index = self.players.index(player)
        self.players[index].add_fall()

    def set_players(self, players):
        self.players = players.copy()   #Чтобы потом вернуть игроков обратно в окно к настройкам
