def solution(phone_book):
    # 사전순 정렬하면 바로 옆 번호만 확인하면 됨
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True