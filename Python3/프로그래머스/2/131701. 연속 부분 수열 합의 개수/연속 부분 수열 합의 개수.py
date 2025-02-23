def solution(elements):
    # 길이별로 모든 합을 구해볼 수 밖에 없다. set으로 구성하여 중복을 처리함
    # 시간 복잡도: 길이가 1씩 늘어날 때마다 원소 하나씩만 추가하여 합을 계산한다.
    # 원형 수열 인덱스 처리: % 연산 이용
    s, l = set(), len(elements)
    sum = [0 for _ in range(l)] # sum[0]: 인덱스 0부터 시작한 합을 저장한다
    for k in range(l-1):
        for i in range(l):
            sum[i] += elements[(i+k)%l]
            s.add(sum[i])
            
    return len(s)+1