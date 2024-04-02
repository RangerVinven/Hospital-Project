from utils.record_manager import RecordManager
from utils.query_builder import QueryBuilder
from utils.id_generator import IDGenerator

class Patient():
    def __init__(self, database_connector, firstname, surname, postcode, address, phone, email, insurance_ID):
        self.patient_id = IDGenerator.generate_id(database_connector, 8, True, True, "Patient", "patientID")
        self.firstname = firstname
        self.surname = surname
        self.postcode = postcode
        self.address = address
        self.phone = phone
        self.email = email
        self.insurance_id = insurance_ID

        self._create_patient(database_connector)

    def _create_patient(self, database_connector):
        database_connector.cursor.execute("INSERT INTO Patient(patientID, firstname, surname, postcode, address, phone, email, insuranceID) VALUES (%s, %s, %s, %s, %s, %s);", (self.patient_id, self.firstname, self.surname, self.address, self.email, self.insurance_id))
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
        id = input("Please enter the ID of the patient you wish to search for (leave blank if unknown): ")
        firstname = input("Please enter the firstname you wish to search for (leave blank if unknown): ")
        surname = input("Please enter the surname you wish to search for (leave blank if unknown): ")
        postcode = input("Please enter the postcode you wish to search for (leave blank if unknown): ")
        address = input("Please enter the address you wish to search for (leave blank if unknown): ")
        phone = input("Please enter the phone you wish to search for (leave blank if unknown): ")
        email = input("Please enter the email you wish to search for (leave blank if unknown): ")
        insurance_id = input("Please enter the insurance id you wish to search for (leave blank if unknown): ")
        insurance_type = input("Please enter the insurance type you wish to search for (leave blank if unknown): ")
        insurance_duration = input("Please enter the insurance duration you wish to search for (leave blank if unknown): ")
        
        query, variables = QueryBuilder.create_find_query("Patient", ("patientID", "firstname", "surname", "postcode", "address", "phone", "email", "insuranceID", "insuranceType", "insuranceDuration"), (id, firstname, surname, postcode, address, phone, email, insurance_id, insurance_type, insurance_duration))

        # Executes the query
        database_connector.cursor.execute(query, tuple(variables))        
        RecordManager.print_records(database_connector.cursor.fetchall())
    
    @staticmethod
    def update_patient(database_connector):

        # Gets the new item details
        patient_id = input("Enter the ID of the patient you want to update: ")
        firstname = input("Enter the new firstname (leave blank for no change): ")
        surname = input("Enter the new surname (leave blank for no change): ")
        postcode = input("Enter the new postcode (leave blank for no change): ")
        address = input("Enter the new address (leave blank for no change): ")
        phone = input("Enter the new phone (leave blank for no change): ")
        email = input("Enter the new email (leave blank for no change): ")
        insurance_id = input("Enter the new insurance id (leave blank for no change): ")
        insurance_type = input("Enter the new insurance type (leave blank for no change): ")
        insurance_duration = input("Enter the new insurance duration (leave blank for no change): ")

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
    def __init__(self, firstname, surname, postcode, address, phone, email, insurance_type, insurance_duration):
        super().__init__(firstname, surname, postcode, address, phone, email)
        
        self.insurance_type = insurance_type
        self.insurance_duration = insurance_duration

        self._create_patient()

    def _create_patient(self, database_connector):
        database_connector.cursor.execute("INSERT INTO Patient(patientID, firstname, surname, postcode, address, phone, email, insuranceID, insuranceType, insuranceDuration) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (self.patient_id, self.firstname, self.surname, self.address, self.email, self.insurance_id, self.insurance_type, self.insurance_duration))
        database_connector.db.commit()