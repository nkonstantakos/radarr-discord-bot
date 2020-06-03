from trakt import Trakt
import logging
from Application.Trakt.Auth.TraktAuthenticator import TraktAuthenticator
import configparser


class TraktManager(object):
    def __init__(self, config: configparser.ConfigParser):
        logging.basicConfig(level=logging.DEBUG)
        self.config = config
        self.user_account = self.config['TRAKT']['userAccount']
        self.list_name = self.config['TRAKT']['listName']
        self.trakt_authenticator = TraktAuthenticator(config)

    def authenticate(self, pin: str):
        Trakt.configuration.defaults.oauth.from_response(
            self.trakt_authenticator.authenticate(pin)
        )

    def search_movie(self, imdb_id):
        results = Trakt['search'].lookup(imdb_id, 'imdb', 'movie')
        print(results)
        return results

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

