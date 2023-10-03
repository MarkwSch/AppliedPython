from postoffice import PostOffice
from letter import Letter


class Person:
    def __init__(self, name, letterbox):
        self.name = name
        self.letterbox = letterbox
        self.waiting = False
        self.received_letters = []

    # Function to write and send a letter
    def write_letter(self, recipient, post_office, message):
        if not self.waiting:
            # Encrypt the message
            encrypted_message = self.encrypt_message(message)
            # Creates a new instance of the letter class
            new_letter = Letter(self, recipient, encrypted_message)
            print(new_letter.message)
            # Places the letter in the recipient's letterbox
            # recipient.letterbox.receive_letter(new_letter)
            # Deposit letter in the Post Office
            post_office.deposit_letter(new_letter)
            # Sets waiting status to True
            self.waiting = True

    # Function to receive letter
    def receive_letter(self, letter):
        # Appends the letter to a list
        self.received_letters.append(letter)
        decrypted_message = self.decrypt_message(letter.message)
        # Prints out the letter to the console
        print(f"Dear {self.name}, \n {decrypted_message} \n From {letter.sender.name}")
        # Removes the letter from the list
        self.received_letters.remove(letter)
        # Sets waiting to False (Can reply to message now)
        self.waiting = False
        # Returns the decrypted message for unit testing purposes.
        return decrypted_message

    # Function to check person's letterbox
    def check_letterbox(self):
        # If there is a letter inside the letterbox do the following. If not, do nothing.
        if self.letterbox.letter_inside:
            print("There's a letter inside.")
            # Sets received_letter variable as the letter removed from the letterbox
            received_letter = self.letterbox.remove_letter(self.letterbox.letter)
            # Calls the receive_letter function on the letter
            decrypted_message = self.receive_letter(received_letter)
            # Reads the letter
            received_letter.read_message()
            return decrypted_message
        else:
            print('There is no new mail.')
            return
    def encrypt_message(self, message):
        # Write a message to encrypt the message
        encrypted_message = ""
        for char in message:
            # print(f'Character: {char}')
            char_unicode = ord(char)
            # print(f'Character Unicode: {char_unicode}')
            encrypted_unicode = char_unicode + 3
            # print(f'Shifted Unicode: {encrypted_unicode}')
            encrypted_char = chr(encrypted_unicode)
            # print(f'Encrypted Character: {encrypted_char}')
            encrypted_message += encrypted_char
            # print(f'Encrypted Message: {encrypted_message}')
        return encrypted_message

    def decrypt_message(self, message):
        # Write a function to decrypt the message
        decrypted_message = ""
        for char in message:
            # print(f'Character: {char}')
            char_unicode = ord(char)
            # print(f'Character Unicode: {char_unicode}')
            decrypted_unicode = char_unicode - 3
            # print(f'Decrypted Unicode: {decrypted_unicode}')
            decrypted_char = chr(decrypted_unicode)
            # print(f'Decrypted Character: {decrypted_char}')
            decrypted_message += decrypted_char
            # print(f'Decrypted Message: {decrypted_message}')
        return decrypted_message
