import sys
input = sys.stdin.readline

# dp[i][j]를 i부터 j까지 곱했을 때 최소 연산수라 하자
# e.g. dp[A][D] -> ABCD를 했을 때 최소 연산수
# e.g. dp[A][C] -> ABC를 했을 때 최소 연산수
# e.g. dp[A][B] -> AB를 했을 때 최소 연산수 -> AB는 그냥 곱한경우 1가지 밖에 없기 때문에 자체로 최소 연산수임
# e.g. dp[A][A] -> 0 이라고 하자

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
dp = [[sys.maxsize] * n for _ in range(n)]

for i in range(n):
    for j in range(n - i):
        x = j
        y = i + j

        if x == y:
            dp[x][y] = 0
        elif y - x == 1:
            dp[x][y] = info[x][0] * info[x][1] * info[y][1]
        else:
            for k in range(x, y):
                # info[k][1] -> info[k + 1][0] 으로 바꿔도 됨
                dp[x][y] = min(dp[x][y], dp[x][k] + dp[k + 1][y] + info[x][0] * info[k][1] * info[y][1])

print(dp[0][-1])

##########################################################################
# import sys 

# num = int(input())

# p = [None] * (num+1)

# for i in range(1, num): 
#     r, c = map(int, input().split())
#     p[i-1] = r
# else : 
#     r, c = map(int, input().split())
#     p[-2] = r
#     p[-1] = c

# # print(p)

# def matrix_chain_order(n, p):
#     # n = p.length -1
#     m = [[None] * (n+1) for _ in range(n+1)]
#     # s = [[None] * (n+1) for _ in range(n+1)]

#     for idx in range(1,n+1):
#         m[idx][idx] = 0

#     for length in range (2, n+1):
#         for i in range(1,n-length+2):
#             j = i+length-1
#             m[i][j] = sys.maxsize
#             for k in range(i,j) :
#                 q = m[i][k] + m[k+1][j] + (p[i-1] * p[k] * p[j])
#                 if q < m[i][j] :
#                     m[i][j] = q
#                     # s[i][j] = k

#     # print(m)
#     # print(s)
#     print(m[1][n])

# matrix_chain_order(num, p)