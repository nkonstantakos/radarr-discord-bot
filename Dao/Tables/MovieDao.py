from Domain.Movie import Movie
from sqlite3 import Connection


def create_movie_table(connection):
    """
    @type connection: Connection
    """
    connection.execute('''CREATE TABLE IF NOT EXISTS MOVIE
                         (movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                         imdb_id INTEGER,
                         movie_name TEXT,
                         creator INTEGER,
                         upvotes INTEGER,
                         downvotes INTEGER,
                         approved INTEGER,
                         declined INTEGER,
                         deleted INTEGER,
                         FOREIGN KEY(creator) REFERENCES USER (user_id))''')


def insert_movie(connection, movie):
    """
    @type connection: Connection
    @type movie: Movie
    """
    connection.execute('INSERT INTO MOVIE (imdb_id, movie_name, creator, upvotes, downvotes, approved, declined, deleted)'
                         'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                         (movie.imdb_id,
                          movie.movie_name,
                          movie.creator,
                          movie.upvotes,
                          movie.downvotes,
                          int(movie.approved),
                          int(movie.declined),
                          int(movie.deleted)))
