from colorama import Fore

from classes.Visit import Visit
from utils.database_connector import database_connector

def show_visit_menu():
    menu = '''
1. Create visit
2. List visits
3. Search for a visit
4. Edit a visit
5. Delete a visit
6. Back
'''

    visit = Visit()

    while True:
        print(Fore.YELLOW + menu)
        selected_option = input("Enter your option: ")

        while selected_option not in ["1", "2", "3", "4", "5", "6"]:
            print(Fore.RED + "Invalid choice")
            selected_option = input(Fore.YELLOW + "Enter your option: ")

        # Creates a visit
        if selected_option == "1":
            visit.create_visit(database_connector)

        elif selected_option == "2":
            visit.list_visits(database_connector)

        elif selected_option == "3":
            visit.find_visit(database_connector)

        elif selected_option == "4":
            visit.update_visit(database_connector)

        elif selected_option == "5":
            visit.delete_visit(database_connector)

        else:
            break