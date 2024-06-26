from classes.Patients import Patient
from classes.Patients import InsuredPatient

from utils.database_connector import database_connector
from colorama import Fore

def show_patient_menu():
    menu = '''
1. Create patient
2. List patients
3. Search for a patient
4. Edit a patient
5. Delete a patient
6. Back
'''

    patient = Patient()

    while True:
        print(Fore.YELLOW + menu)
        selected_option = input("Enter your option: ")

        while selected_option not in ["1", "2", "3", "4", "5", "6"]:
            print(Fore.RED + "Invalid choice")
            selected_option = input(Fore.YELLOW + "Enter your option: ")

        # Calls the relevant method
        if selected_option == "1":
            # Gets whether the doctor is a specialist
            is_insured = input("Is the patient insured (yes/no)? ").lower()
            while is_insured not in ["y", "n", "yes", "no"]:
                print("Invalid option")
                is_insured = input("Is the patient insured (yes/no)? ").lower()

            # Creates a InsuredPatient
            if is_insured == "y" or is_insured == "yes":
                insured_patient = InsuredPatient(database_connector)
                insured_patient.create_insured_patient(database_connector)

            # Creates a Patient
            else:
                patient.create_patient(database_connector)

        elif selected_option == "2":
            patient.list_patients(database_connector)

        elif selected_option == "3":
            patient.find_patient(database_connector)

        elif selected_option == "4":
            patient.update_patient(database_connector)

        elif selected_option == "5":
            patient.delete_patient(database_connector)

        else:
            break