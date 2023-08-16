def calPoints(operations):
    stack = []
    for o in operations:
        if o == '+':
            stack.append(stack[-1] + stack[-2])
        elif o == 'D':
            stack.append(stack[-1] + stack[-1])
        elif o == 'C':
            stack.pop()
        else:
            stack.append(int(o))
    
    return sum(stack)

print(calPoints(["5","-2","4","C","D","9","+","+"]))
    

