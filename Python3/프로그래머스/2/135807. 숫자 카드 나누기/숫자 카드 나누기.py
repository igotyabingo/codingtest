def solution(arrayA, arrayB):
    return max(processing(arrayA, arrayB), processing(arrayB, arrayA))

def getDivisor(a):
    lst = set()

    for i in range(1, int(a**0.5)+1):
        if a % i == 0:
            lst.add(i)
            lst.add(a//i)
    
    return sorted(list(lst), reverse=True)

def processing(master, slave):
    answer = 0
    a = min(master)
    lst = getDivisor(a)
    passed = []

    for l in lst: 
        val = True
        for a in master:
            if a%l != 0: 
                val= False
                break
        if val: 
            passed.append(l)

    for k in passed[:-1]:
        val = True
        for b in slave:
            if b%k == 0:
                val = False
                break
        if val:
            answer = k 
            break
    
    return answer