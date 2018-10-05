import numpy as np

class Operator:

    def __init__(self, operation, strength):
        self.operation = operation
        self.strength = strength

    def execute(self, num1, num2):
        result = self.operation(num1, num2)
        return result

    def get_strength(self):
        return self.strength








