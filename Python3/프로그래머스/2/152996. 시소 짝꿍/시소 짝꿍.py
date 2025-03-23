from collections import Counter

def solution(weights):
    count = 0
    
    dic = dict(Counter(weights))
    weights = list(dic.keys())

    while(dic):
        target = weights.pop(0)
        target_num = dic[target]
        count += (target_num)*(target_num-1)//2
        del dic[target]

        for other in dic:
            if other/target in [1.5, 2.0, 4/3, 0.5, 2/3, 3/4]:
                count += target_num*(dic[other])

    return count