from classes.Patients import Patient
from classes.Patients import InsuredPatient

from utils.database_connector import database_connector
from colorama import Fore

# Shows the menu
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

        # Gets the users's selected option        
        selected_option = input("Enter your option: ")

        # Ensures the user enters a valid choice
        while selected_option not in ["1", "2", "3", "4", "5", "6"]:
            print(Fore.RED + "Invalid choice")
            selected_option = input(Fore.YELLOW + "Enter your option: ")

        # Creates a patient 
        if selected_option == "1":
            # Gets whether the doctor is a specialist
            is_insured = input("Is the patient insured (yes/no)? ").lower()

            # Ensures the user entered a valid input
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

        # List Patients
        elif selected_option == "2":
            patient.list_patients(database_connector)

        # Find Patient
        elif selected_option == "3":
            patient.find_patient(database_connector)

        # Update Patient
        elif selected_option == "4":
            patient.update_patient(database_connector)

        # Delete Patient
        elif selected_option == "5":
            patient.delete_patient(database_connector)

        # Exit
        else:
            break