from utils.query_builder import QueryBuilder
from utils.record_manager import RecordManager
from utils.validator import Validator, TableAndColumn 

class Visit():
    def __init__(self):
        self.validator = Validator()  # Used to validate any user inputs

        # Used for validating the user's input for the create and update method
        self.column_options = {
            "patient_id": { "max_length": 10, "exists_in_table": TableAndColumn(table_name="Patient", column_name="patientID") },
            "doctor_id": { "max_length": 4, "exists_in_table": TableAndColumn(table_name="Doctor", column_name="doctorID")},
            "date_of_visit": { "is_date": True },
            "symptoms": { "max_length": 200 },
            "diagnosis": { "max_length": 50 }
        }

    # Creates the visit
    def create_visit(self, database_connector):
        # Gets the inputs
        self.patient_id = self.validator.get_input(database_connector, "What's the patient's id? ", self.column_options["patient_id"])
        self.doctor_id = self.validator.get_input(database_connector, "What's the doctor's id? ", self.column_options["doctor_id"])
        self.date_of_visit = self.validator.get_input(database_connector, "What's the visit date (YYYY-MM-DD)? ", self.column_options["date_of_visit"])
        self.symptoms = self.validator.get_input(database_connector, "What's the patient's symptoms? ", self.column_options["symptoms"])
        self.diagnosis = self.validator.get_input(database_connector, "What's the patient's diagnosis? ", self.column_options["diagnosis"])

        # Executes the query
        database_connector.cursor.execute("INSERT INTO Visit (patientID, doctorID, dateofvisit, symptoms, diagnosis) VALUES (%s, %s, %s, %s, %s);", (self.patient_id, self.doctor_id, self.date_of_visit, self.symptoms, self.diagnosis))
        database_connector.db.commit()

    # Lists the visits
    def list_visits(self, database_connector):
        database_connector.cursor.execute("SELECT * FROM Visit;")
        
        # Displays the results of the query
        RecordManager.print_records(database_connector.cursor.fetchall())

    # Finds a specific visit
    def find_visit(self, database_connector):
        # Gets the inputs
        patient_id = self.validator.get_input(database_connector, "Please enter the patient's id (or leave blank): ", { **self.column_options["patient_id"], **{"can_be_blank": True} })
        doctor_id = self.validator.get_input(database_connector, "Please enter the doctor's id (or leave blank): ", { **self.column_options["doctor_id"], **{"can_be_blank": True} })
        date_of_visit = self.validator.get_input(database_connector, "Please enter the date of visit in YYYY-MM-DD format (or leave blank): ", { **self.column_options["date_of_visit"], **{"can_be_blank": True} })
        symptoms = self.validator.get_input(database_connector, "Please enter the symptoms (or leave blank): ", self.column_options["symptoms"])
        diagnosis = self.validator.get_input(database_connector, "Please enter the diagnosis (or leave blank): ", self.column_options["diagnosis"])

        # Creates and executes the find query
        query, variables = QueryBuilder.create_find_query("Visit", ("patientID", "doctorID", "dateofvisit", "symptoms", "diagnosis"), (patient_id, doctor_id, date_of_visit, symptoms, diagnosis))
        database_connector.cursor.execute(query, variables)
        
        # Displays the results of the query
        RecordManager.print_records(database_connector.cursor.fetchall())

    # Updates a visit
    def update_visit(self, database_connector):
        # Gets the details necessary to find the visit the user wants to update
        patient_id = self.validator.get_input(database_connector, "Please enter the patient's id (needed to identify the record): ", self.column_options["patient_id"])  
        doctor_id = self.validator.get_input(database_connector, "Please enter the doctor's id  (needed to identify the record): ", self.column_options["doctor_id"])  
        date_of_visit = self.validator.get_input(database_connector, "Please enter the date of visit in YYYY-MM-DD format (needed to identify the record): ", self.column_options["date_of_visit"])  

        # Gets the new details for the visit
        new_patient_id = self.validator.get_input(database_connector, "Please enter the new patient's id (or leave blank for no change): ", { **self.column_options["patient_id"], **{"can_be_blank": True} })  
        new_doctor_id = self.validator.get_input(database_connector, "Please enter the new doctor's id (or leave blank for no change): ", { **self.column_options["doctor_id"], **{"can_be_blank": True} })  
        new_date_of_visit = self.validator.get_input(database_connector, "Please enter the new date of visit in YYYY-MM-DD format (or leave blank for no change): ", { **self.column_options["date_of_visit"], **{"can_be_blank": True} })  
        symptoms = self.validator.get_input(database_connector, "Please enter the new symptoms (or leave blank for no change): ", self.column_options["symptoms"])  
        diagnosis = self.validator.get_input(database_connector, "Please enter the new diagnosis (or leave blank for no change): ", self.column_options["diagnosis"])  

        # Creates and executes the update query
        query, variables = QueryBuilder.create_update_query("Visit", ["patientID", "doctorID", "dateofvisit"], [patient_id, doctor_id, date_of_visit], ("patientID", "doctorID", "dateofvisit", "symptoms", "diagnosis"), (new_patient_id, new_doctor_id, new_date_of_visit, symptoms, diagnosis))
        database_connector.cursor.execute(query, tuple(variables))

        # Displays the second argument if the table was changed, the third argument if not
        RecordManager.is_row_changed(database_connector, "Visit updated", "Visit not found, no visit updated")
        database_connector.db.commit()

    # Deletes the visit
    def delete_visit(self, database_connector):
        # Gets the inputs to find the visit
        patient_id = self.validator.get_input(database_connector, "Enter the patient's ID: ", self.column_options["patient_id"])
        doctor_id = self.validator.get_input(database_connector, "Enter the doctor's ID: ", self.column_options["doctor_id"])
        date_of_visit = self.validator.get_input(database_connector, "Enter the Date of Visit (YYYY-MM-DD): ", self.column_options["date_of_visit"])

        database_connector.cursor.execute("DELETE FROM Visit WHERE (patientID, doctorID, dateofvisit) = (%s, %s, %s);", (patient_id, doctor_id, date_of_visit))

        # Displays the second argument if the table was changed, the third argument if not
        RecordManager.is_row_changed(database_connector, "Visit deleted", "Visit not found, no visit deleted")
        database_connector.db.commit()