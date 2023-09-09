import unittest
from letterbox import Letterbox
from person import Person

class TestLetterExchange(unittest.TestCase):

    def setUp(self):
        # Create letterboxes for Alice and Bob
        self.alice_letterbox = Letterbox()
        self.bob_letterbox = Letterbox()

        # Create Alice and Bob
        self.alice = Person("Alice", self.alice_letterbox)
        self.bob = Person("Bob", self.bob_letterbox)

    # Tests Alice sending Bob a letter
    def test_alice_sends_bob_letter(self):
        self.alice.write_letter(self.bob, "Hello Bob")
        # Check to see if the letter was written and sent
        self.assertTrue(self.bob.letterbox.letter_inside)

    # Tests Bob sending Alice a letter
    def test_bob_sends_alice_letter(self):
        self.bob.write_letter(self.alice, "Hi Alice")
        # Check to see if the letter was written and sent
        self.assertTrue(self.alice.letterbox.letter_inside)

    # Tests Bob reading Alice's letter and removing it from letterbox
    def test_bob_reads_letter(self):
        self.alice.write_letter(self.bob, "Hello Bob")
        # Check to see if there is a letter inside
        self.assertTrue(self.bob.letterbox.letter_inside)
        self.bob.check_letterbox()
        # Check to see if there isn't a letter inside after checking mail
        self.assertFalse(self.bob.letterbox.letter_inside)
        # Check to see if the mail has been read
        self.assertTrue(self.bob.letterbox.letter.been_read)

    # Tests Alice reading Bob's letter and removing it from letterbox
    def test_alice_reads_letter(self):
        self.bob.write_letter(self.alice, "Hello Alice")
        # Check to see if there is a letter inside
        self.assertTrue(self.alice.letterbox.letter_inside)
        self.alice.check_letterbox()
        # Check to see if there isn't a letter inside after checking mail
        self.assertFalse(self.alice.letterbox.letter_inside)
        # Check to see if the mail has been read
        self.assertTrue(self.alice.letterbox.letter.been_read)

    # Tests Alice checking an empty letterbox
    def test_alice_letterbox_is_empty(self):
        self.alice.check_letterbox()
        self.assertFalse(self.alice.letterbox.letter_inside)

    # Tests Alice checking an empty letterbox
    def test_bob_letterbox_is_empty(self):
        self.bob.check_letterbox()
        self.assertFalse(self.bob.letterbox.letter_inside)

if __name__ == '__main__':
    unittest.main()