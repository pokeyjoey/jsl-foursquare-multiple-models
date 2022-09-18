import api.lib.db as db
import api.lib.orm as build_from_record
import api.models as models

class VenueCategory:
    __table__ = 'venue_categories'
    columns = ['id', 'venue_id', 'category_id']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise KeyError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)

    def category(self, cursor):
        query_str = "SELECT categories.* FROM categories WHERE id = %s"
        cursor.execute(query_str, (self.venue_id,))
        record = cursor.fetchone()
        return build_from_record(models.Category, record)

    
