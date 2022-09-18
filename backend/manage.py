from api.models.venue import Venue
from api.adapters.client import Client
from api.adapters.venue_builder import VenueBuilder
from api.adapters.category_builder import CategoryBuilder
from api.adapters.builder import Builder
from api.lib.db import conn, cursor

def run(conn, cursor, search_params = {'ll': "40.7,-74", "query": "tacos"}):
    venues = []
    client = Client()
    venue_responses = client.request_venues(search_params)
    for venue_response in venue_responses:
        venue_response = client.request_venue(venue_response['id'])
        builder = VenueBuilder(venue_response)
        venue = builder.run(conn, cursor)
        if not venue.exists:
            builder = CategoryBuilder(venue_response)
            categories = builder.run(venue_response, venue, conn, cursor)
        venues.append(venue)
    return venues


# def run(search_params = {'ll': "40.7,-74", "query": "tacos"}, conn, cursor):
#     client = Client()
#     builder = Builder()
#     venues = client.request_venues(search_params)
#     venue_foursquare_ids = [venue['id'] for venue in venues]
#     venue_objs = []
#     for foursquare_id in venue_foursquare_ids:
#         venue_details = client.request_venue(foursquare_id)
#         venue_obj = builder.run(venue_details, conn, cursor)
#         venue_objs.append(venue_obj)
#     return venue_objs
