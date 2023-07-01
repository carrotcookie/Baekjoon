# 10974
# import sys
# import itertools
# input = sys.stdin.readline

# n = int(input())
# arr = [i for i in range(1, n + 1)]

# for row in itertools.permutations(arr, n):
#     print(*row)

#####################################################################################################

# 조합, 순열 구현
def combinations(arr, n):
    result = []

    if n == 0:
        return [[]]
    
    for i, elem in enumerate(arr):
        for c in combinations(arr[i + 1:], n - 1):
            result.append([elem] + c)
    
    return result

def permutations(arr, n):
    result = []

    if n == 0:
        return [[]]
    
    for i, elem in enumerate(arr):
        for p in permutations(arr[:i] + arr[i + 1:], n - 1):
            result += [[elem] + p]
    
    return result

print(*combinations([1,2,3,4,5], 2), sep = '\n')
print()
print(*permutations([1,2,3,4,5], 2), sep = '\n')
print()