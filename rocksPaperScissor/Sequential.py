

from Action import*
from Random import*

class Sequential(Player):

    def __init__(self, playername):
        Player.__init__(self, playername)
        self.a = 0

    def choose_action(self, opponent):
        action = Action(self.a%3)
        self.a += 1
        return action




