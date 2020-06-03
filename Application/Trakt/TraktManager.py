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
        auth = self.trakt_authenticator.authenticate(pin)
        Trakt.configuration.defaults.oauth.from_response(auth)
        return auth is not None

    def search_movie(self, imdb_id):
        results = Trakt['search'].lookup(imdb_id, 'imdb', 'movie')
        return results

    def add_movie(self, movie):
        try:
            return Trakt[self.get_list_path()].add({
                'movies': [
                    {
                        'ids': {
                            'trakt': movie.trakt_id
                        }
                    }
                ]
            })
        except Exception as e:
            print(e)

    def get_list_path(self):
        return 'users/{0}/lists/{1}'.format(self.user_account, self.list_name)

