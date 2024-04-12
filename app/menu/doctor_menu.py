from classes.Doctors import Doctor, Specialist
from colorama import Fore, Style

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

    doctor = Doctor()

    while True:
        print(Fore.CYAN + menu)
        selected_option = input("Enter your option: ")
        
        while selected_option not in ["1", "2", "3", "4", "5", "6"]:
            print(Fore.RED + "Invalid choice")
            selected_option = input(Fore.CYAN + "Enter your option: ")

        # Calls the relevant method
        if selected_option == "1":
            # Gets whether the doctor is a specialist
            is_specialist = input(Fore.MAGENTA + "Is the doctor a specialist (yes/no)? ").lower()
            while is_specialist not in ["y", "n", "yes", "no"]:
                print(Fore.RED + "Invalid option")
                is_specialist = input(Fore.MAGENTA + "Is the doctor a specialist (yes/no)? ").lower()

            # Creates a Specialist
            if is_specialist == "y" or is_specialist == "yes":
                specialist = Specialist()
                specialist.create_specialist(database_connector)

            # Creates a doctor
            else:
                doctor.create_doctor(database_connector)

        elif selected_option == "2":
            doctor.list_doctors(database_connector)

        elif selected_option == "3":
            doctor.find_doctor(database_connector)

        elif selected_option == "4":
            doctor.update_doctor(database_connector)

        elif selected_option == "5":
            doctor.delete_doctor(database_connector)

        else:
            break