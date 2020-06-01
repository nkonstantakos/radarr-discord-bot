from trakt import Trakt
import configparser
import logging
from Trakt.Auth import TraktAuthenticator


class TraktManager(object):
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        self.config = configparser.ConfigParser()
        self.config.read('properties.ini')
        self.user_account = self.config['TRAKT']['userAccount']
        self.list_name = self.config['TRAKT']['listName']
        Trakt.configuration.defaults.oauth.from_response(
            TraktAuthenticator.authenticate()
        )

    def add_movie(self, movie):
        Trakt[self.get_list_path()].add({
            'movies': [
                {
                    'ids': {
                        'imdb': movie.imdb_id
                    }
                }
            ]
        })

    def get_list_path(self):
        return 'users/{0}/lists/{1}'.format(self.user_account, self.list_name)

