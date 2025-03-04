from itertools import product

def solution(numbers, target):
    # +, -로 구성된 len(numbers) 길이의 순열을 모두 구해서 모든 경우의 수를 확인한다.
    answer = 0
    
    for i in list(product([0, 1], repeat=len(numbers))):
        tmp = 0
        for j, n in enumerate(numbers):
            if(i[j] == 0):
                tmp += n
            else:
                tmp -= n
            
        if(tmp==target):
            answer += 1
    return answer