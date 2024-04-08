from utils.query_builder import QueryBuilder
from utils.record_manager import RecordManager
from utils.validator import Validator, TableAndColumn, ColumnOptionMapper

class Visit():
    def __init__(self, database_connector):
        self.validator = Validator()
        self.column_options = {
            "patient_id": { "max_length": 10, "exists_in_table": TableAndColumn(table_name="Patient", column_name="patientID") },
            "doctor_id": { "max_length": 4, "exists_in_table": TableAndColumn(table_name="Doctor", column_name="doctorID")},
            "date_of_visit": { "is_date": True },
            "symptoms": { "max_length": 200 },
            "diagnosis": { "max_length": 50 }
        }

        self.patient_id = self.validator.get_input(database_connector, "What's the patient's id? ", self.column_options["patient_id"])
        self.doctor_id = self.validator.get_input(database_connector, "What's the doctor's id? ", self.column_options["doctor_id"])
        self.date_of_visit = self.validator.get_input(database_connector, "What's the visit date (YYYY-MM-DD)? ", self.column_options["date_of_visit"])
        self.symptoms = self.validator.get_input(database_connector, "What's the patient's symptoms? ", self.column_options["symptoms"])
        self.diagnosis = self.validator.get_input(database_connector, "What's the patient's diagnosis? ", self.column_options["diagnosis"])
        
        self._create_visit(database_connector)
    
    def _create_visit(self, database_connector):
        database_connector.cursor.execute("INSERT INTO Visit (patientID, doctorID, dateofvisit, symptoms, diagnosis) VALUES (%s, %s, %s, %s, %s);", (self.patient_id, self.doctor_id, self.date_of_visit, self.symptoms, self.diagnosis))
        database_connector.db.commit()

    @staticmethod
    def list_visits(database_connector):
        database_connector.cursor.execute("SELECT * FROM Visit;")
        RecordManager.print_records(database_connector.cursor.fetchall())

    @staticmethod
    def find_visit(self, database_connector):
        patient_id = self.validator.get_input(database_connector, "Please enter the patient's id (or leave blank): ", self.column_options["patient_id"])
        doctor_id = self.validator.get_input(database_connector, "Please enter the doctor's id (or leave blank): ", self.column_options[""])
        date_of_visit = self.validator.get_input(database_connector, "Please enter the date of visit in YYYY-MM-DD format (or leave blank): ", self.column_options["date_of_visit"])
        symptoms = self.validator.get_input(database_connector, "Please enter the symptoms (or leave blank): ", self.column_options["symptoms"])
        diagnosis = self.validator.get_input(database_connector, "Please enter the diagnosis (or leave blank): ", self.column_options["diagnosis"])

        query, variables = QueryBuilder.create_find_query("Visit", ("patientID", "doctorID", "dateofvisit", "symptoms", "diagnosis"), (patient_id, doctor_id, date_of_visit, symptoms, diagnosis))

        database_connector.cursor.execute(query, variables)
        RecordManager.print_records(database_connector.cursor.fetchall())

    @staticmethod
    def update_visit(self, database_connector):
        patient_id = self.validator.get_input(database_connector, "Please enter the patient's id (needed to identify the record): ", self.column_options["patient_id"])  
        doctor_id = self.validator.get_input(database_connector, "Please enter the doctor's id  (needed to identify the record): ", self.column_options["doctor_id"])  
        date_of_visit = self.validator.get_input(database_connector, "Please enter the date of visit in YYYY-MM-DD format (needed to identify the record): ", self.column_options["date_of_visit"])  

        new_patient_id = self.validator.get_input(database_connector, "Please enter the new patient's id (or leave blank for no change): ", self.column_options["new_patient_id"])  
        new_doctor_id = self.validator.get_input(database_connector, "Please enter the new doctor's id (or leave blank for no change): ", self.column_options["new_doctor_id"])  
        new_date_of_visit = self.validator.get_input(database_connector, "Please enter the new date of visit in YYYY-MM-DD format (or leave blank for no change): ", self.column_options["new_date_of_visit"])  
        symptoms = self.validator.get_input(database_connector, "Please enter the new symptoms (or leave blank for no change): ", self.column_options["symptoms"])  
        diagnosis = self.validator.get_input(database_connector, "Please enter the new diagnosis (or leave blank for no change): ", self.column_options["diagnosis"])  

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