
from Cipher import*
from Caesar import*
from Multiplier import*

class Affine(Cipher):
    global alphabet
    alphabet = [chr(x) for x in range(32, 127)]

    def __init__(self):
        return

    # Metodene encode og decode var orginalt mye mer elegante,
    # men fikk "self" problemer med å bruke klassene Caesar og Multiplier

    def encode(self, text, key):
        # Multiplier encryption
        encrypted_text1 = ""
        for i in range(0, len(text)):
            num = ((ord(text[i]) * key[1]) % 95) - 32
            encrypted_text1 = encrypted_text1 + alphabet[num]

        # Caesar encryption
        encrypted_text2 = ""
        for i in range(0, len(text)):
            num = ((ord(encrypted_text1[i]) + key[0]) % 95) - 32
            encrypted_text2 = encrypted_text2 + alphabet[num]
        return encrypted_text2

    def decode(self, text, key):
        # Caesar decryption
        decrypted_text1 = ""
        for i in range(0, len(text)):
            num = ((ord(text[i]) - key[0]) % 95) - 32
            decrypted_text1 = decrypted_text1 + alphabet[num]

        # Multiplier decryption
        decrypted_text2 = ""
        for i in range(0, len(text)):
            num = ((ord(decrypted_text1[i]) * key[1]) % 95) - 32
            decrypted_text2 = decrypted_text2 + alphabet[num]
        return decrypted_text2


    def set_keys(self):
        c_key = Caesar.generate_keys(self)
        m_key = Multiplier.generate_keys(self)
        return [c_key[0],  m_key[0], c_key[1], m_key[1]]

    def generate_keys(self):
        return self.cipher.set_keys(self)





