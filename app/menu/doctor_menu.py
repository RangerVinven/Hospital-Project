from classes.Doctors import Doctor
from utils.database_connector import database_connector

def show_doctor_menu():
    menu = '''
1. List doctors
2. Search for a doctor
3. Edit a doctor
4. Delete a doctor
5. Back
'''

    while True:
        print(menu)
        selected_option = input("Enter your option: ")

        while selected_option not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice")
            selected_option = input("Enter your option: ")

        # Lists all the doctors
        if selected_option == "1":
            Doctor.list_doctors(database_connector)

        elif selected_option == "2":
            Doctor.find_doctor(database_connector)

        elif selected_option == "3":
            Doctor.update_doctor(database_connector)

        elif selected_option == "4":
            Doctor.delete_doctor(database_connector)

        else:
            break