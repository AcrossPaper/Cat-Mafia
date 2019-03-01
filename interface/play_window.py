from PyQt5 import uic
from PyQt5.QtWidgets import QWidget



class Play_Window(QWidget):
        def __init__(self):
            super().__init__()
            uic.loadUi('play_window.ui', self)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = Play_Window()
    window.show()
    sys.exit(app.exec_())
