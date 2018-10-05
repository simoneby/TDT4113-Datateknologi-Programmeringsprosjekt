
from Person import*
from Cipher import*
from Affine import*


class Sender(Person):

    def __init__(self, name, cipher, reciever):
        self.name = name
        self.cipher = cipher
        self.reciever = reciever

    def set_key(self):
        if self.cipher == Affine:
            [key1, key2, key3, key4] = self.cipher.generate_keys(self)
            self.key = [key1, key2]
            self.reciever.set_key([key3, key4])
        else:
            [key1, key2] = self.cipher.generate_keys(self)
            self.key = key1
            self.reciever.set_key(key2)

    def get_key(self):
        return self.key

    def operate_cipher(self, text):
        self.set_key()
        key = self.key
        return self.cipher.encode(self, text, key)
