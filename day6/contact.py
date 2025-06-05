def add_contact(contacts):
    with open("try.txt", "a") as file:
        name = input("Enter Contact Name: ")
        mobile = input("Enter mobile number: ")
        contacts[name] = mobile
        msg = f"Added contact: {name} : {mobile}"
        print(msg)
        file.write(msg + "\n")

def view_contacts(contacts):
    with open("./try.txt,", "a")as file:
        if contacts:
            for name, number in contacts.items():
                msg = f"{name} : {number}"
                print(msg)
                file.write(msg + "\n")
        else:
            msg = "No contacts to display"
            print(msg)
            file.write(msg + "\n")

def delete_contact(contacts):
    name = input("Enter contact name: ")
    with open("new.txt", "a") as file:
        if name in contacts:
            del contacts[name]
            msg = f"Deleted contact: {name}"
            print(msg)
            file.write(msg + "\n")
        else:
            msg = "No contact found"
            print(msg)
            file.write(msg + "\n")

def find_contact(contacts):
    name = input("Enter name to search: ")
    found = False
    with open("new.txt", "a") as file:
        for key in contacts:
            if name in key:
                msg = f"{key} : {contacts[key]}"
                print(msg)
                file.write(msg + "\n")
                found = True
        if not found:
            msg = "Query not Found!!!"
            print(msg)
            file.write(msg + "\n")

def edit_contact(contacts):
    name = input("Enter contact name to edit: ")
    with open("contact.txt", "a") as file:
        if name in contacts:
            number = input("Enter new number: ")
            contacts[name] = number
            msg = f"Edited contact: {name}"
            print(msg)
            file.write(msg + "\n")
        else:
            msg = "Contact not found"
            print(msg)
            file.write(msg + "\n")