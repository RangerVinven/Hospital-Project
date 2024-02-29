from ..utils.id_generator import IDGenerator

class Drug():
    def __init__(self, database_connector, name, side_effects, benefits):
        self.drug_id = IDGenerator.generate_id(db_connector=database_connector, id_length=7, hasNumbers=True, hasLetters=False, table="Drug", id_column_name="drugID")
        self.name = name
        self.side_effects = side_effects
        self.benefits = benefits

        self._create_drug(database_connector)

    # Saves the drug to the database
    def _create_drug(self, database_connector):
        # Saves the drug to the database
        database_connector.cursor.execute("INSERT INTO Drug (drugID, name, sideeffects, benefits) VALUES (%s, %s, %s, %s);", (self.drug_id, self.name, self.side_effects, self.benefits))
        database_connector.db.commit()

    # Returns a list of all the drugs
    @staticmethod    
    def list_drugs(self, database_connector):
        database_connector.cursor.execute("SELECT * FROM Drug;")
        return database_connector.fetchall()

    @staticmethod
    def update_drug(database_connector):
        # Gets the items the user wishes to change
        id = input("Please enter the ID of the drug you wish to update: ") or ""
        name = input("Please enter the new name (leave blank for no change): ") or ""
        side_effects = input("Please enter the new side effects (leave blank for no change): ") or ""
        benefits = input("Please enter the new benefits effects (leave blank for no change): ") or ""

        # The inital query
        query = "UPDATE Drug SET drugID=%s"
        variables = [id]

        # Adds the "to-be updated" variables to the query
        if name:
            query += ", name=%s"
            variables.append(name)
        
        if side_effects:
            query += ", sideeffects=%s"
            variables.append(side_effects)
        
        if benefits:
            query += ", benefits=%s"
            variables.append(benefits)

        query += " WHERE drugID=%s;"
        variables.append(id)

        database_connector.cursor.execute(query, tuple(variables))        
        database_connector.db.commit()

    
    @staticmethod
    def delete_drug(database_connector, id):
        database_connector.cursor.execute("DELETE FROM Drug WHERE drugID=%s", (id,))
        database_connector.db.commit()