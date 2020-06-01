from Application.Domain.Vote import Vote
from sqlite3 import Connection


def insert_vote(connection, vote):
    """
    @type connection: Connection
    @type vote: Vote
    """
    connection.execute('INSERT INTO VOTES (creator, movie_id, direction)'
                       'VALUES (?, ?, ?)',
                       (vote.creator,
                        vote.movie_id,
                        int(vote.direction)))
