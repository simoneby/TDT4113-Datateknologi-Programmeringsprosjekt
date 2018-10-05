
from Action import*

from Sequential import*
from Random import*

class SingleGame:

    def __init__ (self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.points = [0,0]
        self.winner = ""
        self.action1 = 0
        self.action2 = 0

    def play_game(self):
        self.action1 = self.player1.choose_action(self.player2)
        self.action2 = self.player2.choose_action(self.player1)

        if self.action1 == self.action2:
            self.points = [0.5, 0.5]
            self.winner = "its a tie!"

        elif self.action1 > self.action2:
            self.points = [1,0]
            self.winner = str(self.player1) + ' is the winner'

        elif self.action1 < self.action2:
            self.points = [0, 1]
            self.winner = str(self.player2) + ' is the winner'

        self.player1.recieve_results(self.player2, self.action2)
        self.player2.recieve_results(self.player1, self.action1)

    def __str__(self):
        self.report = str(self.player1) + ": " + str(self.action1) + "\n" + str(self.player2) + ": " + str(self.action2) + "\n" + str(self.winner) +"\n"
        return self.report


a = Random("Frida")
b = Sequential("Simone")

spill = SingleGame(a,b)
spill.play_game()
print(spill)


d = Random("Frida")
b = Sequential("Simone")

spill = SingleGame(a,b)
spill.play_game()
print(spill)


c = Random("Frida")
b = Sequential("Simone")

spill = SingleGame(a,b)
spill.play_game()
print(spill)
