def solution(nums):
    # 번호 = 종류
    # 전체 N마리 중 N/2마리를 가져갈 수 있다 -> N/2마리를 가져가는 것과 N/2 종류를 가져가는 것은 완전 별개임
    # 최대한 다양한 종류(리턴값)를 보장하면서 N/2마리 선택
    
    # nums에서 distinct한 원소의 개수와 n중의 min값이 리턴값이 됨
    
    return min(len(set(nums)), len(nums)//2)