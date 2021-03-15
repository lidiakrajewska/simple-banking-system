import sqlite3


CREATE_CARD_TABLE = 'CREATE TABLE IF NOT EXISTS card ' \
                    '(id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);'

INSERT_CARD = 'INSERT INTO card (number, pin) VALUES (?, ?);'

CHECK_IF_EXISTS = 'SELECT * FROM card WHERE number = ?;'

LOG_IN = 'SELECT * FROM card WHERE number = ? AND pin = ?;'

BALANCE = 'SELECT balance FROM card WHERE number = ?;'


def connect():
    return sqlite3.connect('card.s3db')


def create_tables(connection):
    with connection:
        connection.execute(CREATE_CARD_TABLE)


def add_card(connection, card_number, pin):
    with connection:
        connection.execute(INSERT_CARD, (card_number, pin))


def check_card(connection, card_number):
    with connection:
        return connection.execute(CHECK_IF_EXISTS, (card_number,)).fetchone()


def log_in(connection, card_number, pin):
    with connection:
        return connection.execute(LOG_IN, (card_number, pin)).fetchone()


def balance(connection, card_number):
    with connection:
        return connection.execute(BALANCE, (card_number,)).fetchone()
