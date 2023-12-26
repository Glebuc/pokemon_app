from ui_mainwindow import Ui_MainWindow

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QMessageBox, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import model
import pypokedex
from controller import PokemonInfoController
import requests



class UIFunction():
    def __init__(self, ui_main_window_instance):
        self.ui = ui_main_window_instance
        self.pokemon_info_controller = PokemonInfoController(self.ui.frameViewPokemon)

    @Slot()
    def get_search_field(self):
        text_filed = self.ui.searchPokemon.text()
        return text_filed

    def clear_frame(self):
        for i in reversed(range(self.ui.frameViewPokemon.layout().count())):
            widget = self.ui.frameViewPokemon.layout().itemAt(i).widget()
            if widget:
                widget.deleteLater()
    def get_pokemon_info(self, pokemon_name):
        try:
            pokemon = pypokedex.get(name=pokemon_name.lower())
            name = pokemon.name
            types = ', '.join([str(t) for t in pokemon.types])
            base_stats = pokemon.base_stats
            img = pokemon.sprites.front.get('default', '') if pokemon.sprites.front else ""
            weight = pokemon.weight
            height = pokemon.height

            pokemon_info = {
                'Name': name,
                'Types': types,
                'Base Stats': base_stats,
                'Weight': weight,
                'Height': height
            }

            # Предполагается, что self.ui - экземпляр Ui_MainWindow, содержащий frameViewPokemon
            self.ui.frameViewPokemon.layout().removeItem(self.ui.frameViewPokemon.layout().itemAt(0))  # Удаление предыдущих виджетов, если они есть
            self.clear_frame()
            label_image = QLabel(self.ui.frameViewPokemon)
            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(img).content)
            label_image.setPixmap(pixmap)
            self.ui.frameViewPokemon.layout().addWidget(label_image)

            # Создаем QLabel для имени покемона и добавляем его в frameViewPokemon
            label_name = QLabel(self.ui.frameViewPokemon)
            label_name.setStyleSheet("font-size: 20px; font-weight: bold; color: black;")
            label_name.setText(f"Имя: {pokemon_info['Name']}")
            self.ui.frameViewPokemon.layout().addWidget(label_name)

            # Создаем QLabel для типов покемона и добавляем его в frameViewPokemon
            label_types = QLabel(self.ui.frameViewPokemon)
            label_types.setStyleSheet("font-size: 16px; color: black;")
            label_types.setText(f"Тип: {pokemon_info['Types']}")
            self.ui.frameViewPokemon.layout().addWidget(label_types)

            # Создаем QLabel для веса покемона и добавляем его в frameViewPokemon
            label_weight = QLabel(self.ui.frameViewPokemon)
            label_weight.setStyleSheet("font-size: 16px; color: black;")
            label_weight.setText(f"Вес: {pokemon_info['Weight']}")
            self.ui.frameViewPokemon.layout().addWidget(label_weight)

            # Создаем QLabel для высоты покемона и добавляем его в frameViewPokemon
            label_height = QLabel(self.ui.frameViewPokemon)
            label_height.setStyleSheet("font-size: 16px; color: black;")
            label_height.setText(f"Рост: {pokemon_info['Height']}")
            self.ui.frameViewPokemon.layout().addWidget(label_height)

            return pokemon_info
        except Exception as e:
            print(e)
            return None

    def check_pokemon(self):
        pokemon_name = self.get_search_field()
        pokemon_info = self.get_pokemon_info(pokemon_name)

        if pokemon_info is None:
            QMessageBox.critical(None, "Ошибка", "Некорректное имя покемона!", QMessageBox.StandardButton.Ok)
        else:
            print(pokemon_info)
    def fill_combo_box(self):
        combo_box = self.ui.comboBox
        results = model.get_all_types_pokemon()
        while results.next():
            item = results.value(0)
            combo_box.addItem(item)







