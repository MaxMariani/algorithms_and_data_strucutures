def validParenthesis(s): 
    
    p = {')' : '(', ']' : '[', '}' : '{'}

    stack = []
    for c in s:
        if c in p:
            if stack and p[c] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
            
    return True if len(stack) == 0 else False


print(validParenthesis('({{}})]'))

