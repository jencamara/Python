from flask import flash

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Recipe:
    def __init__ (self, data):
        self.id = data ['id']

        if data['user_id']: 
            self.user = user.User.pull_from_id({"id": data['user_id']})
        self.name = data ['name']
        self.time= data ['time']
        self.description = data ['description']
        self.instruction = data ['instruction']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        


    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO recipes (user_id, name, time, description, instruction, created_at, updated_at)
            VALUES (%(user_id)s, %(name)s, %(time)s, %(description)s, %(instruction)s, NOW(), NOW());
        """

        return connectToMySQL("users_and_recipes_schema").query_db(query, data)
        

    @classmethod
    def get_every(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL("users_and_recipes_schema").query_db(query)

        recipes = []
        for row in results:
            recipes.append(cls(row))

        return recipes

    @classmethod
    def get_single(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL("users_and_recipes_schema").query_db(query, data)

        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = """
            UPDATE recipes SET name = %(name)s, time = %(time)s, description = %(description)s, instruction = %(instruction)s,
            updated_at = NOW() WHERE id = %(id)s;
        """
        return connectToMySQL("users_and_recipes_schema").query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL("users_and_recipes_schema").query_db(query, data)

    @staticmethod
    def validate(post_data):
        is_valid = True

        if len(post_data['name']) < 3:
            flash("Name must have at least 3 characters.")
            is_valid = False
        
        if len(post_data['description']) < 3:
            flash("Description of the recipe must have at least 3 characters.")
            is_valid = False
        
        if len(post_data['instruction']) < 3:
            flash("Instructions of the recipe must have at least 3 characters.")
            is_valid = False
        
        return is_valid
        
