import json
import os

# Define the filename for storing contacts
FILENAME = 'contacts.json'

def load_contacts():
    """Load contacts from the JSON file."""
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(FILENAME, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def edit_contact(contacts):
    """Edit an existing contact."""
    name = input("Enter the name of the contact to edit: ")
    
    if name in contacts:
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email address (leave blank to keep current): ")
        
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        
        save_contacts(contacts)
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
