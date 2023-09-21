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

    def encrypt_message(self):
        # Write a message to encrypt the message
        encrypted_message = ""
        for char in self.message:
            # print(f'Character: {char}')
            char_unicode = ord(char)
            # print(f'Character Unicode: {char_unicode}')
            encrypted_unicode = char_unicode + 3
            # print(f'Shifted Unicode: {encrypted_unicode}')
            encrypted_char = chr(encrypted_unicode)
            # print(f'Encrypted Character: {encrypted_char}')
            encrypted_message += encrypted_char
            # print(f'Encrypted Message: {encrypted_message}')
        self.message = encrypted_message

    def decrypt_message(self):
        #Write a function to decrypt the message
        decrypted_message = ""
        for char in self.message:
            # print(f'Character: {char}')
            char_unicode = ord(char)
            # print(f'Character Unicode: {char_unicode}')
            decrypted_unicode = char_unicode - 3
            # print(f'Decrypted Unicode: {decrypted_unicode}')
            decrypted_char = chr(decrypted_unicode)
            # print(f'Decrypted Character: {decrypted_char}')
            decrypted_message += decrypted_char
            # print(f'Decrypted Message: {decrypted_message}')
        self.message = decrypted_message

'''# Create a letter from Alice to Bob
alice = "Alice"
bob = "Bob"
message = "Hello does this work for longer form sentences !?><:)(#$@"

letter = Letter(alice, bob, message)

# Encrypt the message
letter.encrypt_message()

# Print the encrypted message
print("Encrypted Message:", letter.message)

# Decrypt the letter
letter.decrypt_message()

# Print the decrypted letter
print("Decrypted Message:", letter.message)'''