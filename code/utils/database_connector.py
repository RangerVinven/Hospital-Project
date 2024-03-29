import mysql.connector

class DatabaseConnector():
    def __init__(self, database_to_connect_to: str):
        
        # Initialises the variables
        self.username = "root"
        self.password = "root"
        self.host = "127.0.0.1"
        self.database_name = "Hospital"

        # Connects to either the development or the testing database
        if database_to_connect_to == "development":
            self.port = "3000"
        
        else:
            self.port = "4000"

        self.connect_to_database()

    # Connects to the database
    def connect_to_database(self):
        self.db = mysql.connector.connect(user=self.username, password=self.password, host=self.host, port=self.port, database=self.database_name)
        self.cursor = self.db.cursor(dictionary=True)

database_connector = DatabaseConnector("development")