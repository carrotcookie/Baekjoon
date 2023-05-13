import sys
input = sys.stdin.readline

n = int(input())
a = [0] + [int(input()) for _ in range(n)]
ans = 0

a = sorted(a)

for i in range(1, n + 1):
    ans += abs(i - a[i])

print(ans)