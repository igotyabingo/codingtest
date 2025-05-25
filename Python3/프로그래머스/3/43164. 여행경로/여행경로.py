from collections import defaultdict

def solution(tickets):
    # DFS 사용한다.
    answer = []
    graph = defaultdict(list)

    for i, ticket in enumerate(tickets):
        a, b = ticket
        graph[a].append((b, i))
    path = [(['ICN'],[])]
    answer = []

    while path:
        target = path.pop(0)
        neighbors = graph[target[0][-1]]
        for n, i in neighbors:
            if i not in target[1]:
                if len(target[0]) == len(tickets):
                    answer.append(target[0]+[n])
                else:
                    path.append((target[0]+[n], target[1]+[i]))

    return sorted(answer)[0]