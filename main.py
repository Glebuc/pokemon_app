import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView
from ui_mainwindow import Ui_MainWindow
import pypokedex
import model
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
        self.ui.btnSearchPokemon.clicked.connect(lambda: ui_function_instance.get_search_field())
        table_model = QSqlQueryModel()
        query = model.get_all_pokemon()
        table_model.setQuery(query)  # Получение данных из модели
        table_view = self.ui.tablePokemon
        table_view.setModel(table_model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())