from utils.id_generator import IDGenerator
from utils.query_builder import QueryBuilder
from utils.record_manager import RecordManager

class Drug():
    def __init__(self, database_connector):
        self.drug_id = IDGenerator.generate_id(db_connector=database_connector, id_length=7, hasNumbers=True, hasLetters=False, table="Drug", id_column_name="drugID")
        self.name = input("What's the drug's name? ")
        self.side_effects = input("What's the drug's side effects? ")
        self.benefits = input("What's the drug's benefits? ")

        self._create_drug(database_connector)

    # Saves the drug to the database
    def _create_drug(self, database_connector):
        # Saves the drug to the database
        database_connector.cursor.execute("INSERT INTO Drug (drugID, name, sideeffects, benefits) VALUES (%s, %s, %s, %s);", (self.drug_id, self.name, self.side_effects, self.benefits))
        database_connector.db.commit()

    # Returns a list of all the drugs
    @staticmethod    
    def list_drugs(database_connector):
        database_connector.cursor.execute("SELECT * FROM Drug;")
        drugs = database_connector.cursor.fetchall()

        RecordManager.print_records(drugs)
    
    @staticmethod
    def find_drug(database_connector):

        # Gets the items the user wishes to change
        id = input("Please enter the ID of the drug you wish to search for (leave blank if unknown): ") or ""
        name = input("Please enter the name of drug you wish to search for (leave blank if unknown): ") or ""
        side_effects = input("Please enter the side effects of drug you wish to search for (leave blank if unknown): ") or ""
        benefits = input("Please enter the benefits effects of drug you wish to search for (leave blank if unknown): ") or ""

        # Gets the query to find the Drug(s)
        query, variables = QueryBuilder.create_find_query("Drug", ("drugID", "name", "sideeffects", "benefits"), (id, name, side_effects, benefits))

        database_connector.cursor.execute(query, tuple(variables))        
        RecordManager.print_records(database_connector.cursor.fetchall())

    @staticmethod
    def update_drug(database_connector):
        # Gets the items the user wishes to change
        id = input("Please enter the ID of the drug you wish to update: ") or ""
        name = input("Please enter the new name (leave blank for no change): ") or ""
        side_effects = input("Please enter the new side effects (leave blank for no change): ") or ""
        benefits = input("Please enter the new benefits effects (leave blank for no change): ") or ""

        query, variables = QueryBuilder.create_update_query("Drug", ["DrugID"], [id], ("name", "sideeffects", "benefits"), (name, side_effects, benefits))

        database_connector.cursor.execute(query, tuple(variables))
        RecordManager.is_row_changed(database_connector, "Drug updated", "Drug not found, no drugs changed")

        database_connector.db.commit()

    @staticmethod
    def delete_drug(database_connector):
        id = input("Please enter the ID of the drug you wish to delete: ")
        database_connector.cursor.execute("DELETE FROM Drug WHERE drugID=%s", (id,))

        RecordManager.is_row_changed(database_connector, "Drug deleted", "Drug not found, no drugs deleted")
        database_connector.db.commit()