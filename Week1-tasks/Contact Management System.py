class ContactManager:
    def __init__(self, filename="contacts.txt"):
        self.filename = filename
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        """Load contacts from a file."""
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    name, phone, email = line.strip().split(",")
                    self.contacts[name] = {"phone": phone, "email": email}
        except FileNotFoundError:
            self.contacts = {}

    def save_contacts(self):
        """Save contacts to a file."""
        with open(self.filename, "w") as file:
            for name, info in self.contacts.items():
                file.write(f"{name},{info['phone']},{info['email']}\n")

    def add_contact(self, name, phone, email):
        """Add a new contact."""
        if name in self.contacts:
            print("Contact already exists.")
            return
        self.contacts[name] = {"phone": phone, "email": email}
        self.save_contacts()
        print(f"Contact '{name}' added successfully.")

    def search_contact(self, name):
        """Search for a contact by name."""
        contact = self.contacts.get(name)
        if contact:
            print(f"Name: {name}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print("Contact not found.")

    def update_contact(self, name, phone=None, email=None):
        """Update an existing contact."""
        if name not in self.contacts:
            print("Contact not found.")
            return
        if phone:
            self.contacts[name]['phone'] = phone
        if email:
            self.contacts[name]['email'] = email
        self.save_contacts()
        print(f"Contact '{name}' updated successfully.")

    def display_all_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("No contacts available.")
            return
        for name, info in self.contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")






def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)

        elif choice == '2':
            name = input("Enter name to search: ")
            manager.search_contact(name)

        elif choice == '3':
            name = input("Enter name to update: ")
            phone = input("Enter new phone (leave blank if no change): ")
            email = input("Enter new email (leave blank if no change): ")
            manager.update_contact(name, phone if phone else None, email if email else None)

        elif choice == '4':
            manager.display_all_contacts()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
