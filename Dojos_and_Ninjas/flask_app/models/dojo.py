from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__ (self, data):
        self.id = data ['id']
        self.name = data ['name']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO dojos (name, created_at, updated_at)
        VALUES (%(name)s, NOW(), NOW());
        """
        dojo_id = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        return dojo_id

    @classmethod
    def get_every(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)

        all_dojos = []

        for row in results:
            all_dojos.append(cls(row))

        return all_dojos

    @classmethod
    def get_single(cls, data):
        pass

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        pass