
class Cipher:

    def __init__(self):
        self.alphabet = [chr(x) for x in range(32, 127)]

    def encode(self, text, key):
        return

    def decode(self, text, key):
        return

    def verify(self, clear_text, key):
        return clear_text == self.decode(self.encode(clear_text, key), key)

    def generate_keys(self):
        return

