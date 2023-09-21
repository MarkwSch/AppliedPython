from postoffice import PostOffice
from letter import Letter
class Person:
    def __init__(self, name, letterbox):
        self.name = name
        self.letterbox = letterbox
        self.waiting = False
        self.received_letters = []

    # Function to write and send a letter
    def write_letter(self, recipient, message):
        if not self.waiting:
            # Creates a new instance of the letter class
            new_letter = Letter(self, recipient, message)
            # Places the letter in the recipient's letterbox
            # recipient.letterbox.receive_letter(new_letter)
            # Deposit letter in the Post Office
            PostOffice().deposit_letter(new_letter)
            # Sets waiting status to True
            self.waiting = True

    # Function to receive letter
    def receive_letter(self, letter):
        # Appends the letter to a list
        self.received_letters.append(letter)
        # Prints out the letter to the console
        print(f"Dear {self.name}, \n {letter.message} \n From {letter.sender.name}")
        # Removes the letter from the list
        self.received_letters.remove(letter)
        # Sets waiting to False (Can reply to message now)
        self.waiting = False

    # Function to check person's letterbox
    def check_letterbox(self):
        # If there is a letter inside the letterbox do the following. If not, do nothing.
        if self.letterbox.letter_inside:
            print("There's a letter inside.")
            # Sets received_letter variable as the letter removed from the letterbox
            received_letter = self.letterbox.remove_letter(self.letterbox.letter)
            # Calls the receive_letter function on the letter
            self.receive_letter(received_letter)
            # Reads the letter
            received_letter.read_message()
        else:
            print('There is no new mail.')