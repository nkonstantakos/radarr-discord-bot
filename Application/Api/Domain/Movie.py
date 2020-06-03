from Application.Api.Domain.PlexUser import PlexUser


class Movie(object):
    def __init__(self,
                 movie_id: int,
                 imdb_id: str,
                 movie_name: str,
                 creator: PlexUser,
                 approved: bool,
                 declined: bool,
                 deleted: bool,
                 private: bool,
                 channel_id: str,
                 trakt_id: str):
        self.movie_id: int = movie_id
        self.imdb_id: str = imdb_id
        self.movie_name: str = movie_name
        self.creator: PlexUser = creator
        self.approved: bool = approved
        self.declined: bool = declined
        self.deleted: bool = deleted
        self.private: bool = private
        self.channel_id: str = channel_id
        self.trakt_id: str = trakt_id
