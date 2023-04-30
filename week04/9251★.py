import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

n1 = len(str1)
n2 = len(str2)

dp = [0] * n1

for i in range(n2):
    cnt = 0
    for j in range(n1):
        if cnt < dp[j]:
            cnt = dp[j]
        elif str1[j] == str2[i]:
            dp[j] = cnt + 1

print(dp)
print(max(dp))