import re

def solution(expression):
    answer = 0
    
    a = solve('*', expression)
    b1 = solve('+', a)
    b2 = last_solve('-', a)
    c1 = abs(int(last_solve('-', b1)))
    c2 = abs(int(last_solve('+', b2)))
    answer = max(answer, c1, c2)
    
    a = last_solve('-', expression)
    print(a)
    b1 = last_solve('+', a)
    print(b1)
    b2 = last_solve('*', a)
    print(b2)
    c1 = abs(int(last_solve('*', b1)))
    c2 = abs(int(last_solve('+', b2)))
    answer = max(answer, c1, c2)

    a = solve('+', expression)
    b1 = solve('*', a)
    b2 = last_solve('-', a)
    c1 = abs(int(last_solve('-', b1)))
    c2 = abs(int(last_solve('*', b2)))
    answer = max(answer, c1, c2)

    return answer

def solve(operator, expression):
    answer = expression
    pattern = r"(\d+)["+operator+"](-?\d+)"

    found = re.search(pattern, answer)
    
    while found:
        tmp = calculate(operator, found.group(1), found.group(2))
        answer = answer[:found.start()] + str(tmp) + answer[found.end():]
        found = re.search(pattern, answer)

    return answer

def last_solve(operator, expression):
    answer = expression
    pattern = r"(-?\d+)["+operator+"](-?\d+)"

    found = re.search(pattern, answer)
    while found:
        tmp = calculate(operator, found.group(1), found.group(2))
        answer = answer[:found.start()] + str(tmp) + answer[found.end():]
        found = re.search(pattern, answer)

    return answer

def calculate(operator, x, y):
    if operator == '*':
        return str(int(x)*int(y))
    elif operator == '-':
        return str(int(x)-int(y))
    else:
        return str(int(x)+int(y))