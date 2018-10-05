
from crypto_utils import*
from Multiplier import*
from Affine import*
from Unbreakable import*
import linecache
import mmap




global alphabet
alphabet = [chr(x) for x in range(32, 127)]

from Sender import*
from Reciever import*
from Cipher import*
from Caesar import*
from Hacker import*


#def encode(text, key):
 #   encrypted_text = ""
  #  for i in range(0, len(text)):
   #     num = ((ord(text[i]) * key) % 95) - 32
    #    encrypted_text = encrypted_text + alphabet[num]
    #return encrypted_text

key2 = modular_inverse(7, 95)

#def decode(text, key2):
#    encrypted_text = ""
#    for i in range(0, len(text)):
 #       num = ((ord(text[i]) * key2) % 95) - 32
  #      encrypted_text = encrypted_text + alphabet[num]
   # return encrypted_text

#print(key2)


#print(ord('A'))
#print(ord('Z'))

#encoded = encode("KODE", 7)

#print(encoded)

#print(decode(encoded, key2))

#p = generate_random_prime(224) #person 1 public key
#q = generate_random_prime(224) #person 2 private key
#n = p * q
#a = (p-1)*(q-1)

#modular_inverse(n, )


f = open('english_words.txt')
lines = f.readlines()
#print(lines[-1])

#frida = Reciever("frida", Caesar)
#simone = Sender("simone",  Caesar, frida)
#ragnhild = Hacker("ragnhild",  Caesar)



frida = Reciever("frida", Unbreakable)
simone = Sender("simone",  Unbreakable, frida)
ragnhild = Hacker("ragnhild",  Unbreakable)


message = "antilabor"
print("secret message: " + message)
secret_message = simone.operate_cipher(message)

hacker_try = ragnhild.brute_force(secret_message)
print("The hacker says: " + hacker_try)
decoded_message = frida.operate_cipher(secret_message)
print("the message was: " + decoded_message)


#def make_wordlist( txt_file):
#    word_list = []
#    word_count = [0] * 27
#    f = open(txt_file)
#    lines = f.readlines()
#    for i in range(1, 26):
#        count[i] = count[i] + count[i - 1]
#    for i in range(0, 109583):
#        line = lines[i].replace('\n','')
#        word_list.append(line)
#        first_letter = ord(lines[i][0])-96
#        if first_letter > -1 and first_letter < 26:
#            word_count[first_letter] += 1
#    return [word_count, word_list]



