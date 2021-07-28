from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import store

class Item:
    def __init__ (self, data):
        self.id = data ['id']
        
        if "store_id" in data: 
            self.store = store.Store.get_single({"id": data['store_id']})
        self.item_name = data ['item_name']
        self.description = data ['description']
        self.note_to_self = data ['note_to_self']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO items (store_id, item_name, description, note_to_self, created_at, updated_at)
            VALUES (%(store_id)s, %(item_name)s, %(description)s, %(note_to_self)s, NOW(), NOW());
        """

        return connectToMySQL("stores_and_items_schema").query_db(query, data)
        

    @classmethod
    def get_every(cls):
        query = "SELECT * FROM items;"
        results = connectToMySQL("stores_and_items_schema").query_db(query)

        items = []
        for row in results:
            items.append(cls(row))

        return items

    @classmethod
    def get_single(cls, data):
        query = "SELECT * FROM items WHERE id = %(id)s;"
        results = connectToMySQL("stores_and_items_schema").query_db(query, data)

        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = """
            UPDATE items SET item_name = %(item_name)s, description = %(description)s, note_to_self = %(note_to_self)s,
            updated_at = NOW() WHERE id = %(id)s;
        """
        return connectToMySQL("stores_and_items_schema").query_db(query, data)


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM items WHERE id = %(id)s;"
        return connectToMySQL("stores_and_items_schema").query_db(query, data)

