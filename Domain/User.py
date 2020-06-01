class User(object):
    def __init__(self,
                 user_id,
                 discord_id,
                 nickname,
                 moderator,
                 admin):
        self.user_id = user_id
        self.discord_id = discord_id
        self.nickname = nickname
        self.moderator = moderator
        self.admin = admin
