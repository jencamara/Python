from flask import flash
from flask_bcrypt import Bcrypt
import re

from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL

bcrypt = Bcrypt(app)

class Client:
    schema = "client_registration_schema"
    
    def __init__(self, data):
        self.id = data ['id']
        self.first_name = data ['first_name']
        self.last_name = data ['last_name']
        self.email = data ['email']
        self.password = data ['password']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        

    @classmethod
    def get_every(cls):
        query = "SELECT * FROM clients;"
        results = connectToMySQL(cls.schema).query_db(query)

        clients =[]
        for row in results:
            clients.append(cls(row))

        return clients

    @classmethod
    def get_single(cls, data):
        query = "SELECT * FROM clients WHERE id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)

        return cls(results[0])

    @classmethod
    def select_email(cls, data):
        query = "SELECT * FROM clients WHERE email = %(email)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)

        if len(results) < 1:
            return False
        
        return cls(results[0])

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO clients (first_name, last_name, email, password, created_at, updated_at)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());
        """
        return connectToMySQL(cls.schema).query_db(query, data)

    @staticmethod
    def register_validate(post_data):
        is_valid = True

        if len(post_data['first_name']) < 2:
            flash("First name must have at least 2 letters.")
            is_valid = False
        if len(post_data['last_name']) < 2:
            flash("Last name must have at least 2 letters.")
            is_valid = False

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        if not EMAIL_REGEX.match(post_data['email']):
            flash("Not a valid email address")
            is_valid = False
        elif Client.select_email({"email": post_data['email']}):
            flash ("Email is already taken")
            is_valid = False

        if len(post_data['password']) < 8:
            flash ("Password must have at least 8 characters.")
            is_valid = False
        elif post_data['password'] != post_data['confirm_password']:
            flash("Your password and confirm password does not match")
            is_valid = False

        return is_valid

    @staticmethod
    def login_validate(post_data):
        client = Client.select_email({"email": post_data['email']})

        if not client:
            flash("this is not your account")
            return False
            
        if not bcrypt.check_password_hash(client.password, post_data['password']):
            flash("this is not your account")
            return False
            
        return True