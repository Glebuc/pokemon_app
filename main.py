import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
import pypokedex
import model
from ui_function import UIFunction




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ui_function_instance = UIFunction(self.ui)
        model.init_db()
        self.ui.btnSearchPokemon.clicked.connect(lambda: ui_function_instance.get_search_field())




if __name__ == "__main__":
    pokemon = pypokedex.get(dex=1)
    print(pokemon.dex)
    print(pokemon.abilities)
    print(pokemon.name)
    print(pokemon.types)
    print(pokemon.sprites)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())