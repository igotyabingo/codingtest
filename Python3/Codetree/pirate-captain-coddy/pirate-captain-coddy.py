import heapq
from collections import defaultdict

def build_heap(boats):
    # boats to heap
    heap = []
    for id in boats.keys():
        heap.append((-boats[id][0], id))
    heapq.heapify(heap)
    return heap

def main():
    t = int(input())
    boats = dict() 
    # boats[선박 번호] = [공격력, 재장전 시간, 상태]
    # 상태: 사격 대기 = True, 재장전 = False
    heap = []
    waiters = defaultdict(list) # 재장전 중인 선박들, key는 사격 대기 상태로 전환되는 시간

    # t개의 명령이 한 줄에 하나씩 순차적으로 주어짐, 각 명령은 1시간 간격으로 실행됨
    for time in range(t):
        # 명령의 4가지 유형: '공격 준비', '지원 요청', '함포 교체', '공격 명령'
        # 반복문 실행 간격 = 1시간 ('time'시)

        if waiters[time]:
            for id in waiters[time]:
                boats[id][2] = True
            del waiters[time]

        line = input()
        if line[0] == '1':
            # 공격 준비
            lst = list(map(int, line.split()))
            n = lst[1]
            for idx in range(2, len(lst), 3):
                id, p, r = lst[idx], lst[idx+1], lst[idx+2]
                boats[id] = [p, r, True]
                heap.append((-p, id))
            heapq.heapify(heap)

        elif line[0] == '2':
            # 지원 요청
            _, id, p, r = map(int, line.split())
            boats[id] = [p, r, True]
            heapq.heappush(heap, (-p, id))

        elif line[0] == '3':
            # 함포 교체
            _, id, pw = map(int, line.split())
            boats[id][0] = pw
            # heap = build_heap(boats)
            heapq.heappush(heap, (-pw, id)) # was the key for time complexity!!!!

        elif line[0] == '4':
            # 공격 명령
            val = 0
            a, c = 0, []
            tmp = []
            while heap:
                p, id = heapq.heappop(heap)
                p = -p

                if boats[id][2] and p == boats[id][0]: # 2nd condition was the key for time complexity!!!!
                    a += p
                    r = boats[id][1]
                    val += 1
                    c.append(id)
                    boats[id][2] = False
                    waiters[time+r].append(id)
                tmp.append((-p, id))
                if val == 5:
                    break
            
            for element in tmp:
                heapq.heappush(heap, element)

            print(f"{a} {val} {' '.join(str(i) for i in c)}")

if __name__ == '__main__':
    main()