from classes.Patients import Patient
from utils.database_connector import database_connector

def show_patient_menu():
    menu = '''
1. Create patient
2. List patients
3. Search for a patient
4. Edit a patient
5. Delete a patient
6. Back
'''

    while True:
        print(menu)
        selected_option = input("Enter your option: ")

        while selected_option not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice")
            selected_option = input("Enter your option: ")

        # Lists all the patients
        if selected_option == "1":
            Patient.list_patients(database_connector)

        elif selected_option == "2":
            Patient.find_patient(database_connector)

        elif selected_option == "3":
            Patient.update_patient(database_connector)

        elif selected_option == "4":
            Patient.delete_patient(database_connector)

        else:
            break