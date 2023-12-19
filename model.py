
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

SELECT_ALL_POKEMON =  "SELECT * FROM pokemon"

def add_row(q,name, weight, type):
    q.addBindValue(name)
    q.addBindValue(weight)
    q.addBindValue(type)
    q.exec()



def db_connection(function_query):
    def wrapper():
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("pokemon_db.sqlite")
        db.open()
        if not db.open():
            print("Нет соединения с базой данных. ОШИБКА")
            sys.exit(1)
        else:
            print("Соединение с базой данных успешно")

        result = function_query()  # Запуск функции и сохранение результата
        return result
    return wrapper

@db_connection
def init_db():
    """Это функция инициализирует Базу данных"""
    q = QSqlQuery()
    q.exec(CREATE_TABLE_POKEMON)

@db_connection
def fill_pokemon_data():
    q = QSqlQuery()
    q.prepare(INSERT_SQL)
    for i in range(1,1200):
        try:
            pokemon = get(dex=i)
            add_row(q, pokemon.name, pokemon.weight, pokemon.types[0] )
        except:
            continue
@db_connection
def get_all_pokemon():
    q = QSqlQuery()
    q.exec_(SELECT_ALL_POKEMON)
    # q.next()
    return q






