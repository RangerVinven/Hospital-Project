from utils.id_generator import IDGenerator
from utils.query_builder import QueryBuilder
from utils.record_manager import RecordManager
from utils.validator import Validator, ColumnOptionMapper, TableAndColumn

class Prescription():
    def __init__(self, database_connector):
        self.validator = Validator()
        self.column_options = { 
            "prescription_id": { "max_length": 10 },
            "date_of_prescription": { "is_date": True },
            "dosage": { "is_int": True },
            "duration": { "is_int": True },
            "comment": { "max_length": 200 },
            "drug_id": { "max_length": 7, "exists_in_table": TableAndColumn(table_name="Drug", column_name="DrugID") },
            "doctor_id": { "max_length": 4, "exists_in_table": TableAndColumn(table_name="Doctor", column_name="DoctorID") },
            "patient_id": { "max_length": 10, "exists_in_table": TableAndColumn(table_name="Patient", column_name="PatientID") },
        }
 
        self.prescription_id = IDGenerator.generate_id(database_connector, 10, True, False, "Prescription", "prescriptionID")
        self.date_of_prescription = self.validator.get_input(database_connector, "What's the data of prescription? ", self.column_options["date_of_prescription"])
        self.dosage = self.validator.get_input(database_connector, "What's the prescription's dosage? ", self.column_options["dosage"])
        self.duration = self.validator.get_input(database_connector, "What's the prescription's duration? ", self.column_options["duration"])
        self.comment = self.validator.get_input(database_connector, "What's the prescription's comment? ", self.column_options["comment"])
        self.drug_id = self.validator.get_input(database_connector, "What's the prescription's drug's id? ", self.column_options["drug_id"])
        self.doctor_id = self.validator.get_input(database_connector, "What's the prescription's doctor's id? ", self.column_options["doctor_id"])
        self.patient_id = self.validator.get_input(database_connector, "What's the prescription's patient's id? ", self.column_options["patient_id"])
        
        self._create_prescription(database_connector)

    # _Creates the prescription
    def _create_prescription(self, database_connector):
        database_connector.cursor.execute("INSERT INTO Prescription (prescriptionID, dateprescribed, dosage, duration, comment, drugID, doctorID, patientID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (self.prescription_id, self.date_of_prescription, self.dosage, self.duration, self.comment, self.drug_id, self.doctor_id, self.patient_id))
        database_connector.db.commit()

    @staticmethod
    def list_prescriptions(database_connector):
        database_connector.cursor.execute("SELECT * FROM Prescription;")
        RecordManager.print_records(database_connector.cursor.fetchall())

    @staticmethod
    def find_prescription(database_connector):
        # Gets the search parameters
        prescription_id = self.validator.get_input(database_connector, "Please enter the ID of the prescription you wish to update: ", self.column_options["prescription_id"])
        date_of_prescription = self.validator.get_input(database_connector, "Please enter the date of prescription in YYYY-MM-DD format (or leave blank): ", self.column_options["date_of_prescription"])
        dosage = self.validator.get_input(database_connector, "Please enter the dosage (or leave blank): ", self.column_options["dosage"])
        duration = self.validator.get_input(database_connector, "Please enter the duration (or leave blank): ", self.column_options["duration"])
        comment = self.validator.get_input(database_connector, "Please enter the comment (or leave blank): ", self.column_options["comment"])
        drug_id = self.validator.get_input(database_connector, "Please enter the drug id (or leave blank): ", self.column_options["drug_id"])
        patient_id = self.validator.get_input(database_connector, "Please enter the patient's id (or leave blank): ", self.column_options["patient_id"])
        doctor_id = self.validator.get_input(database_connector, "Please enter the doctor's id (or leave blank): ", self.column_options["doctor_id"])

        query, variables = QueryBuilder.create_find_query("Prescription", ("prescriptionID", "dateprescribed", "dosage", "duration", "comment", "drugID", "patientID", "doctorID"), (prescription_id, date_of_prescription, dosage, duration, comment, drug_id, patient_id, doctor_id))

        database_connector.cursor.execute(query, variables)
        RecordManager.print_records(database_connector.cursor.fetchall())

    # Updates the prescription
    @staticmethod
    def update_prescription(database_connector):
        prescription_id = self.validator.get_input(database_connector, "Please enter the ID of the prescription you wish to update: ", self.column_options["prescription_id"])
        date_of_prescription = self.validator.get_input(database_connector, "Please enter the date of prescription in YYYY-MM-DD format: ", self.column_options["date_of_prescription"])
        dosage = self.validator.get_input(database_connector, "Please enter the dosage (or leave blank for no change): ", self.column_options["dosage"])
        duration = self.validator.get_input(database_connector, "Please enter the duration (or leave blank for no change): ", self.column_options["duration"])
        comment = self.validator.get_input(database_connector, "Please enter the comment (or leave blank for no change): ", self.column_options["comment"])
        drug_id = self.validator.get_input(database_connector, "Please enter the drug id (or leave blank for no change): ", self.column_options["drug_id"])
        patient_id = self.validator.get_input(database_connector, "Please enter the patient's id: ", self.column_options["patient_id"])
        doctor_id = self.validator.get_input(database_connector, "Please enter the doctor's id : ", self.column_options["doctor_id"])

        query, variables = QueryBuilder.create_update_query("Prescription", ["prescriptionID"], [prescription_id], ("dateprescribed", "dosage", "duration", "comment", "drugID", "patientID", "doctorID"), (date_of_prescription, dosage, duration, comment, drug_id, patient_id, doctor_id))
        
        database_connector.cursor.execute(query, tuple(variables))
        RecordManager.is_row_changed(database_connector, "Prescription updated", "Prescription not found, no prescription updated")

        database_connector.db.commit()

    @staticmethod
    def delete_prescription(database_connector):
        prescription_id = input("Please enter the ID of the prescription you wish to delete: ")

        database_connector.cursor.execute("DELETE FROM Prescription WHERE prescriptionID=%s;", (prescription_id,))
        RecordManager.is_row_changed(database_connector, "Prescription deleted", "Prescription not found, no prescription deleted")

        database_connector.db.commit()

