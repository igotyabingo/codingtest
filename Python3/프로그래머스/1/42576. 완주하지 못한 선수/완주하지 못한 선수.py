def solution(participant, completion):
    answer = ''
    
    # 시간복잡도를 위해 hash를 사용한다.
    dic = {}
    dic2 = {}

    # 리스트 간의 차집합: 단순하게 set으로 처리하면 동명이인이 사라지는 문제
    # 완주하지 못한 사람이 동명이인 중에 있는 경우: len(set(participant)) = len(set(completion))
    # 완주하지 못한 사람이 동명이인 중에 없는 경우: len(set(participant)) = len(set(completion)+1) : 그냥 차집합 바로 수행하면 된다.
    if(len(set(participant)) == len(set(completion))+1):
        return list(set(participant)-set(completion))[0]
    else:
        for i in participant:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        for i in completion:
            if i in dic2:
                dic2[i] += 1
            else:
                dic2[i] = 1
        
        for i in participant:
            if dic[i] != dic2[i]:
                return i

'''
카운터 객체(원소와 원소의 등장횟수를 쉽게 셀 수 있다)를 생성하여 간결하게 코드를 작성할 수 있다.
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''
