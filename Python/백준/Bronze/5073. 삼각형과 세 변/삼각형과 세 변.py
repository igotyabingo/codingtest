while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    
    lst = sorted([a, b, c])
    st = set(lst)
    if lst[2] >= sum(lst[:2]):
        print("Invalid")
    elif len(st) == 1:
        print("Equilateral")
    elif len(st) == 2:
        print("Isosceles")
    else:
        print("Scalene")