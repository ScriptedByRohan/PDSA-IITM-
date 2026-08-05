#evalustion expression generllay we calculate 2+3 = 5 here operator is in the middle but for this  "2 3 + " .we are going to use the stack and push digit in the stack until a number arrives and if some operator arrives we have to pop 2 digit and so that operation on the numbers 

def evalustion_expression(exp):
    stack = []
    tokens = exp.split()
    for item in tokens:
        if item.isdigit():
            stack.append(int(item))
        else:
            b = stack.pop()  
            a = stack.pop()
            if item == '+':
                stack.append(a+b)
            elif item == '-':
                stack.append(a-b)
            elif item == '*':
                stack.append(a*b)
            elif item == '/':
                stack.append(a/b)
            elif item == '**':
                stack.append(a**b)
    return stack.pop()

print(evalustion_expression("5 3 + 2 *"))