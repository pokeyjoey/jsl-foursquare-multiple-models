import requests
from settings import CLIENT_ID, CLIENT_SECRET, DATE

class Client:
    CLIENT_ID = CLIENT_ID
    CLIENT_SECRET = CLIENT_SECRET
    DATE = DATE
    URL = "https://api.foursquare.com/v2/venues/search"
    SHOW_URL = "https://api.foursquare.com/v2/venues"

    def auth_params(self):
        return {'client_id': self.CLIENT_ID,
                   'client_secret': self.CLIENT_SECRET,
                   'v': self.DATE}

    def full_params(self, query_params = {'ll': "40.7,-74", "query": "tacos"}):
        params = self.auth_params().copy()
        params.update(query_params)
        return params

    def request_venues(self, query_params = {'ll': "40.7,-74", "query": "tacos"}):
        response = requests.get(self.URL, self.full_params(query_params))
        return response.json()['response']['venues']

    def request_venue(self, venue_id):
        response = requests.get(f"{self.SHOW_URL}/{venue_id}", self.auth_params())
        return response.json()['response']['venue']

