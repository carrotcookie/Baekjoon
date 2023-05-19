import sys
input = sys.stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))
interval = []
ans = heights[-1] - heights[0]

for i in range(1, n):
    interval.append(heights[i] - heights[i - 1])

interval.sort()

for i in range(k - 1):
    ans -= interval[n - 2 - i]

print(ans)