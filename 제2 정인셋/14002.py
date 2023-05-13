import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
result = []

for i in range(1, n):
    tmp = 0

    for j in range(i):
        if a[i] > a[j]:
            tmp = max(tmp, dp[j])

    dp[i] = tmp + 1

count = max(dp)
index = dp.index(count)
tmp = a[index]
result.append(tmp)
print(count)
for i in range(index - 1, -1, -1):
    if dp[i] == count - 1 and a[i] < tmp:
        count = dp[i]
        tmp = a[i]
        result.append(tmp)

        if count == 1: break

print(*result[::-1])