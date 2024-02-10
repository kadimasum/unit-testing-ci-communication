from phonebook import Phonebook
import unittest 

class Phonebook_Test(unittest.TestCase):

    def setUp(self) -> None:
        self.person_x = Phonebook("John", "Doe", "07123345", "johndoe@gmail.com")

    def tearDown(self) -> None:
        Phonebook.contacts.clear()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.person_x, Phonebook))
    
    def test_save(self):
        self.person_x.save()
        self.assertEqual(1, len(Phonebook.contacts))
        self.assertEqual("John", Phonebook.contacts[0].first_name)
    
    def test_read_all_contacts(self):
        self.person_y = Phonebook("Brian", "Doe", "07123345", "briandoe@gmail.com")
        self.person_z = Phonebook("Jane", "Doe", "07123345", "janedoe@gmail.com")
        self.person_y.save()
        self.person_z.save()
        self.person_x.save()
        self.assertEqual(3, len(Phonebook.contacts))
        self.assertEqual("Brian", Phonebook.contacts[0].first_name)
        self.assertEqual("Jane", Phonebook.contacts[1].first_name)
        self.assertEqual("John", Phonebook.contacts[2].first_name)
        self.assertEqual(3, len(Phonebook.read_all_contacts()))






if __name__ == "__main__":
    unittest.main()