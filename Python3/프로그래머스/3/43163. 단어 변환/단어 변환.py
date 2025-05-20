def solution(begin, target, words):
    # 1. words 리스트 내부에 target이 존재하는가?
    if target not in words: return 0
    
    # 2. words 리스트 각 원소 간의 알파벳 차이 개수 리스트에 저장 - 이 아니라, 1 차이 나는 것들만 쌍으로 저장해두면 된다. 딕셔너리 사용
    # 3. begin으로부터 1 차이나는 words 원소 중의 후보 찾기 (초기 설정)
    l, dic, queue = len(target), dict(), list()
    for word in words:
        diff = 0
        for i in range(l):
            if word[i] != begin[i]:
                diff += 1
            if diff > 1: break
        if diff == 1:
            if word == target: return 1
            queue.append([word])

        dic[word] = list()
        for candidate in words:
            diff = 0
            if word != candidate:
                for i in range(l):
                    if word[i] != candidate[i]:
                        diff += 1
                    if diff > 1: break
            if diff == 1:
                dic[word].append(candidate)
    # 4. 각 후보들로부터 가지를 뻗어나감
    # - 종료 조건: 한번 간 데 다시 가면 안된다 + 1 차이 나는 게 없을 때 (더이상 갈 곳이 없을 때)
    if not queue: return 0
    print(queue)
    while queue:
        lst = queue.pop(0)
        visited, now = lst[:-1], lst[-1]

        for i in dic[now]:
            if i not in visited:
                if i == target:
                    return len(lst)+1
                queue.append(lst+[i])
    
    return 0