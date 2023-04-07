t = int(input())
numList = list(map(int, input().split()))
error = 0
for num in numList:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
                break
    else:
        error += 1

print(len(numList) - error)