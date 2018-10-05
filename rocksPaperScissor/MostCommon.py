
from Player import*
from Action import*

class MostCommon(Player):

    def __init__(self, playername):
        Player.__init__(self, playername)
        #stein, saks, papir
        self.opponent_moves = [0,0,0]

    def recieve_result(self, action):
        self.opponent_moves[action] += 1

    def choose_action(self, opponent):
        if self.opponent_moves[0] > self.opponent_moves[1] and self.opponent_moves[0] > self.opponent_moves[2]:
            return Action(2)

        elif self.opponent_moves[1] > self.opponent_moves[0] and self.opponent_moves[1] > self.opponent_moves[2]:
            return Action(0)
        else:
            return Action(1)





