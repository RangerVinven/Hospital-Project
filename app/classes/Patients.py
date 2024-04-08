from utils.record_manager import RecordManager
from utils.query_builder import QueryBuilder
from utils.id_generator import IDGenerator
from utils.validator import Validator, ColumnOptionMapper, TableAndColumn

class Patient():
    def __init__(self, database_connector):
        self.validator = Validator()
        self.column_options = {
            "patient_id": { "max_length":  8 },
            "firstname": { "max_length": 20 },
            "surname": { "max_length": 30 },
            "postcode": { "max_length": 8 },
            "address": { "max_length": 50 },
            "phone": { "max_length": 12 },
            "email": { "max_length": 40 },
        }
    
        self.patient_id = IDGenerator.generate_id(database_connector, 8, True, True, "Patient", "patientID")
        self.firstname = self.validator.get_input(database_connector, "What is the patient's firstname? ", self.column_options["firstname"])
        self.surname = self.validator.get_input(database_connector, "What is the patient's surname? ", self.column_options["surname"])
        self.postcode = self.validator.get_input(database_connector, "What is the patient's postcode? ", self.column_options["postcode"])
        self.address = self.validator.get_input(database_connector, "What is the patient's address? ", self.column_options["address"])
        self.phone = self.validator.get_input(database_connector, "What is the patient's phone? ", self.column_options["phone"])
        self.email = self.validator.get_input(database_connector, "What is the patient's email? ", self.column_options["email"])

    def create_patient(self, database_connector):
        database_connector.cursor.execute("INSERT INTO Patient(patientID, firstname, surname, postcode, address, phone, email) VALUES (%s, %s, %s, %s, %s, %s, %s);", (self.patient_id, self.firstname, self.surname, self.postcode, self.address, self.phone, self.email))
        
        RecordManager.is_row_changed(database_connector, "Patient created", "Something went wrong, no patient created")
        database_connector.db.commit()

    # Returns all the patient companies
    @staticmethod
    def list_patients(database_connector):
        database_connector.cursor.execute("SELECT * FROM Patient;")
        RecordManager.print_records(database_connector.cursor.fetchall())

    # Returns a specific patient company details
    @staticmethod
    def find_patient(database_connector):
        # Gets the items the user wishes to change
        id = self.validator.get_input(database_connector, "Please enter the ID of the patient you wish to search for (leave blank if unknown): ", self.column_options["id"])
        firstname = self.validator.get_input(database_connector, "Please enter the firstname you wish to search for (leave blank if unknown): ", self.column_options["firstname"])
        surname = self.validator.get_input(database_connector, "Please enter the surname you wish to search for (leave blank if unknown): ", self.column_options["surname"])
        postcode = self.validator.get_input(database_connector, "Please enter the postcode you wish to search for (leave blank if unknown): ", self.column_options["postcode"])
        address = self.validator.get_input(database_connector, "Please enter the address you wish to search for (leave blank if unknown): ", self.column_options["address"])
        phone = self.validator.get_input(database_connector, "Please enter the phone you wish to search for (leave blank if unknown): ", self.column_options["phone"])
        email = self.validator.get_input(database_connector, "Please enter the email you wish to search for (leave blank if unknown): ", self.column_options["email"])
        insurance_id = self.validator.get_input(database_connector, "Please enter the insurance id you wish to search for (leave blank if unknown): ", self.column_options["insurance_id"])
        insurance_type = self.validator.get_input(database_connector, "Please enter the insurance type you wish to search for (leave blank if unknown): ", self.column_options["insurance_type"])
        insurance_duration = self.validator.get_input(database_connector, "Please enter the insurance duration you wish to search for (leave blank if unknown): ", self.column_options["insurance_duration"])
        
        query, variables = QueryBuilder.create_find_query("Patient", ("patientID", "firstname", "surname", "postcode", "address", "phone", "email", "insuranceID", "insuranceType", "insuranceDuration"), (id, firstname, surname, postcode, address, phone, email, insurance_id, insurance_type, insurance_duration))

        # Executes the query
        database_connector.cursor.execute(query, tuple(variables))        
        RecordManager.print_records(database_connector.cursor.fetchall())
    
    @staticmethod
    def update_patient(database_connector):

        # Gets the new item details
        patient_id = self.validator.get_input(database_connector, "Enter the ID of the patient you want to update: ", self.column_options["patient_id"])
        firstname = self.validator.get_input(database_connector, "Enter the new firstname (leave blank for no change): ", self.column_options["firstname"])
        surname = self.validator.get_input(database_connector, "Enter the new surname (leave blank for no change): ", self.column_options["surname"])
        postcode = self.validator.get_input(database_connector, "Enter the new postcode (leave blank for no change): ", self.column_options["postcode"])
        address = self.validator.get_input(database_connector, "Enter the new address (leave blank for no change): ", self.column_options["address"])
        phone = self.validator.get_input(database_connector, "Enter the new phone (leave blank for no change): ", self.column_options["phone"])
        email = self.validator.get_input(database_connector, "Enter the new email (leave blank for no change): ", self.column_options["email"])
        insurance_id = self.validator.get_input(database_connector, "Enter the new insurance id (leave blank for no change): ", self.column_options["insurance_id"])
        insurance_type = self.validator.get_input(database_connector, "Enter the new insurance type (leave blank for no change): ", self.column_options["insurance_type"])
        insurance_duration = self.validator.get_input(database_connector, "Enter the new insurance duration (leave blank for no change): ", self.column_options["insurance_duration"])

        query, variables = QueryBuilder.create_update_query("Patient", ("patientID",), (patient_id,), ("firstname", "surname", "postcode", "address", "phone", "email", "insuranceID", "insuranceType", "insuranceDuration"), (firstname, surname, postcode, address, phone, email, insurance_id, insurance_type, insurance_duration))

        # Executes the query
        database_connector.cursor.execute(query, tuple(variables))

        RecordManager.is_row_changed(database_connector, "Patient updated", "No patient found, nothing was updated")
        database_connector.db.commit()
   
    # Deletes a specific patient
    def delete_patient(database_connector):
        patient_id = input("Please enter the id of the patient you wish to delete: ")
        database_connector.cursor.execute("DELETE FROM Patient WHERE patientID=%s", (patient_id,))
        
        RecordManager.is_row_changed(database_connector, "Patient deleted", "No patient found, nothing was deleted")
        database_connector.db.commit()


class InsuredPatient(Patient):
    def __init__(self, database_connector):
        super().__init__(database_connector)
        
        self.insurance_id = self.validator.get_input(database_connector, "What is the patient's insurance's ID? ", { "max_length": 10, "exists_in_table": TableAndColumn(table_name="Insurance", column_name="insuranceID") })
        self.insurance_type = self.validator.get_input(database_connector, "What is the patient's insurance type? ", { "max_length": 20 })
        self.insurance_duration = self.validator.get_input(database_connector, "What is the patient's insurance duration in years? ", { "is_int": True })

    def create_insured_patient(self, database_connector):
        database_connector.cursor.execute("INSERT INTO Patient(patientID, firstname, surname, postcode, address, phone, email, insuranceID, insuranceType, insuranceDuration) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (self.patient_id, self.firstname, self.surname, self.postcode, self.address, self.phone, self.email, self.insurance_id, self.insurance_type, self.insurance_duration))

        RecordManager.is_row_changed(database_connector, "Patient created", "Something went wrong, no patient created")
        database_connector.db.commit()