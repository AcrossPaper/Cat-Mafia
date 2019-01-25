"""

Самое сложное окно всей программы. Здесь происходит вся игра.

"""
from interface import settings
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer

class Play_Window(QWidget):
    def __init__(self):
        super().__init__()

        #Создадим все необходимые виджеты

        """      Clock_Timer главный таймер окна
                 Он отображает все игровые события и управляет ими.
                 Ограничивает время игроков и делает еще массу полезных штук                               
                                                
                                                """
        self.clock_timer = QTimer()






        #Настроим их
        self.customise()




    def customise(self):
        """    Метод расставляет виджеты для работы    """
        pass

        #Настроим разрешение и положение окна
        self.resize(settings.PLAY_WINDOW_WIDTH, settings.PLAY_WINDOW_HEIGHT)
        self.move_to_center()

        #Настроим таймер для работы
        

    def sayHello(self):
        print("Hello world!")









    def move_to_center(self):
        """   Метод переносит окошко в центр  """
        form = self.frameGeometry()
        window_center = QDesktopWidget().availableGeometry().center()
        form.moveCenter(window_center)
        self.move(form.topLeft())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Play_Window()
    window.show()
    sys.exit(app.exec_())