def solution(cards1, cards2, goal):

    # cards1과 cards2의 인덱스 추적할 변수
    a, b = 0, 0 
    
    for i in range(len(goal)):
        if(a<len(cards1) and cards1[a] == goal[i]):
            a += 1
        elif(b<len(cards2) and cards2[b] == goal[i]):
            b += 1
        else:
            return "No"
        
    return "Yes"