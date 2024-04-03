from classes.Patients import Patient
from classes.Patients import InsuredPatient

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

        while selected_option not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice")
            selected_option = input("Enter your option: ")

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
                doctor = Patient(database_connector)
                doctor.create_patient(database_connector)

        elif selected_option == "2":
            Patient.list_patients(database_connector)

        elif selected_option == "3":
            Patient.find_patient(database_connector)

        elif selected_option == "4":
            Patient.update_patient(database_connector)

        elif selected_option == "5":
            Patient.delete_patient(database_connector)

        else:
            break