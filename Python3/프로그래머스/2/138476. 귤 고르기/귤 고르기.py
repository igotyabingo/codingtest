import collections

def solution(k, tangerine):
    ans, c = 0, 0
    # counter 객체 생성 -> 카운트 기준 내림차순 정렬
    dic = dict(collections.Counter(tangerine))
    sorted_dic = sorted(dic, key=lambda x: dic[x], reverse=True)

    for i in sorted_dic:
        c += dic[i]
        ans += 1
        if(c >= k):
            return ans

# sorted(cnt.values(), reverse = True) 를 통해 value 기준으로 정렬하고 정렬된 value값만 리스트로 뽑아낼 수 있다.
