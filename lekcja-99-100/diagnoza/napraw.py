import sqlite3
def znajdz(conn, nazwa):
    sql = "SELECT id FROM osoby WHERE nazwa = '" + nazwa + "'"
    return conn.execute(sql).fetchall()
