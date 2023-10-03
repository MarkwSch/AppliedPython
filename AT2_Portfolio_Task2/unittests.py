import unittest
from letterbox import Letterbox
from person import Person
from postoffice import PostOffice
from postie import Postie
class TestPostalSystem(unittest.TestCase):

    def setUp(self):
        self.alice_letterbox = Letterbox()
        self.bob_letterbox = Letterbox()
        self.alice = Person("Alice", self.alice_letterbox)
        self.bob = Person("Bob", self.bob_letterbox)
        self.post_office = PostOffice()
        self.charli = Postie(self.post_office)

    def test_alice_sends_bob_letter(self):
        # Alice writes and sends a letter to Bob
        self.alice.write_letter(self.bob, self.post_office, "Hello Bob")
        # Check if the letter was sent to the post office
        self.assertTrue(self.post_office.mailbox)
        # Check to see if the message was encrypted
        self.assertNotEqual(self.post_office.mailbox[0].message, "Hello Bob")

        # Postie delivers letter
        self.charli.deliver_letters()
        # Person checks letterbox
        self.assertTrue(self.bob.letterbox.letter_inside)

        # Bob checks his letterbox and reads the message
        decrypted_message = self.bob.check_letterbox()
        # Asserts that the message has been decrypted successfully
        self.assertEqual(decrypted_message, "Hello Bob")
        # Checks that Bob has read that message and removed it
        self.assertFalse(self.bob.letterbox.letter_inside)

    def test_bob_sends_alice_letter(self):
        # Alice writes and sends a letter to Bob
        self.bob.write_letter(self.alice, self.post_office, "Hello Alice")
        # Check if the letter was sent to the post office
        self.assertTrue(self.post_office.mailbox)
        # Check to see if the message was encrypted
        self.assertNotEqual(self.post_office.mailbox[0].message, "Hello Alice")

        # Postie delivers letter
        self.charli.deliver_letters()
        # Person checks letterbox
        self.assertTrue(self.alice.letterbox.letter_inside)

        # Bob checks his letterbox and reads the message
        decrypted_message = self.alice.check_letterbox()
        # Asserts that the message has been decrypted successfully
        self.assertEqual(decrypted_message, "Hello Alice")
        # Checks that Bob has read that message and removed it
        self.assertFalse(self.alice.letterbox.letter_inside)

    # Postie attempts to deliver letter from empty post office
    def test_postie_attempts_to_deliver_from_empty_post_office(self):
        # Asserts that the Post Office mailbox is empty
        self.assertFalse(self.post_office.mailbox)
        # Postie delivers letter
        self.charli.deliver_letters()
        # Ensures that no letter has been delivered to either letterbox
        self.assertFalse(self.bob.letterbox.letter)
        self.assertFalse(self.bob.letterbox.letter_inside)
        self.assertFalse(self.alice.letterbox.letter)
        self.assertFalse(self.alice.letterbox.letter_inside)

    def test_encrypting_complicated_message(self):
        # Complicated message to be sent. I tried to use all the symbols, numbers and characters.
        message = "ABCDEFGhijklmnopqrStUvWxYz0123456789/*-+!@#$%^&*()=_|{}[]':;?/><,.`~"
        self.alice.write_letter(self.bob, self.post_office, message)
        # Check to see if the message was encrypted
        self.assertNotEqual(self.post_office.mailbox[0].message, message)

    def test_decrypting_complicated_message(self):
        # Complicated message to be sent. I tried to use all the symbols, numbers and characters.
        message = "ABCDEFGhijklmnopqrStUvWxYz0123456789/*-+!@#$%^&*()=_|{}[]':;?/><,.`~"
        self.alice.write_letter(self.bob, self.post_office, message)
        # Postie delivers letter
        self.charli.deliver_letters()
        # Bob checks his letterbox and reads the message
        decrypted_message = self.bob.check_letterbox()
        # Asserts that the message has been decrypted successfully
        self.assertEqual(decrypted_message, message)

    def test_sending_empty_message(self):
        # Empty string
        message = ''
        self.alice.write_letter(self.bob, self.post_office, message)
        # Postie delivers letter
        self.charli.deliver_letters()
        # Checks that the message has been delivered
        self.assertTrue(self.bob.letterbox.letter_inside)
        # Bob checks his letterbox and reads the message
        decrypted_message = self.bob.check_letterbox()
        # Asserts that the empty message has arrived properly
        self.assertEqual(decrypted_message, message)
        # Checks that the message has been removed from the letterbox
        self.assertFalse(self.bob.letterbox.letter_inside)


if __name__ == '__main__':
    unittest.main()