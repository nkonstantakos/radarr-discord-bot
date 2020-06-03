from Application.Api.Domain.Movie import Movie


class MovieDTO(Movie):
    def __init__(self,
                 movie_id,
                 imdb_id,
                 movie_name,
                 approved,
                 declined,
                 deleted,
                 private,
                 channel_id,
                 trakt_id,
                 votes,
                 creator_id):
        super(MovieDTO, self).__init__(movie_id, imdb_id, movie_name, None, approved, declined,
                                       deleted, private, channel_id, trakt_id, votes)
        self.creator_id = creator_id
