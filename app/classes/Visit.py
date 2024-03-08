from ..utils.query_builder import QueryBuilder

class Visit():
    def __init__(self, database_connector, patient_id, doctor_id, date_of_visit, symptoms, diagnosis):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date_of_visit = date_of_visit
        self.symptoms = symptoms
        self.diagnosis = diagnosis

        self._create_visit(database_connector)

    def _create_visit(self, database_connector):
        database_connector.cursor.execute("INSERT INTO Visit (patientID, doctorID, dateofvisit, symptoms, diagnosis) VALUES (%s, %s, %s, %s, %s);", (self.patient_id, self.doctor_id, self.date_of_visit, self.symptoms, self.diagnosis))
        database_connector.db.commit()

    @staticmethod
    def list_visits(database_connector):
        database_connector.cursor.execute("SELECT * FROM Visit;")
        return database_connector.cursor.fetchall()

    @staticmethod
    def find_visit(database_connector):
        patient_id = input("Please enter the patient's id (or leave blank): ")
        doctor_id = input("Please enter the doctor's id (or leave blank): ")
        date_of_visit = input("Please enter the date of visit in YYYY-MM-DD format (or leave blank): ")
        symptoms = input("Please enter the symptoms (or leave blank): ")
        diagnosis = input("Please enter the diagnosis (or leave blank): ")

        query, variables = QueryBuilder.create_find_query("Visit", ("patientID", "doctorID", "dateofvisit", "symptoms", "diagnosis"), (patient_id, doctor_id, date_of_visit, symptoms, diagnosis))

        database_connector.cursor.execute(query, variables)
        return database_connector.cursor.fetchall()

    @staticmethod
    def update_visit(database_connector):
        patient_id = input("Please enter the patient's id (needed to identify the record): ")  # To find the specific record
        doctor_id = input("Please enter the doctor's id  (needed to identify the record): ")  # To find the specific record
        date_of_visit = input("Please enter the date of visit in YYYY-MM-DD format (needed to identify the record): ")  # To find the specific record
        symptoms = input("Please enter the symptoms (or leave blank for no change): ")  # To update the record
        diagnosis = input("Please enter the diagnosis (or leave blank for no change): ")  # To update the record

        query, variables = QueryBuilder.create_update_query("Visit", ["patientID", "doctorID", "dateofvisit"], [patient_id, doctor_id, date_of_visit], ("symptoms", "diagnosis"), (symptoms, diagnosis))
        database_connector.cursor.execute(query, tuple(variables))
        database_connector.db.commit()

    @staticmethod
    def delete_visit(datebase_connector, patient_id, doctor_id, date_of_visit):
        datebase_connector.cursor.execute("DELETE FROM Visit WHERE (patientID, doctorID, dateofvisit) = (%s, %s, %s);", (patient_id, doctor_id, date_of_visit))
        datebase_connector.db.commit()