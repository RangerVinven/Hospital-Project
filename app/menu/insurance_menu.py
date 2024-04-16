from classes.Insurance import Insurance
from utils.database_connector import database_connector
from colorama import Fore

# Shows the menu
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
        print(Fore.CYAN + menu)

        # Gets the user's selected option        
        selected_option = input("Enter your option: ")

        # Ensures the user enters a valid choice
        while selected_option not in ["1", "2", "3", "4", "5", "6"]:
            print(Fore.RED + "Invalid choice")
            selected_option = input(Fore.CYAN + "Enter your option: ")

        # Creates the insurance
        if selected_option == "1":
            insurance.create_insurance(database_connector)


        # List Insurance
        elif selected_option == "2":
            insurance.list_insurance(database_connector)

        # Find Insurance
        elif selected_option == "3":
            insurance.find_insurance(database_connector)

        # Update Insurance
        elif selected_option == "4":
            insurance.update_insurance(database_connector)

        # Delete Insurance
        elif selected_option == "5":
            insurance.delete_insurance(database_connector)

        # Exit
        else:
            break