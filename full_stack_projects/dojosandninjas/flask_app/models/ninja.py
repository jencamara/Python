from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    def __init__ (self, data):
        self.id = data ['id']
        
        if "dojo_id" in data: 
            self.dojo = dojo.Dojo.get_single({"id": data['dojo_id']})
        self.first_name = data ['first_name']
        self.last_name = data ['last_name']
        self.age = data ['age']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
            VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());
        """

        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        # the query returns the ninjas id

    @classmethod
    def get_every(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)

        ninjas = []
        for row in results:
            ninjas.append(cls(row))

        return ninjas

    @classmethod
    def get_single(cls, data):
        pass

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        pass
