class Vote(object):
    def __init__(self,
                 vote_id,
                 creator,
                 movie_id,
                 direction):
        self.vote_id: int = vote_id
        self.creator: int = creator
        self.movie_id: int = movie_id
        self.direction: bool = direction
