class Letterbox:
    def __init__(self):
        # Can set this to the flag (true = show flag, false = hide flag)
        self.letter_inside = False
        self.letter = None

    # Defines function to receive a letter
    def receive_letter(self, letter):
        # Sets the flag to True
        self.letter_inside = True
        self.letter = letter

    # Defines a function to remove the letter from the letterbox
    def remove_letter(self, letter):
        # Sets the flag to False
        letter = self.letter
        # Decrypts the message
        letter.decrypt_message()
        # Sets the letter inside to False
        self.letter_inside = False
        # Returns the letter
        return letter
