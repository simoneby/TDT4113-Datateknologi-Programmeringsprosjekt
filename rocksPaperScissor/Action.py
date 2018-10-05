
class Action:

    def __init__(self, action):
        self.action = action

    def __eq__(self, other):
        return self.action == other.action

    def __gt__(self, other):
       return self.action == other.action - 1 or self.action == other.action + 2

    def __str__(self):
        wordlist = ['rocks', 'scissor','paper ']
        return wordlist[self.action]

    def getAction(self):
        return self.action


a = [1,2,3]
print(a[0:1])