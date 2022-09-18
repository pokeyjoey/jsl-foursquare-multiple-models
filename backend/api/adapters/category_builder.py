from api.models import Category, VenueCategory
from api.lib.orm import save, find_or_create_by_name
class CategoryBuilder:

    def __init__(self, response_venue):
        self._response_venue = response_venue

    @property
    def response_venue(self):
        return self._response_venue

    @response_venue.setter
    def response_venue(self, response_venue):
        self._response_venue = response_venue

    def select_attributes(self):
        category_names = [category['name'] for category in self.response_venue['categories']]

        return category_names

    def find_or_create_categories(self, names, conn, cursor):
        categories = [find_or_create_by_name(Category, name, conn, cursor) for name in names]

        return categories

    def create_venue_categories(self, venue, categories, conn, cursor):
        # create venue category objects
        venue_categories = [
            VenueCategory(category_id = category.id,
                venue_id=venue.id)
                for category in categories]

        # save the objects in the category_venue table
        [save(venue_category, conn, cursor)
            for venue_category in venue_categories]

    def run(self, venue_details, venue, conn, cursor):
        category_names = self.select_attributes()
        categories = self.find_or_create_categories(category_names, conn, cursor)
        venue_categories = self.create_venue_categories(venue, categories, conn, cursor)
        return venue_categories
