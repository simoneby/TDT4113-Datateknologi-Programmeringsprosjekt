import numpy as np
import numbers

class Function:
    def __init__(self, func):
        self.func = func

    def execute(self, element, debug=True):
         #   if not isinstance(self.func, Function):
         #   raise TypeError("Cannot execute func if func is not a Function")

        if not isinstance(element, numbers.Number):
            raise TypeError("Cannot execute func if element is not a number")
        result = self.func(element)

        if debug is True:
            #print("Function: " + self.func.__name__ + "({:f}) = {:f}".format(element, result))
            return result

    def get_strength(self):
        return 0


