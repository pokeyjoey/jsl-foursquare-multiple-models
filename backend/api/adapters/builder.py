from api.adapters.venue_builder import VenueBuilder
from api.adapters.category_builder import CategoryBuilder
class Builder:
    def run(self, venue_details, conn, cursor):
        venue = VenueBuilder().run(venue_details, conn, cursor)
        if venue.exists:
            return venue
        else:
            venue_categories = CategoryBuilder().run(venue_details, venue, conn, cursor)
            return {'venue': venue, 'venue_categories': venue_categories}