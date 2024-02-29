from utils.id_generator import IDGenerator

class Drug():
    def __init__(self, database_connector, name, side_effects, benefits):
        self.drug_id = IDGenerator.generate_id(db_connector=database_connector, id_length=2, hasNumbers=False, hasLetters=True, table="Drug", id_column_name="drugID")
        self.name = name
        self.side_effects = side_effects
        self.benefits = benefits

        self._create_drug(database_connector)

    # Saves the drug to the database
    def _create_drug(self, database_connector):
        # Saves the drug to the database
        database_connector.cursor.execute("INSERT INTO Drug (drugID, name, sideeffects, benefits) VALUES (%s, %s, %s, %s);", (self.drug_id, self.name, self.side_effects, self.benefits))
        database_connector.db.commit()
