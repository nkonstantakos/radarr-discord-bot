from Application.Api.Domain.PlexUser import PlexUser
from sqlite3 import Connection
from sqlite3 import Cursor
from typing import List


def get_users(connection):
    """
    @type connection: Connection
    """
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM PLEX_USERS''')
    return get_records_as_users(cursor)


def get_user_by_discord_id(connection: Connection, discord_id: int):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM PLEX_USERS
                      WHERE discord_id = ?''', (discord_id,))
    return get_records_as_users(cursor)


def get_users_by_user_ids(connection: Connection, user_ids: List[int]):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM PLEX_USERS
                      WHERE user_id IN ({sequence})'''.format(sequence=','.join(['?']*len(user_ids))), user_ids)
    return get_records_as_users(cursor)


def get_admin_users(connection: Connection):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM PLEX_USERS
                      WHERE admin = ?''', 1)
    return get_records_as_users(cursor)


def get_moderator_users(connection: Connection):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM PLEX_USERS
                      WHERE moderator = ?''', 1)
    return get_records_as_users(cursor)


def get_records_as_users(cursor: Cursor):
    result = cursor.fetchall()
    items = []
    for row in result:
        items.append(PlexUser(int(row[0]), int(row[1]), str(row[2]), bool(row[3]), bool(row[4])))
    return items
