from PySide6.QtWidgets import QLabel, QVBoxLayout, QFrame

class PokemonInfoController:
    def __init__(self, frame_view_pokemon: QFrame):
        self.frame_view_pokemon = frame_view_pokemon
        self.layout = QVBoxLayout(self.frame_view_pokemon)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(10)


        self.label_name = QLabel(self.frame_view_pokemon)
        self.label_name.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        self.layout.addWidget(self.label_name)


        self.label_types = QLabel(self.frame_view_pokemon)
        self.label_types.setStyleSheet("font-size: 16px; color: white;")
        self.layout.addWidget(self.label_types)

    def display_pokemon_info(self, pokemon_info):
        # Очищаем существующие виджеты в layout
        self.label_name.clear()
        self.label_types.clear()

        # Если есть информация о покемоне, заполняем виджеты
        if pokemon_info:
            name = pokemon_info.get('Name', 'Unknown')
            types = pokemon_info.get('Types', 'Unknown')

            # Заполняем QLabel с именем покемона
            self.label_name.setText(f"Name: {name}")

            # Заполняем QLabel с типами покемона
            self.label_types.setText(f"Types: {types}")
