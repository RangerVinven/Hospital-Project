from classes.Insurance import Insurance
from utils.database_connector import database_connector

def show_insurance_menu():
    menu = '''
1. Create insurance
2. List insurances
3. Search for a insurance
4. Edit a insurance
5. Delete a insurance
6. Back
'''

    insurance = Insurance()

    while True:
        print(menu)
        selected_option = input("Enter your option: ")

        while selected_option not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice")
            selected_option = input("Enter your option: ")

        # Creates the insurance
        if selected_option == "1":
            insurance.create_insurance(database_connector)

        elif selected_option == "2":
            insurance.list_insurance(database_connector)

        elif selected_option == "3":
            insurance.find_insurance(database_connector)

        elif selected_option == "4":
            insurance.update_insurance(database_connector)

        elif selected_option == "5":
            insurance.delete_insurance(database_connector)

        else:
            break