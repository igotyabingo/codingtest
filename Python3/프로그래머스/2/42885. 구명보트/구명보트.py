def solution(people, limit):
    answer = 0
    # 몸무게를 내림차순으로 정렬하고, 더 태울 수 있는 무게를 확인하고 맨 뒤에서부터 확인한다.
    people.sort(reverse = True)
    right = len(people)-1
    
    for i, p in enumerate(people):
        if(i > right):
            return answer
            
        if(p+people[right]<=limit):
            right -= 1    
        answer += 1
                    
    return answer