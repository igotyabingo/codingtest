from collections import defaultdict, deque

def solution(n, roads, sources, destination):

    graph = defaultdict(list)
    for i, j in roads:
        graph[i].append(j)
        graph[j].append(i)

    visited = set([destination])

    index = dict()
    for i, source in enumerate(sources):
        index[source] = i
    
    s = len(sources)

    result = [-1 for _ in range(s)]
    count = 0

    if destination in index:
        result[index[destination]] = 0
        count += 1
    
    # edge 가중치가 모두 1로 동일하므로 BFS로 탐색한다.
    queue = deque([(destination, 0)])
    
    while queue:
        cur, l = queue.popleft()

        for node in graph[cur]:
            if node not in visited:
                queue.append((node, l+1))
                visited.add(node)
                if node in index:
                    result[index[node]] = l+1
                    count += 1
                    if count == s:
                        return result

    return result