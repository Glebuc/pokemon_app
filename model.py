
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from pypokedex import get
import sys

INSERT_SQL = """INSERT INTO pokemon(name, weight, type) VALUES 
(?, ?, ?);"""


CREATE_TABLE_POKEMON = """CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    name VARCHAR(150) NOT NULL,
    weight INTEGER,
    type VARCHAR(200)
    );"""

def add_row(q,name, weight, type):
    q.addBindValue(name)
    q.addBindValue(weight)
    q.addBindValue(type)
    q.exec()


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

    q = QSqlQuery()
    q.exec(CREATE_TABLE_POKEMON)
    db.close()

def fill_pokemon_data():
    for i in range(100,152):
        pokemon = get(dex=i)
        print(pokemon.dex)
        print(pokemon.name)
        print(pokemon.types[0])
        print("++++++++++++++")

    # for pokemon_name in all_pokemon_names:
    #     poke = get(pokemon_name)
    #
    #     add_row(q, poke.name, poke.weight, poke.types)
    # db.close()

fill_pokemon_data()



