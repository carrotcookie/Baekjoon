import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
ans = 0

for _ in range(n):
    coins.append(int(input()))

for coin in coins[::-1]:
    ans += k // coin
    k %= coin

print(ans)