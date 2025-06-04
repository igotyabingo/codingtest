from collections import deque

def to_minute(time):
    h, m = time.split(':')
    return int(h)*60+int(m)

def to_string(time):
    h, m = time // 60, time % 60
    return f"{h:02d}:{m:02d}"

def solution(n, t, m, timetable):
    timetable = deque(list(map(to_minute, sorted(timetable))))

    for i in range(n):
        bus, people = 540 + t*i, 0

        while timetable and timetable[0] <= bus and people < m:
            last = timetable.popleft()
            people += 1
        
        if i == n-1:
            if people < m:
                return to_string(bus)
            else:
                return to_string(last-1)