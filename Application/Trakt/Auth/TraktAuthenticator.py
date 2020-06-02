import configparser
from trakt import Trakt
import json
import six


class TraktAuthenticator(object):
    def __init__(self, config):
        self.config = config
        self.authorization = None

        Trakt.configuration.defaults.client(
            id=self.config['TRAKT']['clientId'],
            secret=self.config['TRAKT']['clientSecret']
        )

    def authenticate(self):
        if self.authorization:
            return json.loads(self.authorization)

        auth_url = self.config['TRAKT']['authUrl']
        print('Navigate to: %s' % Trakt['oauth'].authorize_url(auth_url))

        code = six.moves.input('Authorization code:')
        if not code:
            exit(1)

        self.authorization = Trakt['oauth'].token_exchange(code, auth_url)
        if not self.authorization:
            exit(1)

        return self.authorization
