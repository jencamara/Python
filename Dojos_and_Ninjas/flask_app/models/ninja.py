from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__ (self, data):
        self.id = data ['id']
        self.dojo_id = data ['dojo_id']
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
        pass

    @classmethod
    def get_one(cls, data):
        pass

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        pass
