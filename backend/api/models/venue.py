import api.lib.db as db
from api.lib.orm import build_from_record
import api.models as models

class Venue:
    columns = ['id', 'foursquare_id', 'name', 'price',
            'rating', 'likes', 'menu_url']
    __table__ = 'venues'
    
    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def find_by_foursquare_id(self, foursquare_id, conn):
        cursor = conn.cursor()
        cursor.execute('SELECT * from venues where foursquare_id = %s', (foursquare_id,))
        record = cursor.fetchone()
        if not record: 
            return None
        else:
            return build_from_record(Venue, record)

    def categories(self, cursor):
        query = f"""
            SELECT c.* FROM venues v
            JOIN venue_categories vc
            ON v.id = vc.venue_id
            JOIN categories c
            ON c.id = vc.category_id
            WHERE v.id = {self.id}
        """
        cursor.execute(query)
        category_records = cursor.fetchall()
        categories = [
            build_from_record(models.Category, category)
            for category in category_records]

        return categories
 
