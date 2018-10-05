from Queue import*
from Container import*
from Calculator import*

# Tester koden

kø = Queue()
kø.push(5)
kø.push(2)
print(kø)


calc = Calculator()

print(calc.normal_to_RPN(calc.text_parser("neg exp (1 - (neg 2))")).get_items())

print("answer is: " + str(calc.calculate_RPN()))

