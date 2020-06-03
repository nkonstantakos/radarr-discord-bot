from Application.Api.Domain.Vote import Vote
from sqlite3 import Connection, Cursor


def get_votes_for_movie(connection: Connection, movie_id: int):
    cursor = connection.cursor()
    cursor.execute('''SELECT *
                      FROM VOTES
                      WHERE movie_id = ?''', (movie_id,))
    return get_records_as_votes(cursor)


def get_records_as_votes(cursor: Cursor):
    result = cursor.fetchall()
    items = []
    for row in result:
        items.append(Vote(int(row[0]), None, str(row[2]), bool(row[3]),  int(row[1])))
    return items
