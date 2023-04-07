cntList = [0 for _ in range(10)]

a = int(input())
b = int(input())
c = int(input())

result = str(a * b * c)

for ch in result:
    cntList[int(ch)] += 1

for num in cntList:
    print(num)