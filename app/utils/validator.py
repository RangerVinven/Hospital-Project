from typing import TypedDict, NotRequired
from colorama import Fore, Style

import re
from datetime import date

class TableAndColumn(TypedDict):
    table_name: str
    column_name: str

class RegexFormatMapper(TypedDict):
    regex: str
    correct_format: str

class Options(TypedDict):
    max_length: NotRequired[int]
    min_length: NotRequired[int]
    is_int: NotRequired[bool] 
    is_date: NotRequired[bool] 
    exists_in_table: NotRequired[TableAndColumn]
    unique: NotRequired[TableAndColumn]
    regex: NotRequired[RegexFormatMapper]

# Maps a column (i.e, patient_id) with the validation Options for that column
class ColumnOptionMapper(TypedDict):
    column_name: str
    options: Options

class Validator():

    def __init__(self):
        pass

    def prompt_user(self, input_message):
        return input(Fore.MAGENTA + "\n" + input_message + "\n")

    def get_input(self, database_connector, input_message: str, options: Options):
        user_input = self.prompt_user(input_message)

        # Allows for a blank input
        if "can_be_blank" in options:
            if user_input == "":
                return user_input

        # Loops until the user enters something short enough
        elif "max_length" in options:
            while len(user_input) > options["max_length"]:
                print(Fore.RED + "That's too long. The maximum length is {}".format(options["max_length"]))
                user_input = self.prompt_user(input_message)

        # Loops until the user enters something long enough
        if "min_length" in options:
            while len(user_input) < options["min_length"]:
                print(Fore.RED + "That's too short. The minimum length is {}".format(options["min_length"]))
                user_input = self.prompt_user(input_message)

        # Ensures the input is an integer
        if "is_int" in options:
            if options["is_int"]:
                incorrect_data_type = True

                # Loops until the user enters an int
                while incorrect_data_type:
                    try:
                        int(user_input)  # Throws exception if the input isn't an integer
                        incorrect_data_type = False

                    except ValueError:
                        print(Fore.RED + "Input type must be an integer (whole number).")
                        user_input = self.prompt_user(input_message)

        # Ensures the item exists in the database (i.e, used when entering foreign keys)
        if "exists_in_table" in options:
            table = options["exists_in_table"]["table_name"]
            column = options["exists_in_table"]["column_name"]

            # Create the query
            query = "SELECT {} FROM {} WHERE {} = %s;".format(column, table, column)

            # Searches for the item in the table
            database_connector.cursor.execute(query, (user_input,))
            results = database_connector.cursor.fetchall()

            # Loops until the user enters something that exists in the table
            while len(results) == 0:
                print(Fore.RED + "Couldn't find that in the {} table.".format(table))
                user_input = self.prompt_user(input_message)
                
                database_connector.cursor.execute(query, (user_input,))
                results = database_connector.cursor.fetchall()

        if "unique" in options:
            table = options["unique"]["table_name"]
            column = options["unique"]["column_name"]

            # Create the query
            query = "SELECT {} FROM {} WHERE {} = %s;".format(column, table, column)

            # Searches for the item in the table
            database_connector.cursor.execute(query, (user_input,))
            results = database_connector.cursor.fetchall()

            # Loops until the user enters something that exists in the table
            while len(results) != 0:
                print(Fore.RED + "That already exists in the {} table. It must be unique.".format(table))
                user_input = self.prompt_user(input_message)
                
                database_connector.cursor.execute(query, (user_input,))
                results = database_connector.cursor.fetchall()

        # Loops until the user enters the correct format
        if "regex" in options:
            regex = options["regex"]["regex"]
            correct_format = options["regex"]["correct_format"]  # Displayed to the user if they enter the wrong format

            # While the regex pattern isn't found in the input
            while not re.search(regex, user_input):
                print(Fore.RED + "Invalid format. The correct format is {}.".format(correct_format))
                user_input = self.prompt_user(input_message)

        
        if "is_date" in options:
            if options["is_date"]:
                incorrect_format = True

                # Loops until the user enters a correct date
                while incorrect_format:
                    try:
                        date.fromisoformat(user_input)
                        incorrect_format = False
                    
                    except ValueError:
                        print(Fore.RED + "Invalid date. Must be a valid date in the YYYY-MM-DD format")
                        user_input = self.prompt_user(input_message)

        # Resets the terminal colour
        print(Style.RESET_ALL)
        return user_input
        