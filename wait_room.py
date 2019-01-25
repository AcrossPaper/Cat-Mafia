"""

Модуль управляет поведением игровой комнаты.

Игровая комната место, откуда приходят и откуда уходят игроки с игры. Некий промежуточный буфер, служащий для работы программы

"""

class WaitRoom:
    def __init__(self):
        #Пока что в комнате нету игроков, кроме самого мастера Ему нужно будет добавить самого себя.
        self.players = []

    def set_date(self, date):
        # Игровая комната была создана в определенный день. Эту дату мы получаем от игрового мастера.
        self.date = date

    def append_player(self, player):
        self.players.append(player)

    def delete_player(self, row):
        self.players.pop(row)

