
from PySide6.QtSql import QSqlDatabase, QSqlQuery

import sys


def init_db():
    """Это функция инициализирует Базу данных"""
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("pokemon_db.sqlite")
    db.open()
    if not db.open():
        print("Нет соединения с базой данных. ОШИБКА")
        sys.exit(1)
    else:
        print("Соединение с базой данных успешно")

    create_table_pokemon = QSqlQuery()
    create_table_pokemon.exec("""
    CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    name VARCHAR(150) NOT NULL,
    weight INTEGER,
    type VARCHAR(200)
    );
    """)