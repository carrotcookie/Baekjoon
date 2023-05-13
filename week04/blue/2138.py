import sys
input = sys.stdin.readline

n = int(input())
start = list(map(int, input().rstrip()))
re_start = start[:]
goal = list(map(int, input().rstrip()))

cnt = 0
for i in range(1, n):
    if start[i - 1] != goal[i - 1]:
        cnt += 1

        start[i - 1] = not start[i - 1]
        start[i] = not start[i]

        if i < n - 1:
            start[i + 1] = not start[i + 1]

else:
    if start == goal:
        print(cnt)
    else:
        re_start[0] = not re_start[0]
        re_start[1] = not re_start[1]
        cnt = 1

        for i in range(1, n):
            if re_start[i - 1] != goal[i - 1]:
                cnt += 1

                re_start[i - 1] = not re_start[i - 1]
                re_start[i] = not re_start[i]

                if i < n - 1:
                    re_start[i + 1] = not re_start[i + 1]

        else:
            if re_start == goal:
                print(cnt)
            else:
                print(-1)