import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(n)
    arrive_time[n] = 0

    while q:
        now = q.popleft()

        if now == k:
            print(arrive_time[now])
            break
        
        # 가장 빠른 시간을 구하려면 일단 0초짜리 먼저 꺼내야 된다 생각하는데
        # append로만 해도 되네? 심지어 if문을 2번째 차례로 해도?
        if 0 <= now * 2 < 100001 and arrive_time[now * 2] == -1:
            arrive_time[now * 2] = arrive_time[now]
            q.appendleft(now * 2)
        if 0 <= now - 1 < 100001 and arrive_time[now - 1] == -1:
            arrive_time[now - 1] = arrive_time[now] + 1
            q.append(now - 1)
        if 0 <= now + 1 < 100001 and arrive_time[now + 1] == -1:
            arrive_time[now + 1] = arrive_time[now] + 1
            q.append(now + 1)

n, k = map(int, input().split())
arrive_time = [-1] * 100001
bfs()