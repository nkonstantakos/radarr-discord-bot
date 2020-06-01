from Domain.PlexUser import PlexUser
from sqlite3 import Connection


def create_user_table(connection):
    """
    @type connection: Connection
    """
    connection.execute('''CREATE TABLE IF NOT EXISTS PLEX_USER
                         (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                         discord_id INTEGER,
                         nickname TEXT,
                         moderator INTEGER,
                         admin INTEGER)''')


def insert_movie(conn, user):
    """
    @type conn: Connection
    @type user: PlexUser
    """
    conn.execute('INSERT INTO PLEX_USER (discord_id, nickname, moderator, admin)'
                 'VALUES (?, ?, ?, ?)',
                 (user.discord_id,
                  user.nickname,
                  int(user.moderator),
                  int(user.admin)))
