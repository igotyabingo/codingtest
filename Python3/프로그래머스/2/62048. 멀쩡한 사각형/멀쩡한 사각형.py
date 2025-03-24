def solution(w,h):
    # 정사각형인 경우와 직사각형인 경우가 다르다.
    if w == h: return w*w-w
    else:
        w, h = min(w, h), max(w, h)
        k = gcd(w, h)
        return w*h - k*(w//k+h//k-1)
    
def gcd (w,h):
    # 유클리드 알고리즘 사용
    tmp = h%w
    while(tmp != 0):
        h, w = w, tmp
        tmp = h%w
    
    return w