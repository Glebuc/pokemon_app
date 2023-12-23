from ui_mainwindow import Ui_MainWindow

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QMessageBox
import model



class UIFunction():
    def __init__(self, ui_main_window_instance):
        self.ui = ui_main_window_instance

    @Slot()
    def get_search_field(self):
        text_filed = self.ui.searchPokemon.text()
        print(text_filed)

    def fill_combo_box(self):
        combo_box = self.ui.comboBox
        results = model.get_all_types_pokemon()
        while results.next():
            item = results.value(0)
            combo_box.addItem(item)







