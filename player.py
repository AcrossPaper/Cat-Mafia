"""

Модуль управляет поведением всех игроков

"""

class Player:
    def __init__(self, nick_name):
        self.nick_name = nick_name
        self.role = None

        self.condition = "В игре"  #Состояние игрока во время игры.
        self.fallcount = 0  #Количество фолов у игрока


    def set_role_mafia(self):
        self.role = "mafia"

    def set_role_citizen(self):
        self.role = "citizen"

    def set_role_sherif(self):
        self.role = "sheriff"

    def set_role_don(self):
        self.role = "don"

    def shoot_player(self):
        self.condition = "Shooted"

    def vote_player(self):
        self.condition = "Voted"

    def disc_player(self):
        self.condition = "disqualification"

    def drop_condition(self):
        #Сбросить роль игрока до роли в игре
        self.condition = "В игре"

    def add_fall(self):
        self.fallcount += 1

    def delete_fall(self):
        self.fallcount -= 1