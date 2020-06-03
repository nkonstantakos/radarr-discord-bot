from trakt import Trakt
import pickle
import json


class TraktAuthenticator(object):
    def __init__(self, config):
        self.config = config
        self.authorization = None
        self.auth_filename = self.config['TRAKT']['auth_filename']
        self.load_auth_file()

        Trakt.configuration.defaults.client(
            id=self.config['TRAKT']['clientId'],
            secret=self.config['TRAKT']['clientSecret']
        )

    def authenticate(self, pin: str):
        auth_url = self.config['TRAKT']['authUrl']

        if not pin:
            exit(1)

        self.authorization = Trakt['oauth'].token_exchange(pin, auth_url)
        if not self.authorization:
            exit(1)
        self.populate_auth_file()
        return self.authorization

    def load_auth_file(self):
        auth_file = open(self.auth_filename, "rb")
        self.authorization = pickle.load(auth_file)
        auth_file.close()

    def populate_auth_file(self):
        auth_file = open("trakt_auth.pkl", "wb")
        pickle.dump(self.authorization, auth_file)
        auth_file.close()
