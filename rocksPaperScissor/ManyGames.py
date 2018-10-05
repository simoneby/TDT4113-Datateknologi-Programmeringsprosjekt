
from Action import*
from Random import*
from Sequential import*
from MostCommon import*
from Historian import*
import matplotlib.pyplot as plt



class ManyGames:

    def __init__ (self, player1, player2, number_of_rounds):
        self.player1 = player1
        self.player2 = player2
        self.points = [0, 0]
        self.ratio1 = []
        self.ratio0 = []
        self.winner = ""
        self.loser = ""
        self.action1 = 0
        self.action2 = 0
        self.indicator = 0
        self.number_of_rounds = number_of_rounds

    def play_one_game(self):
        self.action1 = self.player1.choose_action(self.player2)
        self.action2 = self.player2.choose_action(self.player1)

        if self.action1 == self.action2:
            self.points[0] += 0.5
            self.points[1] += 0.5


        elif self.action1 > self.action2:
            self.points[0] += 1

        elif self.action1 < self.action2:
            self.points[1] += 1

        self.player1.recieve_results(self.action2)
        self.player2.recieve_results(self.action1)

    def play_many_games(self):
        for i in range(0, self.number_of_rounds):
            self.indicator += 1
            self.play_one_game()
            self.ratio0.append(self.points[0] / self.indicator)
            self.ratio1.append(self.points[1] / self.indicator)

        if self.points[0] == self.points[1]:
            self.winner = "no one"

        elif self.points[0] < self.points[1]:
            self.winner = str(self.player1)

        else:
            self.winner = str(self.player2)

    def play_many_games_with_graphics(self):
        for i in range(0, self.number_of_rounds):
            self.indicator += 1
            self.play_one_game()
            self.ratio0.append(self.points[0] / self.indicator)
            self.ratio1.append(self.points[1] / self.indicator)

        if self.points[0] == self.points[1]:
            self.winner = "no one"

        elif self.points[0] < self.points[1]:
            self.winner = str(self.player1)
            self.loser = str(self.player2)

        else:
            self.winner = str(self.player2)
            self.loser = str(self.player1)

        info = str(self.player1) + " mot " + str(self.player2)
        plt.plot(range(0,self.number_of_rounds), self.ratio0, label = info )
        plt.legend(loc = 'upper left')
        plt.hlines(y=0.5, xmin=-0, xmax=100, linewidth=0.2, color='k')

        plt.show()








    def __str__(self):

        self.report2 = "After " + str(self.number_of_rounds) + " games, the winner is " + self.winner + "! The score was " + str(self.points[0]) + " - " + str(self.points[1]) + " to " + self.winner + " over " + self.loser

        return self.report2




sekvens = Sequential("Sekvensielt")
rand = Random("Tilfeldig")
common = MostCommon("Mest Vanlig")
hist = Historian("Historiker", 2)



game1 = ManyGames(sekvens,rand,100)  #blir ca 50/50
game1.play_many_games_with_graphics()
print(game1)

game2 = ManyGames(sekvens,hist,100)  #historiker vinner klart
game2.play_many_games_with_graphics()
print(game2)

game1 = ManyGames(common,hist,100) #historiker vinner klart
game1.play_many_games_with_graphics()
print(game1)

game1 = ManyGames(rand,hist,100) #ca 50/50 fordi historiker ser ikke noe mønster
game1.play_many_games_with_graphics()
print(game1)
