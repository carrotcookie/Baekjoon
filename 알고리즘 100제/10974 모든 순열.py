import sys
import itertools
input = sys.stdin.readline

n = int(input())
arr = [i for i in range(1, n + 1)]

for row in itertools.permutations(arr, n):
    print(*row)