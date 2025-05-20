from collections import deque, defaultdict

def solution(begin, target, words):
    # 1. words 리스트 내부에 target이 존재하는가?
    if target not in words: return 0
    
    # 2. words 리스트 각 원소 간의 알파벳 차이 개수 리스트에 저장 - 이 아니라, 1 차이 나는 것들만 쌍으로 저장해두면 된다. 딕셔너리 사용
    # ******* defaultdict(list)로 dict에 새 key 삽입시 자동으로 value를 빈 list로 생성되게 함
    # ******* zip을 이용하여 알파벳 차이 한 줄로 계산

    l, graph = len(target), defaultdict(list)
    all_words = words + [begin]
    for i in range(len(all_words)):
        for j in range(i+1, len(all_words)):
            w1, w2 = all_words[i], all_words[j]
            diff = sum([1 for a, b in zip(w1, w2) if a != b])
            if diff == 1:
                graph[w1].append(w2)
                graph[w2].append(w1)

    # 3. 각 후보들로부터 가지를 뻗어나감
    # - 종료 조건: 한번 간 데 다시 가면 안된다 + 1 차이 나는 게 없을 때 (더이상 갈 곳이 없을 때)
    # ******* visited는 전체 트리에 대해 하나로만 저장하면 됨. (최단거리 보장) + 마지막 원소만 저장하면 됨
    visited, queue = set(), deque([(begin, 0)])
    
    while queue:
        word, depth = queue.popleft()
        if word == target:
            return depth
        for neighbor in graph[word]:
            if neighbor not in visited:
                queue.append((neighbor, depth+1))
                visited.add(neighbor)
    
    return 0