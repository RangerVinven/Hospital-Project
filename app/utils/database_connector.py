import mysql.connector
from colorama import Fore, Style
from time import sleep

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
        connected = False
        while not connected:
            try:
                self.db = mysql.connector.connect(user=self.username, password=self.password, host=self.host, port=self.port, database=self.database_name)
                self.cursor = self.db.cursor(dictionary=True, buffered=True)
                print(Fore.GREEN + "Connected to the database!")
                connected = True
            
            except Exception as e:
                print(Fore.RED + "Could not connect to the database. If this persists, contact IT. Retrying in 3 seconds..." + Style.RESET_ALL)
                sleep(3) 

    def close_connection(self):
        self.cursor.close()
        self.db.close()

database_connector = DatabaseConnector("development")