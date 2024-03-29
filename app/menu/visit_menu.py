from classes.Visit import Visit
from utils.database_connector import database_connector

def show_visit_menu():
    menu = '''
1. List visits
2. Search for a visit
3. Edit a visit
4. Delete a visit
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
            Visit.list_visits(database_connector)

        elif selected_option == "2":
            Visit.find_visit(database_connector)

        elif selected_option == "3":
            Visit.update_visit(database_connector)

        elif selected_option == "4":
            Visit.delete_visit(database_connector)

        else:
            break