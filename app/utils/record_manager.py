from tabulate import tabulate

class RecordManager():

    # Prints the data, takes an array of dictionaries as a parameter
    @staticmethod
    def print_records(dataToPrint):

        if len(dataToPrint) == 0:
            print("\n")
            print("No results.\n")
            return
        
        headers = dataToPrint[0].keys()
        rows = []

        # Loops over the dataToPrint
        for data in dataToPrint:
            data_rows = []

            # Takes each value from the data and adds it to data_rows
            for header in headers:
                data_rows.append(data[header])

            rows.append(data_rows)

        print("\n")
        print(tabulate(rows, headers=headers))
        print("\n")

    # Tells the user if a record has been changed (i.e, during UPDATE and DELETE methods)
    @staticmethod
    def is_row_changed(database_connector, records_changed_message, records_not_changed_message):
        rows_changed = database_connector.cursor.rowcount
        if rows_changed > 0:
            print(records_changed_message)

        else:
            print(records_not_changed_message)
