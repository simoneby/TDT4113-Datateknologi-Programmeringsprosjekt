
globals()
from Cipher import*

class Unbreakable(Cipher):

    global alphabet
    alphabet = [chr(x) for x in range(32, 127)]

    def __init__(self):
        return

    def encode(self, text, key):
        encrypted_text = ""
        for i in range(0, len(text)):
            key = key * 3
            while len(key) < len(text):
                key = key * 2
            key = key[0:len(text)]
            num = ((ord(text[i])) % 95) - 32
            num2 = ((ord(key[i])) % 95) - 32
            encrypted_text = encrypted_text + alphabet[num + num2]
        return encrypted_text

    def decode(self, text, key):
        encrypted_text = ""
        for i in range(0, len(text)):
            key = key * 3
            while len(key) < len(text):
                key = key * 2
            key = key[0:len(text)]
            num = ((ord(text[i])) % 95) - 32
            num2 = ((ord(key[i])) % 95) - 32
            encrypted_text = encrypted_text + alphabet[num - num2]
        return encrypted_text


    def generate_keys(self):
        secret_word = input("What is the secret keyword?: ")
        return [secret_word, secret_word]

