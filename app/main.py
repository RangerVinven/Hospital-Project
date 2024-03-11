from classes.Drug import Drug
from utils.database_connector import database_connector

def show_menu():
    main_menu = '''    
1. Patients
2. Doctors
3. Drugs
4. Prescription
5. Visits
6. Insurance
99. Exit
'''
    print(main_menu)
    
    # Gets the selected option
    selected_option = input("Enter which category you'd like to interact with: ")
    while selected_option not in ["1", "2", "3", "4", "5", "6", "99"]:
        print("Invalid option")
        selected_option = input("Enter which category you'd like to interact with: ")

    # Shows the appropreate menu
    if selected_option == "3":
        show_drug_menu()

def show_drug_menu():
    menu = '''
1. List drugs
2. Search for a drug
3. Edit a drug
4. Delete a drug
5. Back
'''

    print(menu)
    selected_option = input("Enter your option: ")

    if selected_option == "1":
        Drug.list_drugs(database_connector)



if __name__ == "__main__":
    show_menu()