from Action import*

class Player:

    moves = {0: 'rock', 1: 'scissor', 2: 'paper'}


    def enter_name(self, name):
        self.playername = name

    def __str__(self):
        return self.playername


    def __init__(self, name):
        self.playername = name

    def choose_action(self, opponent):
        return

    def recieve_results(self, action):
        return


