class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        contact = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print(f"Contact added successfully: {name}")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(f"Name: {contact['name']}\tPhone: {contact['phone_number']}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['phone_number']:
                results.append(contact)
        return results

    def update_contact(self, name, phone_number, email, address):
        for contact in self.contacts:
            if contact['name'] == name:
                contact['phone_number'] = phone_number
                contact['email'] = email
                contact['address'] = address
                print(f"Contact updated successfully: {name}")
                return
        print(f"Contact not found: {name}")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                print(f"Contact deleted successfully: {name}")
                return
        print(f"Contact not found: {name}")

def display_menu():
    print("\nCodSoft Contact Book\n")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit\n")

def main():
    contact_book = ContactBook()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_book.view_contact_list()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(query)
            if results:
                print("\nSearch Results:")
                for result in results:
                    print(result)
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_book.update_contact(name, phone_number, email, address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting CodSoft Contact Book... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
