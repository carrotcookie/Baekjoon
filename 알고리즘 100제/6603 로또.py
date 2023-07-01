import sys
input = sys.stdin.readline

def get_combinations(arr, n):
    result = []

    if n == 0:
        return [[]]
    
    for i, elem in enumerate(arr):
        for c in get_combinations(arr[i + 1:], n - 1):
            result.append([elem] + c)
    
    return result

while True:
    test_case = list(map(int, input().split()))

    for row in get_combinations(test_case[1:], 6):
        print(*row, sep = ' ')

    if test_case[0] == 0:
        break

    print()