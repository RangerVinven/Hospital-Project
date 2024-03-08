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
    def find_visit(database_connector):
        patient_id = input("Please enter the patient's id (leave blank if unknown): ")
        doctor_id = input("Please enter the doctor's id (leave blank if unknown): ")
        date_of_visit = input("Please enter the date of visit in YYYY-MM-DD format (leave blank if unknown): ")
        symptoms = input("Please enter the symptoms (leave blank if unknown): ")
        diagnosis = input("Please enter the diagnosis (leave blank if unknown): ")

        query, variables = QueryBuilder.create_find_query("Visit", ("patientID", "doctorID", "dateofvisit", "symptoms", "diagnosis"), (patient_id, doctor_id, date_of_visit, symptoms, diagnosis))

        database_connector.cursor.execute(query, variables)
        return database_connector.cursor.fetchall()

    