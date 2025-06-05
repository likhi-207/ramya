def add_contact (contacts):
    file = open("./try.txt", "a")
    name = input("enter name:")
    mobile = int(input("enter mobile number:"))
    contacts[name] = mobile
    file.write(f"{name},{mobile}\n")
    file.close()
def view_all(contacts):
    print("\n")
    for i in contacts:
        print(f"{i}:{contacts[i]}")
def delete_contact(contacts):
    
    name_to_delete = input("enter contact to delete:")
    del contacts[name_to_delete]
    print("delete contact",name_to_delete)
def find_contact(contacts):
    find = input("enter to search contact:")
    found = False
    for i in contacts:
        if find in i:
            found = True
            print(f"{i}:{contacts[find]}")
        if not found:
            print("contact not found")
def edit_contact(contacts):
    file = open("./try.txt", "r")  
    name = input("enter contact name to edit:")
    mobile = int(input("enter new number"))
    contacts[name] = mobile
    contacts = file.read
    list_contacts = contacts.split("\n")
    print(list_contacts)
    file.close()