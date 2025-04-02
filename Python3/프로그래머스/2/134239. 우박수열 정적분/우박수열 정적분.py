def solution(k, ranges):
    ubak = [k]
    answer = []

    while(k>1):
        if k%2 == 0:
            k = k//2
            ubak.append(k)
        else:
            k = k*3 +1
            ubak.append(k)

    n = len(ubak)-1

    for range in ranges:
        a, b = range
        if n+b < a: answer.append(-1.0)
        elif n+b == a: answer.append(0.0)
        else:
            answer.append((ubak[a]+2*sum(ubak[a+1:n+b])+ubak[n+b])*0.5)

    return answer