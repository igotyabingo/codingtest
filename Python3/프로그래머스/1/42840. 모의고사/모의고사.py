def solution(answers):
    answer = [0, 0, 0]
    ret = []
    
    # 찍는 방식 -> 주기 존재 (5, 8, 10) -> 나머지로 점수 계산
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        ans = answers[i]
        if (ans == a[i%5]):
            answer[0] += 1
        if (ans == b[i%8]):
            answer[1] += 1
        if (ans == c[i%10]):
            answer[2] += 1
    
    k = max(answer)
    if(answer[0] == k):
        ret.append(1)
    if(answer[1] == k):
        ret.append(2)
    if(answer[2] == k):
        ret.append(3)

    return ret