from utils.id_generator import IDGenerator

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
