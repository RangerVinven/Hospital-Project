# Had issues running the tests. If there are issues, go to app/ and run the command:
# python3 -m pytest app/tests/test_insurance.py

from pytest import MonkeyPatch, fixture

from ..utils.database_connector import DatabaseConnector
from ..classes.Insurance import Insurance

database_connector = DatabaseConnector("testing")

@fixture(scope="module", autouse=True)
def setup_database():
    database_connector.cursor.execute("DELETE FROM Insurance;")
    database_connector.db.commit()

@fixture(scope="module")
def teardown():
    database_connector.close_connection()

def test_create_insurance():
    # Arrange
    company = "Test Insurance"
    address = "123 Test St"
    phone = "123-456-7890"

    # Act
    Insurance(database_connector, company, address, phone)
    database_connector.cursor.execute("SELECT * FROM Insurance WHERE company=%s AND address=%s AND phone=%s;", (company, address, phone))

    # Assert
    assert database_connector.cursor.fetchone() is not None, "The insurance company isn't saved to the database"


def test_update_insurance_new_company(monkeypatch: MonkeyPatch):
    # Arrange
    database_connector.cursor.execute("INSERT INTO Insurance(insuranceID, company, address, phone) VALUES (1000, 'Old Insurance', 'Old Address', 'Old Phone');")

    # Act
    updated_value = "New Insurance"
    inputs = ["1000", updated_value, "", ""]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))  # Replaces the inputs inside update function with the above inputs array

    Insurance.update_insurance(database_connector)

    # Assert
    database_connector.cursor.execute("SELECT * FROM Insurance WHERE insuranceID=1000 AND company=%s;", (updated_value,))
    assert database_connector.cursor.fetchone() is not None, "Insurance company not updated"


def test_update_insurance_new_address(monkeypatch: MonkeyPatch):
    # Arrange
    database_connector.cursor.execute("INSERT INTO Insurance(insuranceID, company, address, phone) VALUES (1001, 'Test Insurance', 'Old Address', 'Old Phone');")

    # Act
    updated_value = "New Address"
    inputs = ["1001", "", updated_value, ""]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))  # Replaces the inputs inside update function with the above inputs array

    Insurance.update_insurance(database_connector)

    # Assert
    database_connector.cursor.execute("SELECT * FROM Insurance WHERE insuranceID=1001 AND address=%s;", (updated_value,))
    assert database_connector.cursor.fetchone() is not None, "Insurance company not updated"


def test_update_insurance_new_phone(monkeypatch: MonkeyPatch):
    # Arrange
    database_connector.cursor.execute("INSERT INTO Insurance(insuranceID, company, address, phone) VALUES (1002, 'Test Insurance', 'Old Address', 'Old Phone');")

    # Act
    updated_value = "New Phone"
    inputs = ["1002", "", "", updated_value]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))  # Replaces the inputs inside update function with the above inputs array

    Insurance.update_insurance(database_connector)

    # Assert
    database_connector.cursor.execute("SELECT * FROM Insurance WHERE insuranceID=1002 AND phone=%s;", (updated_value,))
    assert database_connector.cursor.fetchone() is not None, "Insurance company not updated"


def test_delete_insurance():
    # Arrange
    database_connector.cursor.execute("INSERT INTO Insurance(insuranceID, company, address, phone) VALUES (2000, 'Test Insurance', '123 Test St', '123-456-7890');")
    database_connector.db.commit()

    # Act
    Insurance.delete_insurance(database_connector, "2000")

    # Assert
    database_connector.cursor.execute("SELECT * FROM Insurance WHERE insuranceID=2000 AND company='Test Insurance';")
    assert database_connector.cursor.fetchone() is None, "Insurance company not deleted from the database"


def test_find_insurance(monkeypatch: MonkeyPatch):
    # Arrange
    database_connector.cursor.execute("INSERT INTO Insurance(insuranceID, company, address, phone) VALUES (3000, 'Test Insurance', '123 Test St', '123-456-7890');")
    database_connector.db.commit()

    # Act
    inputs = ["3000", "Test Insurance", "123 Test St", "123-456-7890"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))  # Replaces the inputs inside update function with the above inputs array
    insurance_found = Insurance.find_insurance(database_connector)

    # Assert
    assert len(insurance_found) >= 1, "Couldn't search for an insurance company"
