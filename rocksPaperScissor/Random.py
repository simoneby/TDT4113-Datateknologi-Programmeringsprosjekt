import random
from Player import*
from Action import*


class Random(Player):

    def __init__(self, playername):
        Player.__init__(self, playername)

    def choose_action(self, opponent):
        return Action(random.randint(0,2))



