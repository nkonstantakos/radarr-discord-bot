from Application.Api.Domain.Vote import Vote
from sqlite3 import Connection


def insert_vote(connection: Connection, vote: Vote):
    connection.execute('INSERT INTO VOTES (creator_id, movie_id, direction)'
                       'VALUES (?, ?, ?)',
                       (vote.creator,
                        vote.movie_id,
                        int(vote.direction)))
