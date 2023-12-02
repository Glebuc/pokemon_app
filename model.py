
from PySide6.QtSql import QSqlDatabase, QSqlQuery

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
    q.prepare(INSERT_SQL)
    add_row(q, "Bulbasaur", 7, 'grass')
    db.close()



