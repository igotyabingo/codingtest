def solution(nums):
    # nums의 distinct한 종류 개수가 N/2보다 클 경우 N/2를 리턴,
    # 그렇지 않을 경우 distinct한 종류 개수를 리턴
    
    # distinct = 'set'

    return min(len(nums)//2, len(set(nums)))