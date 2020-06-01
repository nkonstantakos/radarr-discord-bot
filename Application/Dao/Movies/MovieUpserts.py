from Application.Domain.Movie import Movie
from sqlite3 import Connection


def insert_movie(connection, movie):
    """
    @type connection: Connection
    @type movie: Movie
    """
    connection.execute('INSERT INTO MOVIES (imdb_id, movie_name, creator, approved, declined, deleted, private)'
                       'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (movie.imdb_id,
                        movie.movie_name,
                        movie.creator,
                        int(movie.approved),
                        int(movie.declined),
                        int(movie.deleted),
                        int(movie.private)))


def approve_movie(connection, movie):
    """
    @type connection: Connection
    @type movie: Movie
    """
    connection.execute('''UPDATE MOVIES
                          SET approved = 1
                          WHERE movie_id = ?''', movie.movie_id)
    connection.commit()


def approve_all(connection):
    """
    @type connection: Connection
    """
    connection.execute('''UPDATE MOVIES
                        SET approved = 1
                        WHERE approved = 0''')
    connection.commit()


def decline_movie(connection, movie):
    """
    @type connection: Connection
    @type movie: Movie
    """
    connection.execute('''UPDATE MOVIES
                          SET declined = 1
                          WHERE movie_id = ?''', movie.movie_id)
    connection.commit()


def delete_movie(connection, movie):
    """
    @type connection: Connection
    @type movie: Movie
    """
    connection.execute('''UPDATE MOVIES
                          SET deleted = 1
                          WHERE movie_id = ?''', movie.movie_id)
    connection.commit()
