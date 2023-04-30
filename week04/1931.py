import sys
input = sys.stdin.readline

n = int(input())
meeting_time = []
ans = 0
tmp = 0

for _ in range(n):
    start_time, end_time = map(int, input().split())
    meeting_time.append((start_time, end_time))

meeting_time = sorted(meeting_time, key = lambda x: (x[1], x[0]))

ans += 1
tmp = meeting_time[0][1]
for time in meeting_time[1:]:
    if tmp <= time[0]:
        ans += 1
        tmp = time[1]

print(ans)