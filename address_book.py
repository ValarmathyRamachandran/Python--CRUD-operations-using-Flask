import os
import pickle


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return "Name:{0}\nEmail address:{1}\nPhone:{2}".format(self.name, self.email, self.phone)

    def change_name(self, name):
        self.name = name

    def change_email(self, email):
        self.email = email

    def change_phone(self, phone):
        self.phone = phone


def add_cont():
    name = input("\nType name for the number: ")
    num = input("\nType Phone number: ")
    email = input("\nEnter email address: ")
    file = open("contacts.txt", "a+")
    file.write("\nName: " + name + f"\nPhone Number: {num} " + "\nEmail: " + email)
    file.write("\n" + "- " * 10)
    print("\n\n\tAdded Successfully!\n")


def get_contact_info_from_user():
    try:
        contact_name = input("Enter contact name\n")
        contact_email = input("Enter contact email\n")
        contact_phone = input("Enter contact phone number\n")
        contact = Contact(contact_name, contact_email, contact_phone)
        return contact
    except EOFError as e:
        # print "You entered end of file. Contact not added"
        raise e
    except KeyboardInterrupt as e:
        # print "Keyboard interrupt. Contact not added"
        raise e


def display_contacts():
    address_book_file = open("address_book_file", "contacts.txt")
    is_file_empty = os.path.getsize("address_book_file") == 0
    if not is_file_empty:
        list_contacts = pickle.load(address_book_file)
        for each_contact in list_contacts:
            print
            each_contact
    else:
        print
        "No contacts in address book"
        return
    address_book_file.close()


if __name__ == "__main__":
    print("Enter 'a' to add a contact, 'b' to display contacts, "
          " 'q' to quit")
    while True:
        choice = input("Enter your choice\n")
        if choice == 'q':
            break
        elif choice == 'a':
            add_cont()
        elif choice == 'b':
            display_contacts()
        else:
            print
            "Incorrect choice. Need to enter the choice again"
