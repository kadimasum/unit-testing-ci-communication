class Phonebook:
    contacts = []
    id = 0

    def __init__(self, first_name:str, last_name:str, phone_number:str, email:str) -> None:
        self.first_name   = first_name
        self.last_name    = last_name
        self.phone_number = phone_number
        self.email        = email

    def save(self):
        if len(Phonebook.contacts) == 0:
            self.id = 1
            Phonebook.id = 1
        else:
            Phonebook.id += 1
            self.id = Phonebook.id
            
        self.contacts.append(self)

    def read_all_contacts():
        return Phonebook.contacts