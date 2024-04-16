from colorama import Fore
from classes.Prescription import Prescription
from utils.database_connector import database_connector

# Shows the menu
def show_prescription_menu():
    menu = '''
1. Create prescription
2. List prescriptions
3. Search for a prescription
4. Edit a prescription
5. Delete a prescription
6. Back
'''

    prescription = Prescription()

    while True:
        print(Fore.CYAN + menu)
        
        # Gets the user's selected option        
        selected_option = input("Enter your option: ")

        # Ensures the user enters a valid choice
        while selected_option not in ["1", "2", "3", "4", "5", "6"]:
            print(Fore.RED + "Invalid choice")
            selected_option = input(Fore.CYAN + "Enter your option: ")

        # Create Prescription
        if selected_option == "1":
            prescription.create_prescription(database_connector)

        # List Prescriptions
        elif selected_option == "2":
            prescription.list_prescriptions(database_connector)

        # Find Prescription
        elif selected_option == "3":
            prescription.find_prescription(database_connector)

        # Update Prescription
        elif selected_option == "4":
            prescription.update_prescription(database_connector)

        # Delete Prescription
        elif selected_option == "5":
            prescription.delete_prescription(database_connector)

        # Exit
        else:
            break