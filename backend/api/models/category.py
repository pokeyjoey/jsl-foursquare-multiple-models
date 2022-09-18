import api.lib.db as db
from api.lib.orm import save, build_from_record
import api.models as models

class Category:
    __table__ = 'categories'
    columns = ['id', 'name']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}'
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def find_by_name(self, name, cursor):
        category_query = """SELECT * FROM categories WHERE name = %s """
        cursor.execute(category_query, (name,))
        category_record =  cursor.fetchone()
        category = build_from_record(self, category_record)
        return category

    @classmethod
    def find_or_create_by_name(self, name, conn, cursor):
        category = self.find_by_name(name, cursor)
        if not category:
            new_category = models.Category(name = name)
            category = save(new_category, conn, cursor)
        return category

    def venues(self, cursor):
        query = f"""
            SELECT v.* FROM categories c
            JOIN venue_categories vc
            ON c.id = vc.category_id
            JOIN venues v
            ON v.id = vc.venue_id
            WHERE c.id = {self.id}"""
        cursor.execute(query)
        venue_records = cursor.fetchall()
        venues = [build_from_record(models.Venue, venue)
                  for venue in venue_records]
        return venues

