def solution(n, wires):
    answer = 1000

    for i in range(len(wires)):
        target = wires[:i]+wires[i+1:]

        all = set([j for j in range(1, n+1)])
        group = set(target[0])

        for _ in range(n):
            for w in target:
                a, b = w
                if a in group or b in group:
                    group.add(a)
                    group.add(b)

        a, b = len(all-group), len(group)
        tmp = max(a-b, b-a)
        answer = min(answer, tmp)
        # print(all-group, group, answer)

    return answer