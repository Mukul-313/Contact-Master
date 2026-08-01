class Contactbook:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}"


class Contactmanager:
    def __init__(self, filename="contacts.txt"):
        self.Contactlist = []
        self.filename = filename
        self.Loadcontacts()

    def Addcontact(self, contact):
        self.Contactlist.append(contact)
        self.Savecontact(contact)

    def Savecontact(self, contact):
        # Append single contact to file (comma-separated line)
        with open(self.filename, "a") as f:
            f.write(f"{contact.name},{contact.phone_number},{contact.email}\n")

    def Loadcontacts(self):
        # Load all contacts from file at startup, if it exists
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        name, phone, email = line.split(",", 2)
                        self.Contactlist.append(Contactbook(name, phone, email))
        except FileNotFoundError:
            pass  # No file yet, start fresh

    def Rewritefile(self):
        # Rewrite entire file to reflect current contact list (used after delete)
        with open(self.filename, "w") as f:
            for contact in self.Contactlist:
                f.write(f"{contact.name},{contact.phone_number},{contact.email}\n")

    def Deletecontact(self, name):
        self.Contactlist = [contact for contact in self.Contactlist if contact.name != name]
        self.Rewritefile()

    def Searchcontact(self, name):
        for contact in self.Contactlist:
            if contact.name == name:
                return contact
        return None

    def Displaycontacts(self):
        for contact in self.Contactlist:
            print(contact)


if __name__ == "__main__":
    manage = Contactmanager()

    while True:
        print("\n**** Contact Book Manager ****")
        print("0 for Exit")
        print("1 for Add Contact")
        print("2 for Delete Contact")
        print("3 for Search Contact")
        print("4 for Display Contact List")
        x = input("Choose your Option: ")

        if x == '0':
            break
        elif x == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            manage.Addcontact(Contactbook(name, phone, email))
            print("Contact Added Successfully")
        elif x == '2':
            name = input("Enter name to delete: ")
            manage.Deletecontact(name)
            print("Contact Deleted Successfully")
        elif x == '3':
            name = input("Enter name to search: ")
            contact = manage.Searchcontact(name)
            if contact:
                print("Contact Found:")
                print(contact)
            else:
                print("Contact Not Found")
        elif x == '4':
            print("Contact List:")
            manage.Displaycontacts()
        else:
            print("Invalid Option, please try again.")