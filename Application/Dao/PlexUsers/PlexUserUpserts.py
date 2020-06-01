from Application.Domain.PlexUser import PlexUser
from sqlite3 import Connection


def insert_user(connection, user):
    """
    @type connection: Connection
    @type user: PlexUser
    """
    connection.execute('INSERT INTO PLEX_USERS (discord_id, nickname, moderator, admin)'
                       'VALUES (?, ?, ?, ?)',
                       (user.discord_id,
                        user.nickname,
                        int(user.moderator),
                        int(user.admin)))
