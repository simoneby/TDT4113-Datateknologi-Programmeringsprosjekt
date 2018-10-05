from Cipher import*
from crypto_utils import*
from random import randint

class Multiplier(Cipher):

    global alphabet
    alphabet = [chr(x) for x in range(32, 127)]

    def __init__(self):
        return

    def encode(self, text, key):
        encrypted_text = ""
        for i in range(0, len(text)):
            num = ((ord(text[i]) * key) % 95) - 32
            encrypted_text = encrypted_text + alphabet[num]
        return encrypted_text

    def decode(self, text, key):
        decrypted_text = ""
        for i in range(0, len(text)):
            num = ((ord(text[i]) * key) % 95) - 32
            decrypted_text = decrypted_text + alphabet[num]
        return decrypted_text

    def generate_keys(self):
        key1 = randint(1,126)
        key2 = modular_inverse(key1, 95)
        while not key2:
            key1 = randint(1, 126)
            key2 = modular_inverse(key1, 95)
        return [key1, key2]

