from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB = 'dojos_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_ninjas(cls):
        query = """
        SELECT * FROM ninjas;
        """

        results = connectToMySQL(cls.DB).query_db(query)

        all_ninjas = []

        for ninja in results:
            all_ninjas.append(cls(ninja))

        return all_ninjas
    
    @classmethod
    def get_one_ninjas(cls, data):
        query = """
        SELECT * FROM ninjas
        WHERE id = %(ninja_id)s;
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        return cls(results[0])
    
    @classmethod
    def add_ninjas(cls, data):
        query = """
        INSERT INTO ninjas (dojo_id, first_name, last_name,
        age)
        VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s,
        %(age)s);
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        return results