from Application.Api.Domain.Movie import Movie
from sqlite3 import Connection


def insert_movie(connection: Connection, movie: Movie):
    connection.execute('INSERT INTO MOVIES (imdb_id, movie_name, creator, approved, declined, '
                       'deleted, private, channel_id, trakt_id)'
                       'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (movie.imdb_id,
                        movie.movie_name,
                        movie.creator.user_id,
                        int(movie.approved),
                        int(movie.declined),
                        int(movie.deleted),
                        int(movie.private),
                        movie.channel_id,
                        movie.trakt_id))


def approve_movie(connection: Connection, movie: Movie):
    connection.execute('''UPDATE MOVIES
                          SET approved = 1
                          WHERE movie_id = ?''', movie.movie_id)
    connection.commit()


def approve_all(connection: Connection):
    connection.execute('''UPDATE MOVIES
                        SET approved = 1
                        WHERE approved = 0''')
    connection.commit()


def decline_movie(connection: Connection, movie: Movie):
    connection.execute('''UPDATE MOVIES
                          SET declined = 1
                          WHERE movie_id = ?''', movie.movie_id)
    connection.commit()


def delete_movie(connection: Connection, movie: Movie):
    connection.execute('''UPDATE MOVIES
                          SET deleted = 1
                          WHERE movie_id = ?''', movie.movie_id)
    connection.commit()
