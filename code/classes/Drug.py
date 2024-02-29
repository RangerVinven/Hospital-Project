from utils.id_generator import IDGenerator

class Drug():
    def __init__(self, database_connector, name, side_effects, benefits):
        self.drug_id = 0
        self.name = name
        self.side_effects = side_effects
        self.benefits = benefits

        self.create_drug(database_connector)

    # Saves the drug to the database
    def create_drug(self, database_connector):
        # Gets the ID
        id = IDGenerator.generate_id(db_connector=database_connector, id_length=2, hasNumbers=False, hasLetters=True, table="Drug", id_column_name="drugID")

        # Saves the drug to the database
        database_connector.cursor.execute("INSERT INTO Drug (drugID, name, sideeffects, benefits) VALUES (%s, %s, %s, %s);", (id, self.name, self.side_effects, self.benefits))
        database_connector.db.commit()
