from Application.Api.Domain.Vote import Vote
from sqlite3 import Connection


def get_votes_for_movie(connection, movie):
    """
    @type connection: Connection
    @type movie: Movie
    """
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM VOTES
                      WHERE movie_id = ?''', movie.movie_id)
    return get_records_as_votes(cursor)


def get_records_as_votes(cursor):
    """
    @type cursor: Cursor
    """
    result = cursor.fetchall()
    items = []
    for row in result:
        items.append(Vote(int(row[0]), int(row[1]), str(row[2]), bool(row[3])))
    return items
