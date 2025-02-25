def solution(clothes):
    # 의상 종류에 따른 카운터 딕셔너리 생성
    closet = dict()
    for i in clothes:
        if i[1] in closet:
            closet[i[1]] += 1
        else:
            closet[i[1]] = 1
    
    mul = 1
    for i in closet.values():
        mul*=(i+1)

    return mul-1