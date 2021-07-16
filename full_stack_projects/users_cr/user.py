from mysqlconnection import connectToMySQL

class User:
    def __init__ (self , data):
        self.id = data ['id']
        self.first_name = data ['first_name']
        self.last_name = data ['last_name']
        self.email = data ['email']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email, created_at, updated_at) 
            VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW()); 
        """
        connectToMySQL("users_schema")

    @classmethod
    def get_every(cls):
        pass

    @classmethod
    def get_single(cls, data):
        pass

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        pass