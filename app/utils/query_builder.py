class QueryBuilder():
    # Returns a query that can be used to find records for a specific a table
    @staticmethod
    def create_find_query(table_name: str, column_names: tuple, column_values: tuple):
        # Creates the initial query
        query = "SELECT * FROM {} WHERE 1=1".format(table_name)
        variables = []

        # Adds each search parameters to the query
        # If the user puts "Patient", (name, address, email), ("John", "", "john@gmail.com")
        # The query will be SELECT * FROM Patient WHERE 1=1 AND name=John AND email=john@gmail.com;
        for i in range(len(column_names)):
            if column_values[i] != "":
                query += " AND {}=%s".format(column_names[i])
                variables.append(column_values[i])

        query += ";"

        return query, variables

    @staticmethod
    def create_update_query(table_name: str, table_id_names: tuple, table_id_values: tuple, column_names: tuple, column_values: tuple):
        query = "UPDATE {} SET {}=%s".format(table_name, table_id_names[0])
        variables = [table_id_values[0]]

        # Adds each search parameters to the query
        # If the user puts "Patient", (name, address, email), ("John", "", "john@gmail.com")
        # The query will be SELECT * FROM Patient WHERE 1=1 AND name=John AND email=john@gmail.com;
        for i in range(len(column_names)):
            if column_values[i] != "":
                query += ", {}=%s".format(column_names[i])
                variables.append(column_values[i])

        query += "WHERE 1=1"

        # Adds the ID (or IDs for composite keys) to the where clause
        for i in range(len(table_id_names)):
            query += " AND {}=%s".format(table_id_names[i])
            variables.append(table_id_values[i])

        query += ";"

        return query, variables