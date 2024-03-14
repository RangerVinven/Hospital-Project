from menu.drug_menu import show_drug_menu
from menu.insurance_menu import show_insurance_menu

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

    elif selected_option == "6":
        show_insurance_menu()


if __name__ == "__main__":
    show_menu()