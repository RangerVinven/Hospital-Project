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
    pass
    # Arrange
    
    # Act
    

    # Assert
    



def test_update_insurance_new_name(monkeypatch: MonkeyPatch):
    pass
    # Arrange

    # Act    
    
    # Assert


def test_update_insurance_new_sideeffects(monkeypatch: MonkeyPatch):
    pass
    # Arrange
    

    # Act
    
    
    # Assert


def test_update_insurance_new_benefits(monkeypatch: MonkeyPatch):
    pass
    # Arrange


    # Act

    
    # Assert


def test_delete_insurance():
    pass
    # Arrange

    # Act

    # Assert

def test_find_insurance(monkeypatch: MonkeyPatch):
    pass
    # Arrange

    # Act

    # Assert