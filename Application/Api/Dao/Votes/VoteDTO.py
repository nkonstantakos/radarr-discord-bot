from Application.Api.Domain.PlexUser import PlexUser
from Application.Api.Domain.Vote import Vote


class VoteDTO(Vote):
    def __init__(self,
                 vote_id,
                 creator,
                 movie_id,
                 direction,
                 creator_id,):
        self.vote_id: int = vote_id
        self.creator: PlexUser = creator
        self.movie_id: int = movie_id
        self.direction: bool = direction
        self.creator_id: int = creator_id
