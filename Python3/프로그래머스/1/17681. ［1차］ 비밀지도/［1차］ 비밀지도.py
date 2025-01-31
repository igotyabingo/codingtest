def solution(n, arr1, arr2):
    answer = []
    map1 = [[False]*n for _ in range(n)]
    map2 = [[False]*n for _ in range(n)]
    
    for i, a in enumerate(arr1):
        for j in range(n-1, -1, -1):
            if a%2 == 1:
                map1[i][j] = True
            a = a // 2
            if(a == 0):
                break
    
    for i, a in enumerate(arr2):
        for j in range(n-1, -1, -1):
            if a%2 == 1:
                map2[i][j] = True
            a = a // 2
            if(a == 0): 
                break   
    
    for i in range(n):
        s = ''
        for j in range(n):
            if (map1[i][j] or map2[i][j]) is True:
                s += "#"
            else:
                s += " "
        answer.append(s)
    
    return answer