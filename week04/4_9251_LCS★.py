import sys
input = sys.stdin.readline

# str1 = input().rstrip()
# str2 = input().rstrip()

# n1 = len(str1)
# n2 = len(str2)

# dp = [0] * n1

# for i in range(n2):
#     cnt = 0
#     for j in range(n1):
#         if cnt < dp[j]:
#             cnt = dp[j]
#         elif str1[j] == str2[i]:
#             dp[j] = cnt + 1

# print(dp)
# print(max(dp))

##############################################################################################################

# # Xi = x1x2x3x4...xi
# # Yj = y1y2y3y4...yj 일 때
# # LCS(i, j)를 Xi와 Yj의 최대 공통 부분 수열 길이라고 한다면
# # 마지막 문자가 같다면 LCS(i, j) = LCS(i-1, j-1) + 1
# # 마지막 문자가 다르면 LCS(i, j) = max(LCS(i, j-1), LCS(i-1, j)) 이다.

word1 = '0' + input().rstrip()
word2 = '0' + input().rstrip()

l1 = len(word1)
l2 = len(word2)

dp = [[0] * l1 for _ in range(l2)]

for i in range(1, l2):
    for j in range(1, l1):
        if word2[i] == word1[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[-1][-1])
for row in dp:
    print(*row)