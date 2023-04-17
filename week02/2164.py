from collections import deque

que = deque([i for i in range(1, int(input())+1)])

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

print(que[0])
# print(*que)
# print(que.pop())