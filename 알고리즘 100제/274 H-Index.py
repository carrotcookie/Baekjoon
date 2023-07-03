import sys
import bisect
input = sys.stdin.readline

def find_correct_index(a, x):
    left, right = 0, len(a) - 1
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if a[mid] >= x:
            right = mid - 1
            result = mid
        else:
            left = mid + 1
            result = mid + 1

    return result

citations = list(map(int, input().split()))
citations.sort()
length = len(citations)
answer = 0

for i in range(1001):
    pos = find_correct_index(citations, i)
    
    if length - pos >= i:
        answer = i

print(answer)