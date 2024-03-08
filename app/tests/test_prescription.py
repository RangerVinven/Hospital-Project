from pytest import MonkeyPatch, fixture
from ..utils.database_connector import DatabaseConnector
from ..classes.Prescription import Prescription

database_connector = DatabaseConnector("testing")

@fixture(scope="module", autouse=True)
def setup_database():
    database_connector.cursor.execute("DELETE FROM Prescription;")
    database_connector.db.commit()

@fixture(scope="module")
def teardown():
    database_connector.close_connection()

def test_create_prescription():
    # Arrange
    date_of_prescription = "2027-07-07"
    dosage = 50
    duration = 7
    comment = "Take with milk"
    drug_id = "ABC123"
    doctor_id = "321"
    patient_id = "123"

    # Act
    Prescription(database_connector, date_of_prescription, dosage, duration, comment, drug_id, doctor_id, patient_id)
    database_connector.cursor.execute("SELECT * FROM Prescription WHERE patientID=%s AND doctorID=%s AND dateprescribed=%s AND dosage=%s AND duration=%s AND comment=%s AND drugID=%s;", (patient_id, doctor_id, date_of_prescription, dosage, duration, comment, drug_id))

    # Assert
    assert database_connector.cursor.fetchone() is not None, "The prescription isn't saved to the database"


def test_update_prescription_new_comment(monkeypatch: MonkeyPatch):
    # Arrange
    database_connector.cursor.execute("INSERT INTO Prescription(prescriptionID, dateprescribed, dosage, duration, comment, drugID, doctorID, patientID) VALUES (1000, '2027-07-07', 50, 7, 'old comment', 'ABC123', '321', '123');")

    # Act
    updated_value = "new comment"
    inputs = ["1000", "", "", "", updated_value, "", "", ""]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))  # Replaces the inputs inside update function with the above inputs array
    
    Prescription.update_prescription(database_connector)
    
    # Assert
    database_connector.cursor.execute("SELECT * FROM Prescription WHERE prescriptionID=1000 AND comment=%s;", (updated_value,))
    assert database_connector.cursor.fetchone() is not None, "Prescription not updated"


def test_delete_prescription():
    # Arrange
    database_connector.cursor.execute("INSERT INTO Prescription(prescriptionID, dateprescribed, dosage, duration, comment, drugID, doctorID, patientID) VALUES (2000, '2027-07-07', 50, 7, 'Take with food', 'ABC123', '321', '123');")    
    database_connector.db.commit()

    # Act
    Prescription.delete_prescription(database_connector, "123", "321", "2027-07-07")

    # Assert
    database_connector.cursor.execute("SELECT * FROM Prescription WHERE prescriptionID=2000 AND comment='Take with food';")
    assert database_connector.cursor.fetchone() is None, "Prescription not deleted from the database"


def test_find_prescription(monkeypatch: MonkeyPatch):
    # Arrange
    database_connector.cursor.execute("INSERT INTO Prescription(prescriptionID, dateprescribed, dosage, duration, comment, drugID, doctorID, patientID) VALUES (3000, '2027-07-07', 50, 7, 'Take with alcohol', 'ABC123', '321', '123');")    
    database_connector.db.commit()

    # Act
    inputs = ["2027-07-07", "50", "7", "", "", "", ""]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))  # Replaces the inputs inside update function with the above inputs array
    prescriptions_found = Prescription.find_prescription(database_connector)

    # Assert
    assert len(prescriptions_found) >= 1, "Couldn't search for a prescription"
