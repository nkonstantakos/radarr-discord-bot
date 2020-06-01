import configparser
from trakt import Trakt
import json
import six


class TraktAuthenticator(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('properties.ini')

        Trakt.configuration.defaults.client(
            id=self.config['TRAKT']['clientId'],
            secret=self.config['TRAKT']['clientSecret']
        )

    def authenticate(self):
        authorization = self.config['TRAKT']['authentication']
        print(authorization)

        if authorization:
            return json.loads(authorization)

        auth_url = self.config['TRAKT']['authUrl']
        print('Navigate to: %s' % Trakt['oauth'].authorize_url(auth_url))

        code = six.moves.input('Authorization code:')
        if not code:
            exit(1)

        authorization = Trakt['oauth'].token_exchange(code, auth_url)
        if not authorization:
            exit(1)

        return authorization
