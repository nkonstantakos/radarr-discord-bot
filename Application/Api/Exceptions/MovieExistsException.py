class MovieExistsException(Exception):
    def __init__(self, movie_name: str, creator_name: str):
        self.movie_name: str = movie_name
        self.creator_name: str = creator_name
        super().__init__(movie_name + ' has already been added by ' + creator_name + '!')
