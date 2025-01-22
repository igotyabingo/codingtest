def solution(absolutes, signs):
    sum = 0
    for i, j in enumerate(absolutes):
        if signs[i]: 
            sum += j
        else:
            sum -= j
    return sum