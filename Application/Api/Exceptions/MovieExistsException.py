class MovieExistsException(Exception):
    def __init__(self, imdb_id: str):
        self.imdb_id = imdb_id
        super().__init__(imdb_id + ' has already been added!')
