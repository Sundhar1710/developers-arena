CONTACTS_FILE = "contacts.txt"
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    if not name or not phone:
        print("Name and phone number are required!")
        return
    
    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added successfully!\n")

def view_contacts():
    with open(CONTACTS_FILE, "r") as file:
        lines = file.readlines()
        if not lines:
            print("No contacts found.\n")
            return
        print("\n--- Contact List ---")
        for id, line in enumerate(lines, start=1):
            name, phone, email = line.strip().split(",")
            print(f"{id}. Name: {name} | Phone: {phone} | Email: {email}")
        print()

def search_contacts():
    search_term = input("Enter name or phone to search: ").strip().lower()
    with open(CONTACTS_FILE, "r") as file:
        results = []
        for line in file:
            name, phone, email = line.strip().split(",")
            if search_term in name.lower() or search_term in phone:
                results.append((name, phone, email))
        if results:
            print("\n--- Search Results ---")
            for id, (name, phone, email) in enumerate(results, 1):
                print(f"{id}. Name: {name} | Phone: {phone} | Email: {email}")
                print()
        else:
            print("No matching contacts found.\n")

def main():
    while True:
        print("---- Contact Book ----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()