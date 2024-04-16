from classes.Drug import Drug
from utils.database_connector import database_connector

from colorama import Fore

# Shows the menu
def show_drug_menu():
    menu = '''
1. Create drug
2. List drugs
3. Search for a drug
4. Edit a drug
5. Delete a drug
6. Back
'''

    drug = Drug()

    while True:
        print(Fore.YELLOW + menu)

        # Gets the user's selected option
        selected_option = input("Enter your option: ")

        # Ensures the user enters a valid choice
        while selected_option not in ["1", "2", "3", "4", "5", "6"]:
            print(Fore.RED + "Invalid choice")
            selected_option = input(Fore.Yellow + "Enter your option: ")

        # Create Drug
        if selected_option == "1":
            drug.create_drug(database_connector)

        # List Drugs
        elif selected_option == "2":
            drug.list_drugs(database_connector)

        # Find Drug
        elif selected_option == "3":
            drug.find_drug(database_connector)

        # Update Drug
        elif selected_option == "4":
            drug.update_drug(database_connector)

        # Delete Drug
        elif selected_option == "5":
            drug.delete_drug(database_connector)

        # Exit
        else:
            break
