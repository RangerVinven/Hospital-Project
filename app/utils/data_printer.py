from tabulate import tabulate

# Prints the data, takes an array of dictionaries as a parameter
def print_data(dataToPrint):
    headers = dataToPrint[0].keys()
    rows = []

    # Loops over the dataToPrint
    for data in dataToPrint:
        data_rows = []

        # Takes each value from the data and adds it to data_rows
        for header in headers:
            data_rows.append(data[header])

        rows.append(data_rows)

    print(tabulate(rows, headers=headers))