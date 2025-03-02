def solution(phone_book):
    
    hashing = dict()
    for i in phone_book:
        hashing[i] = True
    
    length = set(map(len, phone_book))
    print(length)
    
    for l in length:
        for i in hashing:
            if(len(i)>l and i[:l] in hashing):
                return False
    return True