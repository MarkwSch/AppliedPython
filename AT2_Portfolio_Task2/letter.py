class Letter:
    # Initialises the letter message, sender, recipient and the status of the message (defaults to not read)
    def __init__(self, sender, recipient, message):
        self.sender = sender
        self.recipient = recipient
        self.message = message
        self.been_read = False

    # Function to change the letter to read status.
    def read_message(self):
        print('Message has been read.')
        self.been_read = True