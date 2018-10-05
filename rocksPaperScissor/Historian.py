from Player import*
from Action import*
from statistics import mode
import random

class Historian(Player):

    def __init__(self, playername, memory):
        Player.__init__(self, playername)
        self.opponent_moves = []
        self.memory = memory #memory er en Int
        self.next_move = []

    def recieve_results(self, action):
        self.opponent_moves.append(action)

    def choose_action(self, opponent):
        if len(self.opponent_moves) + 1 <= self.memory:
            hold = random.randint(0,2)
            return Action(hold)
        else:
            sequence = self.opponent_moves[-self.memory:]
            for i in range(0, len(self.opponent_moves)-self.memory):
                if sequence == self.opponent_moves[i:i+self.memory]:
                    self.next_move.append(self.opponent_moves[i+self.memory])

            if self.next_move == []:
                hold = random.randint(0, 2)
                return Action(hold)

            else:
                action = str(max(self.next_move, key = self.next_move.count))
                self.next_move = []
                if action == "scissor":
                    return Action(2)
                elif action == "rock":
                    return Action(1)
                else:
                    return Action(0)

