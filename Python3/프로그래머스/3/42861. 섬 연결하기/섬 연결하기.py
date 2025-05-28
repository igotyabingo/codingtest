# Kruskal 알고리즘 문제이다: Finding Minimum Spanning Tree
def solution(n, costs):
    answer = 0
    count = 0 # 선택한 노드수가 n-1개가 될 때까지 반복해야 한다.

    # 비용이 작은 다리부터 선택한다.
    costs.sort(key = lambda x:x[2])

    # class = 노드 번호, merge 할 때는 더 작은 것으로 합친다.
    classes = dict()
    for i in range(n):
        classes[i] = i
    
    # union, find
    for x, y, cost in costs:
        root_x = find(classes, x)
        root_y = find(classes, y)
        if root_x != root_y:
            classes[root_x] = root_y
            answer += cost
            count += 1
        if count == n-1:
            return answer
    
    return -1

def find(classes, i):
    if classes[i] != i:
        classes[i] = find(classes, classes[i])
    return classes[i]