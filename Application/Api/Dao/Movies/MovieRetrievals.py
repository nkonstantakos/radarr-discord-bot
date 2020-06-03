from Application.Api.Domain.Movie import Movie
from Application.Api.Dao.Movies.MovieDTO import MovieDTO
from sqlite3 import Cursor, Connection


def get_all_movies(connection: Connection):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM MOVIES''')
    return get_records_as_movies(cursor)


def get_all_movies_by_channel(connection: Connection, channel_id: int):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM MOVIES
                      WHERE channel_id = ?''', (channel_id,))
    return get_records_as_movies(cursor)


def get_movie_by_imdb_id(connection: Connection, imdb_id: str):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM MOVIES
                      WHERE imdb_id LIKE ?''', (imdb_id,))
    movie_records = get_records_as_movies(cursor)
    return movie_records


def get_movie_by_movie_id(connection: Connection, movie_id: int):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM MOVIES
                      WHERE movie_id = ?''', (movie_id,))
    movie_records = get_records_as_movies(cursor)
    return movie_records


def get_all_movies_pending_approval_for_channel(connection: Connection, channel_id: int):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM MOVIES
                      WHERE approved = 0
                      AND deleted = 0
                      AND declined = 0
                      AND channel_id = ?''', (channel_id,))
    return get_records_as_movies(cursor)


def get_all_movies_pending_approval(connection: Connection):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM MOVIES
                      WHERE approved = 0
                      AND deleted = 0
                      AND declined = 0''')
    return get_records_as_movies(cursor)


def get_movies_pending_approval(connection: Connection, private: bool):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM MOVIES
                      WHERE approved = 0
                      AND deleted = 0
                      AND declined = 0
                      AND private = ?''', (int(private),))
    return get_records_as_movies(cursor)


def get_declined_movies(connection: Connection):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM MOVIES
                      WHERE declined = 1
                      AND deleted = 0
                      AND approved = 0''')
    return get_records_as_movies(cursor)


def get_deleted_movies(connection: Connection):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM MOVIES
                      WHERE deleted = 1''')
    return get_records_as_movies(cursor)


def get_records_as_movies(cursor: Cursor):
    result = cursor.fetchall()
    items = []
    for row in result:
        items.append(MovieDTO(int(row[0]), str(row[1]), str(row[2]), bool(row[4]),
                              bool(row[5]), bool(row[6]), bool(row[7]), int(row[8]),
                              int(row[9]), None, int(row[3])))
    return items
