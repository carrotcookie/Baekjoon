import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = []

    for _ in range(n):
        score1, score2 = map(int, input().split())
        heapq.heappush(arr, (score1, score2))
    
    pivot = arr[0][1]
    ans = 1

    while arr:
        score1, score2 = heapq.heappop(arr)

        if score2 < pivot:
            ans += 1
            pivot = score2
    
    print(ans)