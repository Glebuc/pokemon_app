
from Pyside6.QtSql import QSqlDatabase, QSqlQuery


def init_db():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabseName("pokemon_db")

    db.open()