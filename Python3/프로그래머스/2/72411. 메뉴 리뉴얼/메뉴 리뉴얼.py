from itertools import combinations

def solution(orders, course):
    answer = []
    # Finding Frequent Itemsets Algorithm with support = 2
    
    temp = dict()
    for order in orders:
        for alp in order:
            if alp in temp:
                temp[alp] += 1
            else:
                temp[alp] = 1
    
    check_support(temp)
    char_set = set(temp.keys())

    for i in range(1, max(course)):
        to_cnt = list(combinations(char_set, i+1))
        char_set = set()
        temp_dic = dict()
        max_value, max_index = -1, []
        for c in to_cnt:
            tmp = 0
            for o in orders:
                tmp += 1
                for alp in c:
                    if alp not in o:
                        tmp -= 1
                        break
            if(tmp>1):
                string = ''
                for k in sorted(c):
                    char_set.add(k)
                    string += k
                temp_dic[string] = tmp
                if tmp > max_value:
                    max_value = tmp
                    max_index = [string]
                elif tmp == max_value:
                    max_index.append(string)
        if i+1 in course:
            answer += max_index        

    return sorted(answer)

def check_support(dic):
    to_del = list()
    for alp in dic:
        if dic[alp] < 2:
            to_del.append(alp)
    for d in to_del:
        del dic[d]