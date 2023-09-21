
class Postie:
    def __init__(self, post_office):
        # Initialises the Postie with a Post Office reference
        self.post_office = post_office

    def retrieve_letter(self):
        # Collects the latest message from the post office
        retrieved_letter = self.post_office.mailbox
        # Clears the post office mailbox
        self.post_office.mailbox = []
        # Returns the letter
        return retrieved_letter

    def deliver_letters(self, retrieved_letter):
        """Pretty pointless feature right now but basically checks to make sure it is the correct
        letterbox before depositing the letter."""
        recipient_letterbox = retrieved_letter.recipient.letterbox
        if recipient_letterbox == retrieved_letter.recipient.letterbox:
            # Deposits the letter into the recipient's letterbox
            retrieved_letter.recipient.letterbox.receive_letter(retrieved_letter)

