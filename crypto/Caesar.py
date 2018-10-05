
globals()
from random import randint
from Cipher import*

class Caesar(Cipher):

    global alphabet
    alphabet = [chr(x) for x in range(32, 127)]

    def __init__(self):
        return

    def encode(self,  text, key):
        encrypted_text = ""
        for i in range(0, len(text)):
            num = ((ord(text[i]) + key) % 95) - 32
            encrypted_text = encrypted_text + alphabet[num]
        return encrypted_text

    def decode(self,  text, key):
        decrypted_text = ""
        for i in range(0, len(text)):
            num = ((ord(text[i]) - key) % 95) - 32
            decrypted_text = decrypted_text + alphabet[num]
        return decrypted_text

    def generate_keys(self):
        a = randint(1, 126)
        return [a, a]

