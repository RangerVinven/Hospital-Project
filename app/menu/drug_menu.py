from classes.Drug import Drug
from utils.database_connector import database_connector

def show_drug_menu():
    menu = '''
1. Create drug
2. List drugs
3. Search for a drug
4. Edit a drug
5. Delete a drug
6. Back
'''

    while True:
        print(menu)
        selected_option = input("Enter your option: ")

        while selected_option not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice")
            selected_option = input("Enter your option: ")

        # Lists all the drugs
        if selected_option == "1":
            Drug(database_connector)

        elif selected_option == "2":
            Drug.list_drugs(database_connector)

        elif selected_option == "3":
            Drug.find_drug(database_connector)

        elif selected_option == "4":
            Drug.update_drug(database_connector)

        elif selected_option == "5":
            Drug.delete_drug(database_connector)

        else:
            break