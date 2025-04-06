from heapq import heappush, heappop, heapify

def solution(book_time):

    for i, j in enumerate(book_time):
        a, b = j
        book_time[i] = [to_minute(a), to_minute(b)+10]

    book_time.sort(key = lambda x:x[0])

    # min heap의 자료 구조 사용
    heap = [book_time[0][1]]
    heapify(heap)
    answer = 1

    for time in book_time[1:]:
        while heap and heap[0] <= time[0]:
            heappop(heap)
        heappush(heap, time[1])
        answer = max(answer, len(heap))
    
    return answer

def to_minute(time):
    h, m = time.split(':')

    return 60*int(h)+int(m)