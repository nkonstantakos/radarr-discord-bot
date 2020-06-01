class Movie(object):
    def __init__(self,
                 movie_id,
                 imdb_id,
                 movie_name,
                 creator,
                 upvotes,
                 downvotes,
                 approved,
                 declined,
                 deleted):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.movie_name = movie_name
        self.creator = creator
        self.upvotes = upvotes
        self.downvotes = downvotes
        self.approved = approved
        self.declined = declined
        self.deleted = deleted
