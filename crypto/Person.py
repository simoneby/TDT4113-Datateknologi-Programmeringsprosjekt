
class Person:

    def __init__(self, name, cipher):
        self.name = name
        self.cipher = cipher

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def operate_cipher(self, text):
        return

