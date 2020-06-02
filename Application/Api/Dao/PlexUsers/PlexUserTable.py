from sqlite3 import Connection


def create_user_table(connection):
    """
    @type connection: Connection
    """
    connection.execute('''CREATE TABLE IF NOT EXISTS PLEX_USERS
                         (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                         discord_id INTEGER,
                         nickname TEXT,
                         moderator INTEGER,
                         admin INTEGER)''')

