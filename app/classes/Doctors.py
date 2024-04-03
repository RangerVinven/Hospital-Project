from utils.record_manager import RecordManager
from utils.query_builder import QueryBuilder
from utils.id_generator import IDGenerator
from utils.validator import Validator


class Doctor():
    def __init__(self, database_connector):
        self.validator = Validator()

        self.doctor_id = IDGenerator.generate_id(database_connector, 4, True, False, "Doctor", "doctorID")
        self.firstname = self.validator.get_input(database_connector, "What's the doctor's firstname? ", { "max_length": 20 })
        self.surname = self.validator.get_input(database_connector, "What's the doctor's surname? ", { "max_length": 30 })
        self.address = self.validator.get_input(database_connector, "What's the doctor's address? ", { "max_length": 50 })
        self.email = self.validator.get_input(database_connector, "What's the doctor's email? ", { "max_length": 40 })

    def create_doctor(self, database_connector):
        database_connector.cursor.execute("INSERT INTO Doctor(doctorID, firstname, surname, address, email) VALUES (%s, %s, %s, %s, %s);", (self.doctor_id, self.firstname, self.surname, self.address, self.email))
        
        RecordManager.is_row_changed(database_connector, "Doctor created", "Something went wrong, nothing was created")
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
        specialization = input("Please enter the specialization you wish to search for (leave blank if unknown): ")
        experience = input("Please enter the experience you wish to search for (leave blank if unknown): ")

        query, variables = QueryBuilder.create_find_query("Doctor", ("doctorID", "firstname", "surname", "address", "email", "specialization", "experience"), (id, firstname, surname, address, email, specialization, experience))

        # Executes the query
        database_connector.cursor.execute(query, tuple(variables))        
        RecordManager.print_records(database_connector.cursor.fetchall())
    
    @staticmethod
    def update_doctor(database_connector):

        # Gets the new data
        doctor_id = input("Enter the ID of the doctor you want to update: ")
        firstname = input("Enter the new firstname (leave blank for no change): ")
        surname = input("Enter the new surname (leave blank for no change): ")
        address = input("Enter the new address (leave blank for no change): ")
        email = input("Enter the new email (leave blank for no change): ")
        specialization = input("Enter the new specialization (leave blank for no change): ")
        experience = input("Enter the new experience (leave blank for no change): ")

        # Runs only if the object is an instance of the Doctor class
        query, variables = QueryBuilder.create_update_query("Doctor", ("doctorID",), (doctor_id,), ("firstname", "surname", "address", "email", "specialization", "experience"), (firstname, surname, address, email, specialization, experience))

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
    def __init__(self, database_connector):
        super().__init__(database_connector)
        self.specialization = self.validator.get_input(database_connector, "What's the doctor's specialization? ", { "max_length": 25 })
        self.experience = self.validator.get_input(database_connector, "What's the doctor's experience (in years)? ", { "is_int": True })

    def create_specialist(self, database_connector):
        database_connector.cursor.execute("INSERT INTO Doctor(doctorID, firstname, surname, address, email, specialization, experience) VALUES (%s, %s, %s, %s, %s, %s, %s);", (self.doctor_id, self.firstname, self.surname, self.address, self.email, self.specialization, self.experience))
        
        RecordManager.is_row_changed(database_connector, "Specialist created", "Something went wrong, nothing was created")
        database_connector.db.commit()