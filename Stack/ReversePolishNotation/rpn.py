op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y }

def calculate_rpn(expression):
    stack = []
    expression = expression.split()         #O(n)
    for o in expression:                  #O(n)
        if o.isdigit():
            stack.append(float(o))          #O(1)
        elif o in op:
            a = stack.pop()                 #O(1)
            b = stack.pop()                 #O(1)
            stack.append(op[o](a, b))       #O(1)
        else:
            raise ValueError("Invalid value: " + o)

    return stack.pop()                      #O(1)

expression = "4 5 + 3 *"
result = calculate_rpn(expression)

print("Result:", result)
