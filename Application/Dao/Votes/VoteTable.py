from sqlite3 import Connection


def create_vote_table(connection):
    """
    @type connection: Connection
    """
    connection.execute('''CREATE TABLE IF NOT EXISTS VOTES
                         (vote_id INTEGER PRIMARY KEY AUTOINCREMENT,
                         creator INTEGER,
                         movie_id TEXT,
                         direction INTEGER,
                         FOREIGN KEY(creator) REFERENCES PLEX_USERS (user_id),
                         FOREIGN KEY(movie_id) REFERENCES MOVIES (movie_id))''')
