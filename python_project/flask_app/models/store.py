from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import item

class Store:
    def __init__ (self, data):
        self.id = data ['id']
        self.store_name = data ['store_name']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.items =[]

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO stores (store_name, created_at, updated_at)
        VALUES (%(store_name)s, NOW(), NOW());
        """
        store_id = connectToMySQL("stores_and_items_schema").query_db(query, data)

        return store_id

    @classmethod
    def get_every(cls):
        query = "SELECT * FROM stores;"
        results = connectToMySQL("stores_and_items_schema").query_db(query)

        all_stores = []

        for row in results:
            all_stores.append(cls(row))

        return all_stores

    @classmethod
    def get_single(cls, data):
        query = "SELECT * FROM stores LEFT JOIN items ON stores.id = items.store_id WHERE stores.id = %(id)s;"
        results = connectToMySQL("stores_and_items_schema").query_db(query, data)

        print(results)

        store = cls(results[0])

        for row in results:
            row_data = {
                "id": row['items.id'],
                "item_name": row['item_name'],
                "description": row['description'],
                "note_to_self": row['note_to_self'],
                "created_at": row['items.created_at'],
                "updated_at": row['items.updated_at']
            }
            store.items.append(item.Item(row_data))

        return store

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM stores WHERE id = %(id)s;"
        return connectToMySQL("stores_and_items_schema").query_db(query, data)
