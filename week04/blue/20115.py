import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(float, input().split()))
a = deque(sorted(a))

while n > 1:
    tmp = a.popleft()
    a[-1] += tmp / 2
    n -= 1

print(a[0])