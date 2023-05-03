import sys
input = sys.stdin.readline

# dp[i]는 i번째 계단을 밟았을 때 그 때까지의 최대값

n = int(input())
a = []
dp = []

for i in range(n):
    a.append(int(input()))


if n == 1:
    dp.append(a[0])
    print(dp[-1])
elif n == 2: 
    dp.append(a[0])
    dp.append(max(a[0] + a[1], a[1]))
    print(dp[-1])
else:
    dp.append(a[0])
    dp.append(max(a[0] + a[1], a[1]))
    dp.append(max(a[0] + a[2], a[1] + a[2]))
    for i in range(3, n):
        dp.append(max(dp[i - 2] + a[i], dp[i - 3] + a[i] + a[i - 1]))
    print(dp[-1])