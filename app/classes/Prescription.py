from utils.id_generator import IDGenerator
from utils.query_builder import QueryBuilder
from utils.record_manager import RecordManager

class Prescription():
    def __init__(self, database_connector, date_of_prescription, dosage, duration, comment, drug_id, doctor_id, patient_id):
        self.prescription_id = IDGenerator.generate_id(database_connector, 10, True, False, "Prescription", "prescriptionID")
        self.date_of_prescription = date_of_prescription
        self.dosage = dosage
        self.duration = duration
        self.comment = comment
        self.drug_id = drug_id
        self.doctor_id = doctor_id
        self.patient_id = patient_id

        self._create_prescription(database_connector)

    # Creates the prescription
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
        prescription_id = input("Please enter the ID of the prescription you wish to update: ")
        date_of_prescription = input("Please enter the date of prescription in YYYY-MM-DD format (or leave blank): ")
        dosage = input("Please enter the dosage (or leave blank): ")
        duration = input("Please enter the duration (or leave blank): ")
        comment = input("Please enter the comment (or leave blank): ")
        drug_id = input("Please enter the drug id (or leave blank): ")
        patient_id = input("Please enter the patient's id (or leave blank): ")
        doctor_id = input("Please enter the doctor's id (or leave blank): ")

        query, variables = QueryBuilder.create_find_query("Prescription", ("prescriptionID", "dateprescribed", "dosage", "duration", "comment", "drugID", "patientID", "doctorID"), (prescription_id, date_of_prescription, dosage, duration, comment, drug_id, patient_id, doctor_id))

        database_connector.cursor.execute(query, variables)
        RecordManager.print_records(database_connector.cursor.fetchall())

    # Updates the prescription
    @staticmethod
    def update_prescription(database_connector):
        prescription_id = input("Please enter the ID of the prescription you wish to update: ")
        date_of_prescription = input("Please enter the date of prescription in YYYY-MM-DD format: ")
        dosage = input("Please enter the dosage (or leave blank for no change): ")
        duration = input("Please enter the duration (or leave blank for no change): ")
        comment = input("Please enter the comment (or leave blank for no change): ")
        drug_id = input("Please enter the drug id (or leave blank for no change): ")
        patient_id = input("Please enter the patient's id: ")
        doctor_id = input("Please enter the doctor's id : ")

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

