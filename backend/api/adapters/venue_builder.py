from api.models.venue import Venue
from api.lib.orm import save
class VenueBuilder:
    def __init__(self, response_venue):
        self.response_venue = response_venue

    def select_attributes(self):
        foursquare_id = self.response_venue['id']
        venue_name = self.response_venue['name']
        
        price = self.response_venue.get('price', {'tier': None}).get('tier', None)
        
        likes = self.response_venue['likes']['count']
        menu_url = self.response_venue.get('delivery', '')
        if menu_url:
            menu_url = menu_url.get('url', '').split('?')[0]
        rating = self.response_venue.get('rating', None)
        vals = [foursquare_id, venue_name, price, rating, likes, menu_url]
        keys = ['foursquare_id', 'name', 'price', 'rating', 'likes', 'menu_url']
        attr = dict(zip(keys, vals))
        return attr

    def run(self, conn, cursor):
        venue = Venue.find_by_foursquare_id(self.response_venue['id'], conn)
        if venue:  
            venue.exists = True
        else:
            attr = self.select_attributes()
            venue = Venue(**attr)
            venue = save(venue, conn, cursor)
            venue.exists = False
        return venue

