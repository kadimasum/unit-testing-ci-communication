from phonebook import Phonebook
import unittest 

class Phonebook_Test(unittest.TestCase):

    def setUp(self) -> None:
        self.person_x = Phonebook("John", "Doe", "07123345", "johndoe@gmail.com")
        self.person_y = Phonebook("Brian", "Doe", "07123345", "briandoe@gmail.com")
        self.person_z = Phonebook("Jane", "Doe", "07123345", "janedoe@gmail.com")

    def tearDown(self) -> None:
        Phonebook.contacts.clear()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.person_x, Phonebook))
    
    def test_save(self):
        self.person_x.save()
        self.assertEqual(1, len(Phonebook.contacts))
        self.assertEqual("John", Phonebook.contacts[0].first_name)
    
    def test_read_all_contacts(self):
        self.person_y.save()
        self.person_z.save()
        self.person_x.save()
        self.assertEqual(3, len(Phonebook.contacts))
        self.assertEqual("Brian", Phonebook.contacts[0].first_name)
        self.assertEqual("Jane", Phonebook.contacts[1].first_name)
        self.assertEqual("John", Phonebook.contacts[2].first_name)
        self.assertEqual(3, len(Phonebook.read_all_contacts()))

    def test_delete_contact(self):
        self.person_y.save()
        self.person_z.save()

        Phonebook.delete_contact(1)
        
        self.assertEqual(1, len(Phonebook.contacts))
        self.assertEqual(2, Phonebook.contacts[0].id)

    def test_filter_by_first_name(self):
        self.person_y.save()
        self.person_z.save()
        self.person_x.save()

        self.assertTrue(self.person_x.__dict__, Phonebook.filter_by_first_name("John"))
        self.assertTrue(self.person_y.__dict__, Phonebook.filter_by_first_name("Brian"))
        self.assertTrue(self.person_z.__dict__, Phonebook.filter_by_first_name("Jane"))


    def test_update_name(self):
        self.person_y.save()
        self.person_y.update_name(1,"Bruno", "Jackson" )
        
        self.assertEqual("Bruno", self.person_y.first_name)
        self.assertEqual("Jackson", self.person_y.last_name)

    def test_update_number(self):
        self.person_x.save()

        self.person_x.update_number(1, "0724558667")

        self.assertEqual("0724558667", self.person_x.phone_number)





if __name__ == "__main__":
    unittest.main()