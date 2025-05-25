from collections import defaultdict

def solution(tickets):
    # 사전순으로 빠른 '한' 경로만 찾는다. 를 이용하면 간단해진다. : 오일러 경로 - Hierholzer’s Algorithm
    graph = defaultdict(list)

    for a, b in tickets:
        graph[a].append(b)
    
    for key in graph:
        graph[key].sort()
    
    path = ['ICN']
    answer = []

    while path:
        current = path[-1]

        if graph[current] != []:
            path.append(graph[current].pop(0))
        else:
            # 백트래킹의 개념: 더이상 갈곳이 없으면 마지막 원소임이 보장된다, 그 전 원소부터 다시 탐색
            answer.append(path.pop())
    
    return answer[::-1]