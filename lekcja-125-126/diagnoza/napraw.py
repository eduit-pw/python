import sqlite3
def dodaj(sciezka, nazwa):
    conn = sqlite3.connect(sciezka)
    try:
        conn.execute("INSERT INTO produkty (nazwa) VALUES (?)", (nazwa,))
    finally:
        conn.close()
