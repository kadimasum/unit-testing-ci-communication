class Phonebook:

    contacts = []

    def __init__(self, first_name:str, last_name:str, phone_number:str, email:str) -> None:
        self.first_name   = first_name
        self.last_name    = last_name
        self.phone_number = phone_number
        self.email        = email

    def save(self):
        if len(Phonebook.contacts) != 0:
            self.id = len(Phonebook.contacts) + 1
        else:
            self.id = 1
        Phonebook.contacts.append(self)
         

    def read_all_contacts():
        return Phonebook.contacts
    

    def delete_contact(id: int):
        for contact in Phonebook.contacts:
            if contact.id == id:
                del Phonebook.contacts[id - 1]
    
    def filter_by_first_name(name: str):
        for contact in Phonebook.contacts:
            if contact.first_name == name:
                return contact.__dict__
            
    def update_name(self, id: int, new_first_name: str, new_last_name: str):
        for contact in Phonebook.contacts:
            if contact.id == id:
                contact.first_name = new_first_name
                contact.last_name = new_last_name

    def update_number(self, id: int, new_number: str):
        for contact in Phonebook.contacts:
            if contact.id == id:
                contact.phone_number = new_number
