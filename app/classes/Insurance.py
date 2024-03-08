from ..utils.id_generator import IDGenerator

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
        return database_connector.cursor.fetchall()

    # Returns a specific insurance company details
    @staticmethod
    def find_insurance(database_connector):
        # Gets the items the user wishes to change
        id = input("Please enter the ID of the insurance you wish to update (leave blank if unknown): ") or ""
        company = input("Please enter the new company name (leave blank if unknown): ") or ""
        address = input("Please enter the new address (leave blank if unknown): ") or ""
        phone = input("Please enter the new phone number (leave blank if unknown): ") or ""

        # The initial query
        query = "SELECT * FROM Insurance WHERE 1=1"
        variables = []

        # Adds the "to-be updated" variables to the query
        if id:
            query += " AND insuranceID=%s"
            variables.append(id)

        if company:
            query += " AND company=%s"
            variables.append(company)
        
        if address:
            query += " AND address=%s"
            variables.append(address)
        
        if phone:
            query += " AND phone=%s"
            variables.append(phone)

        query += ";"

        # Executes the query
        database_connector.cursor.execute(query, tuple(variables))        
        return database_connector.cursor.fetchall()
    
    @staticmethod
    def update_insurance(database_connector):

        # Gets the new item details
        insurance_id = input("Enter the ID of the insurance company you want to update: ")
        company = input("Enter the new company name (leave blank for no change): ") or ""
        address = input("Enter the new company name (leave blank for no change): ") or ""
        phone = input("Enter the new company name (leave blank for no change): ") or ""

        # Initialises the query
        query = "UPDATE Insurance SET insuranceID=%s"
        variables = [insurance_id]

        # Adds items the user wants to update
        if company:
            query += ", company=%s"
            variables.append(company)
        
        if address:
            query += ", address=%s"
            variables.append(address)

        if phone:
            query += ", phone=%s"
            variables.append(phone)

        # Finishes the query
        query += " WHERE insuranceID=%s;"
        variables.append(insurance_id)

        print(query)
        print(variables)

        # Executes the query
        database_connector.cursor.execute(query, tuple(variables))
        database_connector.db.commit()

    
   
    # Deletes a specific insurance company
    def delete_insurance(database_connector, insurance_id):
        database_connector.cursor.execute("DELETE FROM Insurance WHERE insuranceID=%s", (insurance_id,))
        database_connector.db.commit()