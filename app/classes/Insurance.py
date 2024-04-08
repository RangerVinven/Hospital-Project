from utils.id_generator import IDGenerator
from utils.query_builder import QueryBuilder
from utils.record_manager import RecordManager
from utils.validator import Validator, ColumnOptionMapper, RegexFormatMapper

class Insurance():
    def __init__(self, database_connector):
        self.validator = Validator() 
        self.column_options = {
            "insurance_id": { "max_length": 7 },
            "company": { "max_length": 45 },
            "address": { "max_length": 50 },
            "phone": { "max_length": 14, "regex": RegexFormatMapper(regex="^\d\d\d-\d\d\d-\d\d\d\d", correct_format="###-###-####") },
        }
    
        self.insurance_id = IDGenerator.generate_id(database_connector, 7, True, True, "Insurance", "insuranceID")
        self.company = self.validator.get_input(database_connector, "What's the insurance's company name? ", self.column_options["company"])
        self.address = self.validator.get_input(database_connector, "What's the insurance's address? ", self.column_options["address"])
        self.phone = self.validator.get_input(database_connector, "What's the insurance's phone number? ", self.column_options["phone"])


        self._create_insurance(database_connector)
       
    # Inserts the insurance into the table
    def _create_insurance(self, database_connector): 
        database_connector.cursor.execute("INSERT INTO Insurance (insuranceID, company, address, phone) VALUES (%s, %s, %s, %s);", (self.insurance_id, self.company, self.address, self.phone))
        database_connector.db.commit()

    # Returns all the insurance companies
    @staticmethod
    def list_insurance(database_connector):
        database_connector.cursor.execute("SELECT * FROM Insurance;")
        RecordManager.print_records(database_connector.cursor.fetchall())

    # Returns a specific insurance company details
    @staticmethod
    def find_insurance(database_connector):
        # Gets the items the user wishes to change
        id = input("Please enter the ID of the insurance you wish to search for (leave blank if unknown): ")
        company = input("Please enter the company name you wish to search for (leave blank if unknown): ")
        address = input("Please enter the address you wish to search for (leave blank if unknown): ")
        phone = input("Please enter the phone number you wish to search for (leave blank if unknown): ")

        query, variables = QueryBuilder.create_find_query("Insurance", ("insuranceID", "company", "address", "phone"), (id, company, address, phone))

        # Executes the query
        database_connector.cursor.execute(query, tuple(variables))        
        RecordManager.print_records(database_connector.cursor.fetchall())
    
    @staticmethod
    def update_insurance(database_connector):

        # Gets the new item details
        insurance_id = self.validator.get_input(database_connector, "Enter the ID of the insurance company you want to update: ", self.column_options["insurance_id"])
        company = self.validator.get_input(database_connector, "Enter the new company name (leave blank for no change): ", self.column_options["company"])
        address = self.validator.get_input(database_connector, "Enter the new company address (leave blank for no change): ", self.column_options["address"])
        phone = self.validator.get_input(database_connector, "Enter the new company phone (leave blank for no change): ", self.column_options["phone"])

        query, variables = QueryBuilder.create_update_query("Insurance", ["insuranceID"], [insurance_id], ("company", "address", "phone"), (company, address, phone))

        # Executes the query
        database_connector.cursor.execute(query, tuple(variables))

        RecordManager.is_row_changed(database_connector, "Insurance updated", "No insurance found, nothing was updated")
        database_connector.db.commit()
   
    # Deletes a specific insurance company
    def delete_insurance(database_connector):
        insurance_id = input("Please enter the id of the insurance you wish to delete: ")
        database_connector.cursor.execute("DELETE FROM Insurance WHERE insuranceID=%s", (insurance_id,))
        
        RecordManager.is_row_changed(database_connector, "Insurance deleted", "No insurance found, nothing was deleted")
        database_connector.db.commit()