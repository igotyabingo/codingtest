def solution(brown, yellow):
    # yellow 직사각형이 a*b 크기일 때 [a+2, b+2]를 리턴해야 하고
    # 2*(a+b) +4 = brown 격자 수
    # 사실 이차방정식의 해를 구하면 바로 나온다.
    # yellow를 두 수의 곱으로 나타낼 수 있는 것을 하나하나 brown 수 조건을 확인하면서 
    
    for i in range(1, int(yellow**(1/2))+1):
        if(yellow%i == 0):
            if(2*(yellow//i + i)+4 == brown):
                return [yellow//i +2, i+2]