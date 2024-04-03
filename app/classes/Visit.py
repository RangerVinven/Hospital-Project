from utils.query_builder import QueryBuilder
from utils.record_manager import RecordManager
from utils.validator import Validator

class Visit():
    def __init__(self, database_connector):
        self.validator = Validator()
    
        self.patient_id = self.validator.get_input(database_connector, "What's the patient's id? ", { "max_length": 20 })
        self.doctor_id = self.validator.get_input(database_connector, "What's the doctor's id? ", { "max_length": 20 })
        self.date_of_visit = self.validator.get_input(database_connector, "What's the visit date (YYYY-MM-DD)? ", { "max_length": 20 })
        self.symptoms = self.validator.get_input(database_connector, "What's the patient's symptoms? ", { "max_length": 20 })
        self.diagnosis = self.validator.get_input(database_connector, "What's the patient's diagnosis? ", { "max_length": 20 })
        
        self._create_visit(database_connector)
    
    def _create_visit(self, database_connector):
        database_connector.cursor.execute("INSERT INTO Visit (patientID, doctorID, dateofvisit, symptoms, diagnosis) VALUES (%s, %s, %s, %s, %s);", (self.patient_id, self.doctor_id, self.date_of_visit, self.symptoms, self.diagnosis))
        database_connector.db.commit()

    @staticmethod
    def list_visits(database_connector):
        database_connector.cursor.execute("SELECT * FROM Visit;")
        RecordManager.print_records(database_connector.cursor.fetchall())

    @staticmethod
    def find_visit(database_connector):
        patient_id = input("Please enter the patient's id (or leave blank): ")
        doctor_id = input("Please enter the doctor's id (or leave blank): ")
        date_of_visit = input("Please enter the date of visit in YYYY-MM-DD format (or leave blank): ")
        symptoms = input("Please enter the symptoms (or leave blank): ")
        diagnosis = input("Please enter the diagnosis (or leave blank): ")

        query, variables = QueryBuilder.create_find_query("Visit", ("patientID", "doctorID", "dateofvisit", "symptoms", "diagnosis"), (patient_id, doctor_id, date_of_visit, symptoms, diagnosis))

        database_connector.cursor.execute(query, variables)
        RecordManager.print_records(database_connector.cursor.fetchall())

    @staticmethod
    def update_visit(database_connector):
        patient_id = input("Please enter the patient's id (needed to identify the record): ")  # To find the specific record
        doctor_id = input("Please enter the doctor's id  (needed to identify the record): ")  # To find the specific record
        date_of_visit = input("Please enter the date of visit in YYYY-MM-DD format (needed to identify the record): ")  # To find the specific record

        new_patient_id = input("Please enter the new patient's id (or leave blank for no change): ")  # To find the specific record
        new_doctor_id = input("Please enter the new doctor's id (or leave blank for no change): ")  # To find the specific record
        new_date_of_visit = input("Please enter the new date of visit in YYYY-MM-DD format (or leave blank for no change): ")  # To find the specific record
        symptoms = input("Please enter the new symptoms (or leave blank for no change): ")  # To update the record
        diagnosis = input("Please enter the new diagnosis (or leave blank for no change): ")  # To update the record

        query, variables = QueryBuilder.create_update_query("Visit", ["patientID", "doctorID", "dateofvisit"], [patient_id, doctor_id, date_of_visit], ("patientID", "doctorID", "dateofvisit", "symptoms", "diagnosis"), (new_patient_id, new_doctor_id, new_date_of_visit, symptoms, diagnosis))
        database_connector.cursor.execute(query, tuple(variables))

        RecordManager.is_row_changed(database_connector, "Visit updated", "Visit not found, no visit updated")
        database_connector.db.commit()

    @staticmethod
    def delete_visit(datebase_connector):
        patient_id = input("Enter the patient's ID: ")
        doctor_id = input("Enter the doctor's ID: ")
        date_of_visit = input("Enter the Date of Visit (YYYY-MM-DD): ")

        datebase_connector.cursor.execute("DELETE FROM Visit WHERE (patientID, doctorID, dateofvisit) = (%s, %s, %s);", (patient_id, doctor_id, date_of_visit))

        RecordManager.is_row_changed(datebase_connector, "Visit deleted", "Visit not found, no visit deleted")
        datebase_connector.db.commit()