class Movie(object):
    def __init__(self,
                 movie_id,
                 imdb_id,
                 movie_name,
                 creator,
                 approved,
                 declined,
                 deleted,
                 private):
        self.movie_id: int = movie_id
        self.imdb_id: str = imdb_id
        self.movie_name: str = movie_name
        self.creator: int = creator
        self.approved: bool = approved
        self.declined: bool = declined
        self.deleted: bool = deleted
        self.private: bool = private
