from random import randrange

class IDGenerator():

    @staticmethod
    # Generates the ID
    def generate_id(db_connector, id_length: int, hasNumbers: bool, hasLetters: bool, table, id_column_name):
        id_generator = IDGenerator()

        # Gets the characters and creates an ID
        characters = id_generator._create_character_set(hasNumbers, hasLetters)
        id = id_generator._generate_random_id(characters, id_length)

        # Keeps generating IDs until it's unique
        while not id_generator._is_unique(db_connector, table, id_column_name, id):
            print("ID {} not unique".format(id))
            id = id_generator._generate_random_id(characters, id_length)

        return id

    # Gets the characters needed for the ID
    def _create_character_set(self, hasNumbers: bool, hasLetters: bool):
        # Gets all the numbers and letters
        numbers = "1234568790"
        letters = "abcdefghijklmnopqrstuvwxyz"
        letters = letters + letters.capitalize()

        character_set = ""

        # Adds the numbers to the available characters
        if hasNumbers:
            character_set += numbers
        
        # Adds the letters to the available characters
        if hasLetters:
            character_set += letters

        return character_set

    # Generates the ID
    def _generate_random_id(self, characters, id_length):
        id = ""

        # Generates the id
        for _ in range(id_length):
            id += characters[randrange(0, len(characters))]

        return id
    
    # Checks if the ID is unique
    def _is_unique(self, db_connector, table, id_column_name, id):
        query = "SELECT {} FROM {} WHERE {} = %s;".format(id_column_name, table, id_column_name)

        db_connector.cursor.execute(query, (id,))

        # Checks if the ID is unique
        if len(db_connector.cursor.fetchall()) == 0:
            return True
        
        return False