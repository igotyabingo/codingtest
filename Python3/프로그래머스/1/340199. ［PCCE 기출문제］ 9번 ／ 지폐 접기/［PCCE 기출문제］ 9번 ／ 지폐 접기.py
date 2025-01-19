def solution(wallet, bill):
    answer = 0
    
    while(min(wallet)<min(bill) or max(bill)>max(wallet)):
        a, b = max(bill), min(bill)
        bill = [a//2, b]
        answer += 1
    
    return answer