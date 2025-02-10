import collections
def solution(X, Y):
    both = []   # 공통으로 들어있는 숫자를 모두 담을 리스트
    
    X = [i for i in str(X)]
    Y = [i for i in str(Y)]
    
    X = collections.Counter(X)
    Y = collections.Counter(Y)
    
    if(len(X) < len(Y)):
        both = check(X, Y)
    else:
        both = check(Y, X)
    
    if not both:
        return "-1"
    elif set(both) == {'0'}:
        return "0"
    else:
        both.sort(reverse=True)
        return ''.join(i for i in both)  

def check(A, B):  # A가 X, Y 중 길이가 더 작은 리스트이다.
    ans = []
    for i in A:
        if i in B:
            ans += [i for _ in range(min(A[i], B[i]))]
    return ans