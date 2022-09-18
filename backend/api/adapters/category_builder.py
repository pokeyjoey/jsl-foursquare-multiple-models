from api.models import Category, VenueCategory
from api.lib.orm import save, find_or_create_by_name
class CategoryBuilder:
    
    def run(self, venue_details, venue, conn, cursor):
        category_names = self.select_attributes()
        categories = self.find_or_create_categories(category_names, conn, cursor)
        venue_categories = self.create_venue_categories(venue, categories, conn, cursor)
        return venue_categories