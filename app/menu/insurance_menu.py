from classes.Insurance import Insurance
from utils.database_connector import database_connector

def show_insurance_menu():
    menu = '''
1. List insurances
2. Search for a insurance
3. Edit a insurance
4. Delete a insurance
5. Back
'''

    while True:
        print(menu)
        selected_option = input("Enter your option: ")

        while selected_option not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice")
            selected_option = input("Enter your option: ")

        # Lists all the insurances
        if selected_option == "1":
            Insurance.list_insurance(database_connector)

        elif selected_option == "2":
            Insurance.find_insurance(database_connector)

        elif selected_option == "3":
            Insurance.update_insurance(database_connector)

        elif selected_option == "4":
            Insurance.delete_insurance(database_connector)

        else:
            break