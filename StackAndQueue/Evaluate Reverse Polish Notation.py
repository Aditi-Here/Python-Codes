def evalRPN(tokens) :
    stack = []
    operators = ['+', '-', '*', '/']
    result = 0
    for t in tokens:
        if t in operators:
            if stack:
                a = stack.pop()
                b = stack.pop()
                if t == '+':
                    result = int(a) + int(b)
                if t == '-':
                    result = int(b) - int(a)
                if t == '*':
                    result = int(b) * int(a)
                if t == '/':
                    result = int(b) / int(a)
                stack.append(result)
        else:
            stack.append(t)
    return int(stack.pop())
tokens =["18"]
a=evalRPN(tokens)
print(a)

