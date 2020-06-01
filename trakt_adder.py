import discord
import sys
import configparser
from trakt import Trakt
import logging
import json
import six

config = configparser.ConfigParser()
config.read('properties.ini')

Trakt.configuration.defaults.client(
    id=config['TRAKT']['clientId'],
    secret=config['TRAKT']['clientSecret']
)


def run():
    logging.basicConfig(level=logging.DEBUG)
    Trakt.configuration.defaults.oauth.from_response(
        authenticate()
    )
    print(Trakt['sync/collection'].movies())


def authenticate():
    global config
    authorization = config['TRAKT']['authentication']
    print(authorization)

    if authorization:
        print('Already had it!')
        return json.loads(authorization)

    print('Navigate to: %s' % Trakt['oauth'].authorize_url('urn:ietf:wg:oauth:2.0:oob'))

    code = six.moves.input('Authorization code:')
    if not code:
        exit(1)

    authorization = Trakt['oauth'].token_exchange(code, 'urn:ietf:wg:oauth:2.0:oob')
    if not authorization:
        exit(1)

    return authorization


run()
