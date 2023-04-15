# 1.
# import sys

# n = int(input())
# arr = list(map(int, sys.stdin.readline().split()))
# arr.sort()

# pl, pr = 0, n - 1
# tmp = sys.maxsize
# result = [0, 0]

# while pl < pr:
#     sum = arr[pl] + arr[pr]

#     if abs(sum) < tmp:
#         tmp = abs(sum)
#         result[0], result[1] = arr[pl], arr[pr]

#     if sum < 0:
#         pl += 1
#     else:
#         pr -= 1

# print(result[0], result[1])

##########################################################################################################################'

# 2.
import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

pl, pr = 0, n - 1
i1 = i2 =0
tmp = sys.maxsize

if arr[0] >= 0:
    print(arr[0], arr[1])
    exit()
if arr[-1] <= 0:
    print(arr[-2], arr[-1])
    exit()

while pl < pr:
    sum = arr[pl] + arr[pr]

    if sum == 0:
        print(arr[pl], arr[pr])
        break

    if sum < 0:
        if -sum < tmp:
            i1, i2, tmp = pl, pr, -sum
        pl += 1
    else:
        if sum < tmp:
            i1, i2, tmp = pl, pr, sum
        pr -= 1

print(arr[i1], arr[i2])