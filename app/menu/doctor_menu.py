from classes.Doctors import Doctor
from classes.Doctors import Specialist

from utils.database_connector import database_connector

def show_doctor_menu():
    menu = '''
1. Create doctor
2. List doctors
3. Search for a doctor
4. Edit a doctor
5. Delete a doctor
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
            is_specialist = input("Is the doctor a specialist (yes/no)? ").lower()
            while is_specialist not in ["y", "n", "yes", "no"]:
                print("Invalid option")
                is_specialist = input("Is the doctor a specialist (yes/no)? ").lower()

            # Creates a Specialist
            if is_specialist == "y" or is_specialist == "yes":
                specialist = Specialist(database_connector)
                specialist.create_specialist(database_connector)

            # Creates a doctor
            else:
                doctor = Doctor(database_connector)
                doctor.create_doctor(database_connector)

        elif selected_option == "2":
            Doctor.list_doctors(database_connector)

        elif selected_option == "3":
            Doctor.find_doctor(database_connector)

        elif selected_option == "4":
            Doctor.update_doctor(database_connector)

        elif selected_option == "5":
            Doctor.delete_doctor(database_connector)

        else:
            break