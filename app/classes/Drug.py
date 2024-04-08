from utils.id_generator import IDGenerator
from utils.query_builder import QueryBuilder
from utils.record_manager import RecordManager
from utils.validator import Validator, TableAndColumn

class Drug():
    def __init__(self):
        self.validator = Validator()
        self.column_options = {
            "drug_id": { "max_length":  7 },
            "name": { "max_length": 50 },
            "side_effects": { "max_length": 200 },
            "benefits": { "max_length": 200 },
        }

    # Saves the drug to the database
    def create_drug(self, database_connector):
        self.drug_id = IDGenerator.generate_id(db_connector=database_connector, id_length=7, hasNumbers=True, hasLetters=False, table="Drug", id_column_name="drugID")
        self.name = self.validator.get_input(database_connector, "What's the drug's name? ", self.column_options["name"])
        self.side_effects = self.validator.get_input(database_connector, "What's the drug's side effects? ", self.column_options["side_effects"])
        self.benefits = self.validator.get_input(database_connector, "What's the drug's benefits? ", self.column_options["benefits"])
        
        # Saves the drug to the database
        database_connector.cursor.execute("INSERT INTO Drug (drugID, name, sideeffects, benefits) VALUES (%s, %s, %s, %s);", (self.drug_id, self.name, self.side_effects, self.benefits))
        database_connector.db.commit()

    # Returns a list of all the drugs
    def list_drugs(self, database_connector):
        database_connector.cursor.execute("SELECT * FROM Drug;")
        drugs = database_connector.cursor.fetchall()

        RecordManager.print_records(drugs)
    
    def find_drug(self, database_connector):

        # Gets the items the user wishes to change
        id = self.validator.get_input(database_connector, "Please enter the ID of the drug you wish to search for (leave blank if unknown): ", self.column_options["drug_id"])
        name = self.validator.get_input(database_connector, "Please enter the name of drug you wish to search for (leave blank if unknown): ", self.column_options["name"])
        side_effects = self.validator.get_input(database_connector, "Please enter the side effects of drug you wish to search for (leave blank if unknown): ", self.column_options["side_effects"])
        benefits = self.validator.get_input(database_connector, "Please enter the benefits effects of drug you wish to search for (leave blank if unknown): ", self.column_options["benefits"] )

        # Gets the query to find the Drug(s)
        query, variables = QueryBuilder.create_find_query("Drug", ("drugID", "name", "sideeffects", "benefits"), (id, name, side_effects, benefits))

        database_connector.cursor.execute(query, tuple(variables))        
        RecordManager.print_records(database_connector.cursor.fetchall())

    def update_drug(self, database_connector):
        # Gets the items the user wishes to change
        id = self.validator.get_input(database_connector, "Please enter the ID of the drug you wish to update: ", { "max_length": self.column_options["drug_id"]["max_length"], "exists_in_table": TableAndColumn(table_name="Drug", column_name="drugID") })
        name = self.validator.get_input(database_connector, "Please enter the new name (leave blank for no change): ", self.column_options["name"]) 
        side_effects = self.validator.get_input(database_connector, "Please enter the new side effects (leave blank for no change): ", self.column_options["side_effects"])
        benefits = self.validator.get_input(database_connector, "Please enter the new benefits effects (leave blank for no change): ", self.column_options["benefits"])

        query, variables = QueryBuilder.create_update_query("Drug", ["DrugID"], [id], ("name", "sideeffects", "benefits"), (name, side_effects, benefits))

        database_connector.cursor.execute(query, tuple(variables))
        RecordManager.is_row_changed(database_connector, "Drug updated", "Drug not found, no drugs changed")

        database_connector.db.commit()

    def delete_drug(self, database_connector):
        id = self.validator.get_input("Please enter the ID of the drug you wish to delete: ", { "exists_in_table": TableAndColumn(table_name="Drug", column_name="drugID") })
        database_connector.cursor.execute("DELETE FROM Drug WHERE drugID=%s", (id,))

        RecordManager.is_row_changed(database_connector, "Drug deleted", "Drug not found, no drugs deleted")
        database_connector.db.commit()