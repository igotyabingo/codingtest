import sys
input = sys.stdin.readline

M = int(input())
count = set()

for _ in range(M):
    cmd = input().strip()
    
    if cmd == "all":
        count =  set([i for i in range(1, 21)])
    elif cmd == "empty":
        count = set()
    else:
        command, x = cmd.split()
        x = int(x)
        if command == "add":
            count.add(x)
        elif command == "remove":
            count.discard(x)
        elif command == "check":
            print(1 if x in count else 0)
        elif command == "toggle":
            if x in count: count.remove(x)
            else: count.add(x)