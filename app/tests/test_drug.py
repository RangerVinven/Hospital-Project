# Had issues running the tests. If there are issues, go to app/ and run the command:
# python3 -m app.tests.test_drug

import unittest

from ..utils.database_connector import DatabaseConnector
from ..classes.Drug import Drug

database_connector = DatabaseConnector("testing")

class TestDrug(unittest.TestCase):

    def test_create_drug(self):
        # Arrange
        drug_name = "Honey Bunny"
        side_effects = "Death"
        benefits = "None"

        # Act
        Drug(database_connector, drug_name, side_effects, benefits)
        database_connector.cursor.execute("SELECT * FROM Drug WHERE name=%s AND sideeffects=%s AND benefits=%s;", (drug_name, side_effects, benefits))

        # Assert
        self.assertIsNotNone(database_connector.cursor.fetchone(), "The drug isn't saved to the database")

if __name__ == "__main__":
    unittest.main()