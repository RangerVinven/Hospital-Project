from classes.Drug import Drug
from utils.database_connector import database_connector

def show_drug_menu():
    menu = '''
1. List drugs
2. Search for a drug
3. Edit a drug
4. Delete a drug
5. Back
'''

    while True:
        print(menu)
        selected_option = input("Enter your option: ")

        while selected_option not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice")
            selected_option = input("Enter your option: ")

        # Lists all the drugs
        if selected_option == "1":
            Drug.list_drugs(database_connector)

        elif selected_option == "2":
            Drug.find_drug(database_connector)

        elif selected_option == "3":
            Drug.update_drug(database_connector)

        elif selected_option == "4":
            Drug.delete_drug(database_connector)

        else:
            break