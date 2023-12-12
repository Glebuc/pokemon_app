from ui_mainwindow import Ui_MainWindow

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QMessageBox



class UIFunction():
    def __init__(self, ui_main_window_instance):
        self.ui = ui_main_window_instance

    @Slot()
    def get_search_field(self):
        text_filed = self.ui.searchPokemon.text()
        print(text_filed)




