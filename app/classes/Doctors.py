from utils.record_manager import RecordManager
from utils.query_builder import QueryBuilder
from utils.id_generator import IDGenerator

class Doctor():
    def __init__(self, database_connector, firstname: str, surname: str, address: str, email: str):
        self.doctor_id = IDGenerator.generate_id(database_connector, 7, True, True, "Doctor", "doctorID")
        self.firstname = firstname
        self.surname = surname
        self.address = address
        self.email = email

        self._create_doctor(database_connector)

    def _create_doctor(self, database_connector):
        database_connector.cursor.execute("INSERT INTO Doctors(doctorID, firstname, surname, address, email) VALUES (%s, %s, %s, %s, %s);", (self.doctor_id, self.firstname, self.surname, self.address, self.email))
        database_connector.db.commit()

    # Returns all the doctor companies
    @staticmethod
    def list_doctors(database_connector):
        database_connector.cursor.execute("SELECT * FROM Doctor;")
        RecordManager.print_records(database_connector.cursor.fetchall())

    # Returns a specific doctor company details
    @staticmethod
    def find_doctor(database_connector):
        # Gets the items the user wishes to change
        id = input("Please enter the ID of the insurance you wish to search for (leave blank if unknown): ")
        firstname = input("Please enter the firstname you wish to search for (leave blank if unknown): ")
        surname = input("Please enter the surname you wish to search for (leave blank if unknown): ")
        address = input("Please enter the address you wish to search for (leave blank if unknown): ")
        email = input("Please enter the email you wish to search for (leave blank if unknown): ")

        query, variables = QueryBuilder.create_find_query("Doctor", ("doctorID", "firstname", "surname", "address", "email"), (id, firstname, surname, address, email))

        # Executes the query
        database_connector.cursor.execute(query, tuple(variables))        
        RecordManager.print_records(database_connector.cursor.fetchall())
    
    @staticmethod
    def update_doctor(database_connector):

        # Gets the new item details
        doctor_id = input("Enter the ID of the doctor you want to update: ")
        firstname = input("Enter the new firstname (leave blank for no change): ")
        surname = input("Enter the new surname (leave blank for no change): ")
        address = input("Enter the new address (leave blank for no change): ")
        email = input("Enter the new email (leave blank for no change): ")

        query, variables = QueryBuilder.create_update_query("Doctor", ("doctorID",), (doctor_id,), ("firstname", "surname", "address", "email"), (firstname, surname, address, email))

        # Executes the query
        database_connector.cursor.execute(query, tuple(variables))

        RecordManager.is_row_changed(database_connector, "Doctor updated", "No doctor found, nothing was updated")
        database_connector.db.commit()
   
    # Deletes a specific doctor
    def delete_doctor(database_connector):
        doctor_id = input("Please enter the id of the doctor you wish to delete: ")
        database_connector.cursor.execute("DELETE FROM Doctor WHERE doctorID=%s", (doctor_id,))
        
        RecordManager.is_row_changed(database_connector, "Doctor deleted", "No doctor found, nothing was deleted")
        database_connector.db.commit()

class Specialist(Doctor):
    def __init__(self, firstname: str, surname: str, address: str, email: str, specilization: str, experience: int):
        super().__init__(firstname, surname, address, email)
        self.specilization = specilization
        self.experience = experience