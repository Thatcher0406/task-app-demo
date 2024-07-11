# Define a list to store patients
patients = []

# Function to add a new patient
def add_patient():
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    illness = input("Enter patient's illness: ")
    patient = {'name': name, 'age': age, 'illness': illness}
    patients.append(patient)
    print("Patient added successfully.")

# Function to display all patients
def display_patients():
    if not patients:
        print("No patients in the list.")
    else:
        print("List of Patients:")
        for idx, patient in enumerate(patients, start=1):
            print(f"Patient {idx}:")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Illness: {patient['illness']}")
            print("--------------------")

# Function to search for a patient by name
def search_patient():
    name = input("Enter patient's name to search: ")
    found = False
    for patient in patients:
        if patient['name'].lower() == name.lower():
            print("Patient found:")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Illness: {patient['illness']}")
            found = True
            break
    if not found:
        print("Patient not found.")

# Function to remove a patient by name
def remove_patient():
    name = input("Enter patient's name to remove: ")
    for patient in patients:
        if patient['name'].lower() == name.lower():
            patients.remove(patient)
            print(f"Patient '{name}' removed successfully.")
            return
    print("Patient not found.")

# Main program loop
while True:
    print("\nHospital Patient Management System")
    print("1. Add a new patient")
    print("2. Display all patients")
    print("3. Search for a patient by name")
    print("4. Remove a patient by name")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_patient()
    elif choice == '2':
        display_patients()
    elif choice == '3':
        search_patient()
    elif choice == '4':
        remove_patient()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
