from classes.Prescription import Prescription
from utils.database_connector import database_connector

def show_prescription_menu():
    menu = '''
1. List prescriptions
2. Search for a prescription
3. Edit a prescription
4. Delete a prescription
5. Back
'''

    while True:
        print(menu)
        selected_option = input("Enter your option: ")

        while selected_option not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice")
            selected_option = input("Enter your option: ")

        # Lists all the prescriptions
        if selected_option == "1":
            Prescription.list_prescriptions(database_connector)

        elif selected_option == "2":
            Prescription.find_prescription(database_connector)

        elif selected_option == "3":
            Prescription.update_prescription(database_connector)

        elif selected_option == "4":
            Prescription.delete_prescription(database_connector)

        else:
            break