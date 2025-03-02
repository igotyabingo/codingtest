from collections import Counter

def solution(topping):
    answer = 0
    
    total = dict(Counter(topping))
    right_size = len(total)
    left_size = set()
    
    for i in topping:
        left_size.add(i)
        if i in total:
            if total[i] == 1:
                del total[i]
                right_size -= 1
            else:
                total[i] -= 1
                
        if(len(left_size) == right_size):
            answer += 1
    return answer
        