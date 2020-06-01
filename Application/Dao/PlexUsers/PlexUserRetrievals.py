from Application.Domain.PlexUser import PlexUser
from sqlite3 import Connection


def get_users(connection):
    """
    @type connection: Connection
    """
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM PLEX_USERS''')
    return get_records_as_users(cursor)


def get_admin_users(connection):
    """
    @type connection: Connection
    """
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM PLEX_USERS
                      WHERE admin = ?''', 1)
    return get_records_as_users(cursor)


def get_moderator_users(connection):
    """
    @type connection: Connection
    """
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM PLEX_USERS
                      WHERE moderator = ?''', 1)
    return get_records_as_users(cursor)


def get_records_as_users(cursor):
    """
    @type cursor: Cursor
    """
    result = cursor.fetchall()
    items = []
    for row in result:
        items.append(PlexUser(int(row[0]), int(row[1]), str(row[2]), bool(row[3]), bool(row[4])))
    return items
