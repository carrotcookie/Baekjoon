import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

left, right = 0, 1
ans = sys.maxsize

while left < n and right < n:
    tmp = a[right] - a[left]

    if tmp > m:
        ans = min(ans, tmp)
        left += 1
    elif tmp < m:
        right += 1
    else:
        ans = tmp
        break

print(ans)