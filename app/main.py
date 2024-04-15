from menu.drug_menu import show_drug_menu
from menu.visit_menu import show_visit_menu
from menu.prescription_menu import show_prescription_menu
from menu.insurance_menu import show_insurance_menu
from menu.doctor_menu import show_doctor_menu
from menu.patient_menu import show_patient_menu
from colorama import Fore, Style

def show_menu():

    print(Style.RESET_ALL)

    while True:
        main_menu = '''
    1. Patients
    2. Doctors
    3. Drugs
    4. Prescription
    5. Visits
    6. Insurance
    99. Exit
    '''
        print(Fore.BLUE + main_menu)
        
        # Gets the selected option
        selected_option = input("Enter which category you'd like to interact with: ")

        while selected_option not in ["1", "2", "3", "4", "5", "6", "99"]:
            print(Fore.RED + "Invalid option")
            selected_option = input(Fore.BLUE + "Enter which category you'd like to interact with: ")

        # Shows the appropreate menu
        if selected_option == "1":
            show_patient_menu()

        elif selected_option == "2":
            show_doctor_menu()

        elif selected_option == "3":
            show_drug_menu()

        elif selected_option == "4":
            show_prescription_menu()

        elif selected_option == "5":
            show_visit_menu()

        elif selected_option == "6":
            show_insurance_menu()

        else:
            print(Style.RESET_ALL)
            break


if __name__ == "__main__":
    show_menu()
