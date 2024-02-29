# Had issues running the tests. If there are issues, go to app/ and run the command:
# python3 -m pytest app/tests/test_drug.py

from pytest import MonkeyPatch, fixture

from ..utils.database_connector import DatabaseConnector
from ..classes.Drug import Drug

database_connector = DatabaseConnector("testing")

@fixture(scope="module", autouse=True)
def setup_database():
    database_connector.cursor.execute("DELETE FROM Drug;")
    database_connector.db.commit()

@fixture(scope="module")
def teardown():
    database_connector.close_connection()

def test_create_drug():
    # Arrange
    drug_name = "Honey Bunny"
    side_effects = "Death"
    benefits = "None"

    # Act
    Drug(database_connector, drug_name, side_effects, benefits)
    database_connector.cursor.execute("SELECT * FROM Drug WHERE name=%s AND sideeffects=%s AND benefits=%s;", (drug_name, side_effects, benefits))

    # Assert
    assert database_connector.cursor.fetchone() is not None, "The drug isn't saved to the database"

def test_update_drug_new_name(monkeypatch: MonkeyPatch):
    # Arrange
    database_connector.cursor.execute("INSERT INTO Drug(drugID, name, sideeffects, benefits) VALUES (1000, 'update_me', 'no side effects', 'no benefits');")

    # Act
    updated_value = "new drug name"
    inputs = ["1000", updated_value, "", ""]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))  # Replaces the inputs inside update function with the above inputs array
    
    Drug.update_drug(database_connector)
    
    
    # Assert
    database_connector.cursor.execute("SELECT * FROM Drug WHERE drugID=1000 AND name=%s;", (updated_value,))
    assert database_connector.cursor.fetchone() is not None, "Drug not updated"

def test_update_drug_new_sideeffects(monkeypatch: MonkeyPatch):
    # Arrange
    database_connector.cursor.execute("INSERT INTO Drug(drugID, name, sideeffects, benefits) VALUES (1001, 'cool drug name', 'update me', 'no benefits');")

    # Act
    updated_value = "really cool side effects"
    inputs = ["1001", "", updated_value, ""]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))  # Replaces the inputs inside update function with the above inputs array
    
    Drug.update_drug(database_connector)
    
    # Assert
    database_connector.cursor.execute("SELECT * FROM Drug WHERE drugID=1001 AND sideeffects=%s;", (updated_value,))
    assert database_connector.cursor.fetchone() is not None, "Drug not updated"

def test_update_drug_new_benefits(monkeypatch: MonkeyPatch):
    # Arrange
    database_connector.cursor.execute("INSERT INTO Drug(drugID, name, sideeffects, benefits) VALUES (1002, 'cool drug name', 'no side effects', 'update me');")

    # Act
    updated_value = "Really cool benefits"
    inputs = ["1002", "", "", updated_value]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))  # Replaces the inputs inside update function with the above inputs array
    
    Drug.update_drug(database_connector)
    
    # Assert
    database_connector.cursor.execute("SELECT * FROM Drug WHERE drugID=1002 AND benefits=%s;", (updated_value,))
    assert database_connector.cursor.fetchone() is not None, "Drug not updated"

