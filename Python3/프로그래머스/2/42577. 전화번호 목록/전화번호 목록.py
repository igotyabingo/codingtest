def solution(phone_book):
    # phone_book의 각 원소 = 번호, 한 번호가 다른 번호의 '접두어'인 경우가 없는지 bool값 리턴
    
    # # 1. 모든 순서쌍 확인 (O(n**2)) / 있으면 바로 False 리턴하게 -> 효율성 테스트 통과 X
    # for i, phone in enumerate(phone_book):
    #     for target in phone_book[i+1:]:
    #         if len(phone) >= len(target) and phone[:len(target)] == target:
    #             return False
    #         if len(phone) < len(target) and target[:len(phone)] == phone:
    #             return False
    # return True
                
    # 2. 정렬 -> 앞에 원소만 확인하면 됨 -> O(n)
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        
    return True
        
    
