import sys
input = sys.stdin.readline

n = int(input())
cars = [[] for _ in range(1001)]
answer = 0

for i in range(1, n + 1):
    v, w = map(int, input().split())
    
    if not cars[v]:
        cars[v].append([w, i])
    elif cars[v][0][0] <= w and cars[v][0][1] < i:
        cars[v][0] = [w, i]

for car in cars[1:]:
    if car:
        answer += car[0][1]

print(answer)