class Postie:
    def __init__(self, post_office):
        # Initialises the Postie with a Post Office reference
        self.post_office = post_office

    def retrieve_letter(self):
        if self.post_office.mailbox:
            # Collects the latest message from the post office
            retrieved_letters = self.post_office.mailbox
            # Clears the post office mailbox
            self.post_office.mailbox = []
            # Returns the letter
            return retrieved_letters
        else:
            print('There are no letters to deliver.')
            return None

    def deliver_letters(self):
        # Retrieve letters from the post office
        retrieved_letters = self.retrieve_letter()
        print(retrieved_letters)
        if retrieved_letters:
            for letter in retrieved_letters:
                recipient_letterbox = letter.recipient.letterbox
                # Deposits the letter into the recipient's letterbox
                recipient_letterbox.receive_letter(letter)
            return retrieved_letters

