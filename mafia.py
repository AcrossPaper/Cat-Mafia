"""

Главный модуль программы, стартовая точка запуска.

"""

import sys
from PyQt5.QtWidgets import QApplication
import master
from interface import main_window

#Создадим мастера
mst = master.Master("Бумажный")



#Покажем начальное окно и уйдем в обработчик событий
app = QApplication(sys.argv)
#Передадим в интерфейс ссылку на мастера
interface = main_window.Main_Window(mst)
interface.start_window.show()
sys.exit(app.exec_())







