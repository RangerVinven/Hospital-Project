from pytest import MonkeyPatch, fixture

from ..utils.database_connector import DatabaseConnector
from ..classes.Visit import Visit

database_connector = DatabaseConnector("testing")

@fixture(scope="module", autouse=True)
def setup_database():
    database_connector.cursor.execute("DELETE FROM Visit;")
    database_connector.db.commit()

@fixture(scope="module")
def teardown():
    database_connector.close_connection()

def test_create_visit():
    # Arrange
    patient_id = "123"
    doctor_id = "321"
    date_of_visit = "2027-07-07"
    symptoms = "Man's coughing"
    diagnosis = "The cold"

    # Act
    Visit(database_connector, patient_id, doctor_id, date_of_visit, symptoms, diagnosis)
    database_connector.cursor.execute("SELECT * FROM Visit WHERE patientID=%s AND doctorID=%s AND dateofvisit=%s AND symptoms=%s AND diagnosis=%s;", (patient_id, doctor_id, date_of_visit, symptoms, diagnosis))

    # Assert
    assert database_connector.cursor.fetchone() is not None, "The visit isn't saved to the database"


def test_find_visit(monkeypatch: MonkeyPatch):
    # Arrange
    patient_id = "111"
    doctor_id = "222"
    date_of_visit = "2027-07-07"
    symptoms = "Man's dying"
    diagnosis = "Death"

    database_connector.cursor.execute("INSERT INTO Visit(patientID, doctorID, dateofvisit, symptoms, diagnosis) VALUES (%s, %s, %s, %s, %s);", (patient_id, doctor_id, date_of_visit, symptoms, diagnosis))
    database_connector.db.commit()

    # Act
    inputs = [patient_id, doctor_id, date_of_visit, symptoms, diagnosis]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))  # Replaces the inputs inside update function with the above inputs array
    visit_found = Visit.find_visit(database_connector)

    # Assert
    assert len(visit_found) >= 1, "Couldn't search for a visit"


def test_delete_visit():
    # Arrange
    patient_id = "222"
    doctor_id = "333"
    date_of_visit = "2027-07-07"
    symptoms = "Man's really coughing"
    diagnosis = "Definitely the cold"
    Visit(database_connector, patient_id, doctor_id, date_of_visit, symptoms, diagnosis)

    # Act
    Visit.delete_visit(database_connector, patient_id, doctor_id, date_of_visit)

    # Assert
    database_connector.cursor.execute("SELECT * FROM Visit WHERE patientID=%s AND doctorID=%s AND dateofvisit=%s;", (patient_id, doctor_id, date_of_visit))
    assert database_connector.cursor.fetchone() is None, "Visit not deleted"


def test_find_visit(monkeypatch: MonkeyPatch):
    # Arrange
    patient_id = "111"
    doctor_id = "222"
    date_of_visit = "2027-07-07"
    symptoms = "Man's dying"
    diagnosis = "Death"

    database_connector.cursor.execute("INSERT INTO Visit(patientID, doctorID, dateofvisit, symptoms, diagnosis) VALUES (%s, %s, %s, %s, %s);", (patient_id, doctor_id, date_of_visit, symptoms, diagnosis))
    database_connector.db.commit()

    # Act
    inputs = [patient_id, doctor_id, date_of_visit, symptoms, diagnosis]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))  # Replaces the inputs inside update function with the above inputs array
    visit_found = Visit.find_visit(database_connector)

    # Assert
    assert len(visit_found) >= 1, "Couldn't search for a visit"


def test_update_visit(monkeypatch: MonkeyPatch):
    # Arrange (uses the same record from test_create_visit)
    patient_id = "123"
    doctor_id = "321"
    date_of_visit = "2027-07-07"
    symptoms = "Man's definitely gonna die"
    diagnosis = "He's dead"

    # Act
    inputs = [patient_id, doctor_id, date_of_visit, symptoms, diagnosis]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))  # Replaces the inputs inside update function with the above inputs array
    Visit.update_visit(database_connector)

    # Assert
    database_connector.cursor.execute("SELECT * FROM Visit WHERE (patientID, doctorID, dateofvisit) = (%s, %s, %s);", (patient_id, doctor_id, date_of_visit))
    search_result = database_connector.cursor.fetchall()
    
    if len(search_result) != 0:
        assert search_result[0]["symptoms"] == symptoms, "Symptoms wasn't updated"
        assert search_result[0]["diagnosis"] == diagnosis, "Diagnosis wasn't updated"
    else:
        assert False, "Updated result not found"