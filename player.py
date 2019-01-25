"""

Модуль управляет поведением всех игроков

"""

class Player:
    def __init__(self, nick_name):
        self.nick_name = nick_name
        self.role = None


    def set_role_mafia(self):
        self.role = "mafia"

    def set_role_citizen(self):
        self.role = "citizen"

    def set_role_sherif(self):
        self.role = "sheriff"

    def set_role_don(self):
        self.role = "don"