
from Function import*
from Operator import*
from Queue import*
import numbers
from Stack import*
import re


class Calculator:

    def __init__(self):

        self.functions = {'EXP':  Function(np.exp),
                          'LOG':  Function(np.log),
                          'SIN':  Function(np.sin),
                          'COS':  Function(np.cos),
                          'SQRT': Function(np.sqrt),
                          'NEG': Function(np.negative)}

        self.operators = {'ADD': Operator(np.add, 0),
                          'MULT': Operator(np.multiply, 1),
                          'DIVIDE': Operator(np.divide, 1),
                          'SUBTRACT': Operator(np.subtract, 0)}
        self.output_queue = Queue()

    def calculate_RPN(self):
        stack = Stack()
        while self.output_queue.size() > 0:
            element = self.output_queue.pop()

            if isinstance(element, numbers.Number):
                stack.push(element)

            elif isinstance(element, Function):
                a = stack.pop()
                stack.push(element.execute(a))

            elif isinstance(element, Operator):
                a = stack.pop()
                b = stack.pop()
                stack.push(element.execute(b, a))

        return stack.pop()


    def normal_to_RPN(self, input_queue):
        operator_stack = Stack()
        while input_queue.size() > 0:
            element = input_queue.pop()

            if isinstance(element, numbers.Number):
                self.output_queue.push(element)

            elif isinstance(element, Function):
                operator_stack.push(element)

            elif element == '(':
                operator_stack.push(element)

            elif element == ')':
                while isinstance(operator_stack.peek(), Function) or isinstance(operator_stack.peek(), Operator):
                    self.output_queue.push(operator_stack.pop())
                operator_stack.pop()


            elif isinstance(element, Operator):
                if operator_stack.size() > 0:
                    a = operator_stack.peek()
                    while isinstance(a, Function) or (isinstance(a, Operator) and a.get_strength() >= element.get_strength()) and a != '(':
                        self.output_queue.push(operator_stack.pop())
                        if operator_stack.size() == 0:
                            break
                        a = operator_stack.peek()

                operator_stack.push(element)

        while operator_stack.size() > 0:
            self.output_queue.push(operator_stack.pop())

        return self.output_queue

    def text_parser(self, text):
        output_queue = Queue()
        text = re.split('([^a-zA-Z0-9])', text)
        operator_dict = {"+": self.operators['ADD'],
                         "-": self.operators['SUBTRACT'],
                         "*": self.operators['MULT'],
                         "/": self.operators["DIVIDE"],
                         "exp": self.functions['EXP'],
                         "log": self.functions['LOG'],
                         "sin": self.functions['SIN'],
                         "cos": self.functions['COS'],
                         "sqrt": self.functions['SQRT'],
                         "neg": self.functions['NEG']}

        operators = ["+", "-", "*", "/", "exp", "log", "sin", "cos", "sqrt", "neg"]

        for element in text:
            if element in operators:
                if isinstance(operator_dict[element], Operator) or isinstance(operator_dict[element], Function):
                    output_queue.push(operator_dict[element])

            elif element.isdigit():
                if isinstance(float(element), numbers.Number):
                    output_queue.push(float(element))

            elif element == '(' or element == ')':
                output_queue.push(element)


        return output_queue






