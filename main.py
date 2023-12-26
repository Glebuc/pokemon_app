import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView
from ui_mainwindow import Ui_MainWindow
import pypokedex
import model
from PySide6.QtCore import Qt, Slot, QModelIndex
from PySide6.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery, QSqlQueryModel
from ui_function import UIFunction




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ui_function_instance = UIFunction(self.ui)
        model.init_db()
        # model.fill_pokemon_data()
        # self.ui.btnSearchPokemon.clicked.connect(lambda: ui_function_instance.get_search_field())
        table_model = QSqlQueryModel()
        query = model.get_all_pokemon()
        table_model.setQuery(query)  # Получение данных из модели
        table_view = self.ui.tablePokemon
        table_view.setModel(table_model)
        query_combo_box = model.get_all_types_pokemon()
        combo_box = self.ui.comboBox
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_view.setColumnHidden(0, True)
        self.ui.btnSearchPokemon.clicked.connect(lambda: ui_function_instance.check_pokemon())
        frame_view_pokemon = self.ui.frameViewPokemon
        # pokemon_info_controller = PokemonInfoController(frame_view_pokemon)
        # self.ui.tablePokemon.setColumnHidden(table_model.QModelIndex('id'), True)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())