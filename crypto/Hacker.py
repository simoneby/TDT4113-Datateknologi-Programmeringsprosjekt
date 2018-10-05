from Person import*
from Caesar import*
from Affine import*
from Multiplier import*
from Unbreakable import*
import linecache
import mmap


# Protip når du tester hacker, kun bruk ord på 'a' som message og key, og gjerne lange ord. Korte ord er litt
# buggy for meg.


class Hacker(Person):

    def __init__(self, name, cipher):
        self.name = name
        self.cipher = cipher


    def brute_force(self, text):
        cracked = False

        # Caesar hacking
        # Her tester jeg alle mulige nøkler for å se om det matcher et ord i ordboken
        if self.cipher == Caesar:
            for i in range(1,126):
                test_word = self.operate_cipher(text, i)
                index = open('english_words.txt', 'r').read().find(test_word)
                if (index > -1):
                    cracked = True
                    return "I hacked the code! The secret word was: " + test_word

        # Mutliplier hacking. Ganske lik som over
        if self.cipher == Multiplier:
            for i in range(1,126):
                test_word = self.operate_cipher(text, modular_inverse(i,95))
                index = open('english_words.txt', 'r').read().find(test_word)
                if (index > -1):
                    cracked = True
                    return "I hacked the code! The secret word was: " + test_word

        # Affine hacking. De to over kombinert. husk mutliplier først og så Caesar
        if self.cipher == Affine:
            for i in range(1, 126):
                for j in range(1, 126):
                    test_word2 = self.operate_cipher(text, [i, modular_inverse(j, 95)])
                    index = open('english_words.txt', 'r').read().find(test_word2)
                    if (index > -1):
                        cracked = True
                        return "I hacked the code! The secret word was: " + test_word2

         # Unbreakable hacking
        if self.cipher == Unbreakable:
            print("hacking...")
            [count, words] = self.make_wordlist('english_words.txt')
            for i in range(0, 109583):
                message = self.operate_cipher(text, words[i])
                first_letter = ord(message[0]) - 97
                for j in range(count[first_letter], count[first_letter + 1]):  #Her passer jeg på å bare sjekke ord som begynner på samme bokstav for å spare tid
                    if message == words[j]:
                        return "I hacked the code! The secret word was: " + message + " and the keyword was: " + words[i]

        if cracked == False:
            return "the secret word is not in the english dictionary"

    def make_wordlist(self, txt_file):
        word_list = []
        word_count = [0] * 27
        f = open(txt_file)
        lines = f.readlines()
        for i in range(1, 26):
            word_count[i] = word_count[i] + word_count[i-1]
        for i in range(0, 109583):
            line = lines[i].replace('\n', '')
            word_list.append(line)
            first_letter = ord(lines[i][0]) - 96
            if first_letter > -1 and first_letter < 27:
                word_count[first_letter] += 1
        return [word_count, word_list]

    def operate_cipher(self, text, key):
        return self.cipher.decode(self, text, key)

