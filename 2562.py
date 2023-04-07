numArr = []

for _ in range(9):
    numArr.append(int(input()))

print(max(numArr), numArr.index(max(numArr)) + 1, sep = '\n')