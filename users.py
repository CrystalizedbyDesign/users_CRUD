# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the user table from our database
class User:
    
    # import the function that will return an instance of a connection
    def __init__( self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.full_name = data['full_name']
        
        
        
    def full_name(self):
        return (f"{self.first_name} {self.last_name}")    
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db(query)
        print(results, "you made it here")
        all_users = []
        for user in results:
            #Make an object
            all_users.append(cls(user))  #Add to a list
        return all_users    
    
    @classmethod
    def save(cls, data):
        query = '''INSERT INTO users (first_name, last_name, email)
        VALUES %(first_name)s, %(last_name)s, %(email)s;'''
        # returns as the new row id
        result = connectToMySQL('users_schema').query_db(query, data) # data is a dictionary that will be passed into the save method from server.py
        print(result, "This is the saved info ##################################")
        return result
    
    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query,data)
        print("#############")
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query = """UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(emails)s, updated_at=NOW() 
        WHERE id = %(id)s;"""
        
        print("test you made it to updates ##########################3")
        return connectToMySQL('users_schema').query_db(query, data)
    
    @classmethod
    def delete(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        print("YOU MADE IT HERE ********************************************")
        
        return connectToMySQL('users_schema').query_db(query,data)
    
    
