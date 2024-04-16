from utils.record_manager import RecordManager
from utils.query_builder import QueryBuilder
from utils.id_generator import IDGenerator
from utils.validator import Validator, TableAndColumn


class Doctor():
    # Class constructor
    def __init__(self):
        self.validator = Validator()  # Used to validate any user inputs

        # Used for validating the user's input for the create and update method
        self.column_options = {
            "doctor_id": { "max_length": 4, "exists_in_table": TableAndColumn(table_name="Doctor", column_name="DoctorID") },
            "firstname": { "max_length": 20 },
            "surname": { "max_length": 30 },
            "address": { "max_length": 50 },
            "email": { "max_length": 40 },
            "specialization": { },
            "experience": { "is_int": True, "can_be_blank": True }
        }

    # Gets user's inputs for creating the instance
    def get_create_inputs(self, database_connector):
        self.doctor_id = IDGenerator.generate_id(database_connector, 4, True, False, "Doctor", "doctorID")
        self.firstname = self.validator.get_input(database_connector, "What's the doctor's firstname? ", self.column_options["firstname"])
        self.surname = self.validator.get_input(database_connector, "What's the doctor's surname? ", self.column_options["surname"])
        self.address = self.validator.get_input(database_connector, "What's the doctor's address? ", self.column_options["address"])
        self.email = self.validator.get_input(database_connector, "What's the doctor's email? ", self.column_options["email"])

    # Creates the doctor
    def create_doctor(self, database_connector):
        self.get_create_inputs(database_connector)

        database_connector.cursor.execute("INSERT INTO Doctor(doctorID, firstname, surname, address, email) VALUES (%s, %s, %s, %s, %s);", (self.doctor_id, self.firstname, self.surname, self.address, self.email))
        
        # Displays the second argument if the table was changed, the third argument if not
        RecordManager.is_row_changed(database_connector, "Doctor created", "Something went wrong, nothing was created")
        
        # Saves the changes of the query
        database_connector.db.commit()

    # Displays all the doctor companies
    def list_doctors(self, database_connector):
        database_connector.cursor.execute("SELECT * FROM Doctor;")

        # Displays the result of the query
        RecordManager.print_records(database_connector.cursor.fetchall())

    # Displays a specific doctor company details
    def find_doctor(self, database_connector):

        # Gets the items the user wishes to change
        id = self.validator.get_input(database_connector, "Please enter the ID of the doctor you wish to search for (leave blank if unknown): ", { **self.column_options["doctor_id"], **{"can_be_blank": True} })
        firstname = self.validator.get_input(database_connector, "Please enter the firstname you wish to search for (leave blank if unknown): ", self.column_options["firstname"])
        surname = self.validator.get_input(database_connector, "Please enter the surname you wish to search for (leave blank if unknown): ", self.column_options["surname"])
        address = self.validator.get_input(database_connector, "Please enter the address you wish to search for (leave blank if unknown): ", self.column_options["address"])
        email = self.validator.get_input(database_connector, "Please enter the email you wish to search for (leave blank if unknown): ", self.column_options["email"])
        specialization = self.validator.get_input(database_connector, "Please enter the specialization you wish to search for (leave blank if unknown): ", self.column_options["specialization"])
        experience = self.validator.get_input(database_connector, "Please enter the experience you wish to search for (leave blank if unknown): ", { **self.column_options["experience"], **{"can_be_blank": True} })


        # Creates a find query
        query, variables = QueryBuilder.create_find_query("Doctor", ("doctorID", "firstname", "surname", "address", "email", "specialization", "experience"), (id, firstname, surname, address, email, specialization, experience))

        # Executes the query
        database_connector.cursor.execute(query, tuple(variables))        

        # Prints the output of the query
        RecordManager.print_records(database_connector.cursor.fetchall())
    
    # Updates a specific doctor
    def update_doctor(self, database_connector):
        # Gets the ID of the doctor the user wants to update
        doctor_id = self.validator.get_input(database_connector, "Enter the ID of the doctor you want to update: ", self.column_options["doctor_id"])
        
        # Gets the new data
        firstname = self.validator.get_input(database_connector, "Enter the new firstname (leave blank for no change): ", self.column_options["firstname"])
        surname = self.validator.get_input(database_connector, "Enter the new surname (leave blank for no change): ", self.column_options["surname"])
        address = self.validator.get_input(database_connector, "Enter the new address (leave blank for no change): ", self.column_options["address"])
        email = self.validator.get_input(database_connector, "Enter the new email (leave blank for no change): ", self.column_options["email"])
        specialization = self.validator.get_input(database_connector, "Enter the new specialization (leave blank for no change): ", self.column_options["specialization"])
        experience = self.validator.get_input(database_connector, "Enter the new experience (leave blank for no change): ", self.column_options["experience"])

        # Runs only if the object is an instance of the Doctor class
        query, variables = QueryBuilder.create_update_query("Doctor", ("doctorID",), (doctor_id,), ("firstname", "surname", "address", "email", "specialization", "experience"), (firstname, surname, address, email, specialization, experience))

        # Executes the query
        database_connector.cursor.execute(query, tuple(variables))

        # Displays the second argument if the table was changed, the third argument if not
        RecordManager.is_row_changed(database_connector, "Doctor updated", "No doctor found, nothing was updated")

        # Saves the changes to the table
        database_connector.db.commit()
   
    # Deletes a specific doctor
    def delete_doctor(self, database_connector):
        doctor_id = self.validator.get_input(database_connector, "Please enter the id of the doctor you wish to delete: ", self.column_options["doctor_id"])
        database_connector.cursor.execute("DELETE FROM Doctor WHERE doctorID=%s", (doctor_id,))
        
        # Displays the second argument if the table was changed, the third argument if not
        RecordManager.is_row_changed(database_connector, "Doctor deleted", "No doctor found, nothing was deleted")
        
        # Saves teh changes to the table
        database_connector.db.commit()

# Specialist class, subclass of Doctor
class Specialist(Doctor):
    def __init__(self):
        super().__init__()

        # Sets the specialization and experience column option
        self.column_options["specialization"] = { "max_length": 25 }
        self.column_options["experience"] = { "is_int": True }

    # Creates an specialist
    def create_specialist(self, database_connector):
        # Gets the inputs
        self.get_create_inputs(database_connector)  # Gets the inputs for a regular doctor (firstname, lastname, etc)
        self.specialization = self.validator.get_input(database_connector, "What's the doctor's specialization? ", self.column_options["specialization"])
        self.experience = self.validator.get_input(database_connector, "What's the doctor's experience (in years)? ", self.column_options["experience"])
        
        database_connector.cursor.execute("INSERT INTO Doctor(doctorID, firstname, surname, address, email, specialization, experience) VALUES (%s, %s, %s, %s, %s, %s, %s);", (self.doctor_id, self.firstname, self.surname, self.address, self.email, self.specialization, self.experience))
        
        # Displays the second argument if the table was changed, the third argument if not
        RecordManager.is_row_changed(database_connector, "Specialist created", "Something went wrong, nothing was created")
        
        # Saves the changes to the table
        database_connector.db.commit()
