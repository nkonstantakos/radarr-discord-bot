from Dao.Tables import MovieDao
import sqlite3


class GroceriesDao(object):

    def __init__(self, db_name):
        self.db_name = db_name

    def create_tables(self):
        conn = self.get_db_connection()
        MovieDao.create_movie_table()
        commit_and_close(conn)

    def get_db_connection(self):
        return sqlite3.connect(self.db_name)


def commit_and_close(conn):
    conn.commit()
    conn.close()

