import contact
contacts = { }
print("--contact app--")
while True:
    try:
        print("\n\n choice")
        print("1. add contact")
        print("2. view all contacts")
        print("3. delete contact")
        print("4. find contact")
        print("5. edit contact and number")
        print("6. exist")
        choice = int(input("enter choice:"))
        if choice == 1:
            contact.add_contact(contacts)
        elif choice == 2:
            contact.view_all(contacts)  
        elif choice == 3:
            contact.delete_contact(contacts)
        elif choice == 4:
            contact.find_contact(contacts)
        elif choice == 5:
            contact.edit_contact(contacts)
        else:
            print("ok byee")
            break
    except Exception as error:
        print("error occured")
    finally:
        print("program is completed" )