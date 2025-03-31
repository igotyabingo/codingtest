def solution(cards):
    dic = dict()
    lst = []

    for i in range(len(cards)):
        dic[i+1] = cards[i]

    for i in range(len(cards)):
        if dic[i+1]: 
            if dic[i+1] == i+1:
                lst.append(1)
            else:
                count = 1
                value = dic[i+1]
                dic[i+1] = False
                while(True):
                    if dic[value] == i+1:
                        count +=1 
                        dic[value] = False
                        break
                    else:
                        tmp = value
                        value = dic[value]
                        dic[tmp] = False
                        count += 1
                        
                lst.append(count)

    if len(lst) == 1: return 0
    else:
        lst.sort(reverse=True)
        return lst[0]*lst[1]