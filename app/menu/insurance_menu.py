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

    while True:
        print(menu)
        selected_option = input("Enter your option: ")

        while selected_option not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice")
            selected_option = input("Enter your option: ")

        # Lists all the insurances
        if selected_option == "1":
            Insurance(database_connector)

        elif selected_option == "2":
            Insurance.list_insurance(database_connector)

        elif selected_option == "3":
            Insurance.find_insurance(database_connector)

        elif selected_option == "4":
            Insurance.update_insurance(database_connector)

        elif selected_option == "5":
            Insurance.delete_insurance(database_connector)

        else:
            break