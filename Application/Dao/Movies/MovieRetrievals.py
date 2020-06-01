from Application.Domain.Movie import Movie
from sqlite3 import Cursor


def get_all_movies(connection):
    """
    @type connection: Connection
    """
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM MOVIES''')
    return get_records_as_movies(cursor)


def get_all_movies_pending_approval(connection):
    """
    @type connection: Connection
    """
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM MOVIES
                      WHERE approved = 0
                      AND deleted = 0
                      AND declined = 0''')
    return get_records_as_movies(cursor)


def get_movies_pending_approval(connection, private):
    """
    @type connection: Connection
    @type private: bool
    """
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM MOVIES
                      WHERE approved = 0
                      AND deleted = 0
                      AND declined = 0
                      AND private = ?''', int(private))
    return get_records_as_movies(cursor)


def get_declined_movies(connection):
    """
    @type connection: Connection
    """
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM MOVIES
                      WHERE declined = 1
                      AND deleted = 0
                      AND approved = 0''')
    return get_records_as_movies(cursor)


def get_deleted_movies(connection):
    """
    @type connection: Connection
    """
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM MOVIES
                      WHERE deleted = 1''')
    return get_records_as_movies(cursor)


def get_records_as_movies(cursor):
    """
    @type cursor: Cursor
    """
    result = cursor.fetchall()
    items = []
    for row in result:
        items.append(Movie(int(row[0]), int(row[1]), str(row[2]), int(row[3]), bool(row[4]), bool(row[5]), bool(row[6])))
    return items
