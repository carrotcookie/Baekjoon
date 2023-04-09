# 1.
# # 각 숫자마다 자리 할당
# cntList = [0 for _ in range(10)]

# a = int(input())
# b = int(input())
# c = int(input())

# result = str(a * b * c)

# # 해당 숫자자리의 카운팅
# for ch in result:
#     cntList[int(ch)] += 1

# for num in cntList:
#     print(num)

# -----------------------------------------------------------------------------------------------

# 2. count 함수
a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))

for i in range(10):
    print(result.count(str(i)))