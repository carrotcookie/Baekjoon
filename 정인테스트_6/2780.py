import sys
input = sys.stdin.readline

dp = [[0] * 10 for _ in range(1001)]
a = [[7], [2, 4], [1, 3, 5], [2, 6], [1, 5, 7], [2, 4, 6, 8], [3, 5, 9], [0, 4, 8], [5, 7, 9], [6, 8]]
T = int(input())
test_lens = []

if T > 0:
    for _ in range(T):
        test_lens.append(int(input()))

    for j in range(10):
        dp[1][j] = 1

    for i in range(2, max(test_lens) + 1):
        for j in range(10):
            for k in a[j]:
                dp[i][k] += (dp[i - 1][j])

    for length in test_lens:
        print(sum(dp[length]) % 1234567)