class PlexUser(object):
    def __init__(self,
                 user_id,
                 discord_id,
                 nickname,
                 moderator,
                 admin):
        self.user_id: int = user_id
        self.discord_id: int = discord_id
        self.nickname: str = nickname
        self.moderator: bool = moderator
        self.admin: bool = admin
