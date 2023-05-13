import sys
input = sys.stdin.readline

n = int(input())
dp = [sys.maxsize] * (n + 1)
dp[1] = 0
route = [-1, 1]

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    div3 = False
    div2 = False

    if i % 3 == 0:
        if dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            div3 = True
    if i % 2 == 0:
        if dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            div3 = False
            div2 = True
    
    if div3 == True:
        route.append(i // 3)
    elif div2 == True:
        route.append(i // 2)
    else:
        route.append(i - 1)

print(dp[-1])
print(n, end = ' ')
while n != 1:
    print(route[n], end = ' ')
    n = route[n]