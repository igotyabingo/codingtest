def solution(price, money, count):
    ans = money - price*(count*(count+1)/2)
    return -ans if ans<0 else 0