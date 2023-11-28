import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
import pypokedex
import model


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        model.init_db()


if __name__ == "__main__":
    pokemon = pypokedex.get(name="charmander")
    print(pokemon.abilities)
    print(pokemon.name)
    print(pokemon.types)
    print(pokemon.sprites)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())