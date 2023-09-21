from letter import Letter


class PostOffice:
    def __init__(self):
        # Defines the Post Office's mailbox
        self.mailbox = []

    def deposit_letter(self, letter):
        # Calls the function to encrypt the message
        letter.encrypt_message()
        # Appends the encrypted message to the letterbox
        self.mailbox.append(letter)