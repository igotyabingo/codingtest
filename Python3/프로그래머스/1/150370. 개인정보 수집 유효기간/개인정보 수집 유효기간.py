def solution(today, terms, privacies):
    answer = []
    
    # 1. terms의 약관별 유효기간을 dictionary로 정리한다.
    dic = {}
    for t in terms:
        x, y = t.split()
        dic[x] = int(y)
        
    # 2. privacies를 순회하며 각 정보에 대해 파기유무를 판단한다.
    for i, p in enumerate(privacies):
        x, y = p.split()
        if calculate(x, dic[y]) <= today:
            answer.append(i+1)
        
    return answer

# 날짜를 계산하는 함수: date 기준으로 +month달
def calculate(date, month):
    y, m, d = date.split('.')
    # day는 그대로
    
    y = int(y)
    m = int(m) + month
    if(m>12):
        if(m%12 == 0):
          y += m//12 -1
          m = 12
        else: 
          y += m//12
          m = m%12
    
    if(m<10):
        m = '0' + str(m)
    print(f'{y}.{m}.{d}')

    return f'{y}.{m}.{d}'