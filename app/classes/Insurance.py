from utils.id_generator import IDGenerator
from utils.query_builder import QueryBuilder
from utils.record_manager import RecordManager

class Insurance():
    def __init__(self, database_connector, company, address, phone):
       self.insurance_id = IDGenerator.generate_id(database_connector, 7, True, True, "Insurance", "insuranceID")
       self.company = company
       self.address = address
       self.phone = phone

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
        id = input("Please enter the ID of the insurance you wish to search for (leave blank if unknown): ") or ""
        company = input("Please enter the company name you wish to search for (leave blank if unknown): ") or ""
        address = input("Please enter the address you wish to search for (leave blank if unknown): ") or ""
        phone = input("Please enter the phone number you wish to search for (leave blank if unknown): ") or ""

        query, variables = QueryBuilder.create_find_query("Insurance", ("insuranceID", "company", "address", "phone"), (id, company, address, phone))

        # Executes the query
        database_connector.cursor.execute(query, tuple(variables))        
        RecordManager.print_records(database_connector.cursor.fetchall())
    
    @staticmethod
    def update_insurance(database_connector):

        # Gets the new item details
        insurance_id = input("Enter the ID of the insurance company you want to update: ")
        company = input("Enter the new company name (leave blank for no change): ") or ""
        address = input("Enter the new company name (leave blank for no change): ") or ""
        phone = input("Enter the new company name (leave blank for no change): ") or ""

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