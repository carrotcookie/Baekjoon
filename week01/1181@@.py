import sys

# # 1. 버블정렬 이용
# def bubble_sort(a):
#     n = len(a)

#     for i in range(n-1): # 길이가 n인 경우 n-1번 패스를 돈다
#         for j in range(n-1, i, -1): # 맨 끝에서부터 비교
#             if len(a[j-1]) > len(a[j]):
#                 a[j-1], a[j] = a[j], a[j-1]
#             elif len(a[j-1]) == len(a[j]) and a[j-1] > a[j]:
#                 a[j-1], a[j] = a[j], a[j-1]

# n = int(input())
# a = []

# for _ in range(n):
#     a.append(sys.stdin.readline().rstrip())

# a = list(set(a))
# bubble_sort(a)

# for str in a:
#     print(str)

# 2. 내장함수 이용
# n = int(input())
# a = []

# for _ in range(n):
#     tmp = sys.stdin.readline().rstrip()
#     a.append((tmp, len(tmp)))



# # 1순위 길이정렬, 2순위 사전순정렬
# a.sort(key = lambda x: (x[1], x[0]))

# # 처음거는 일단 띄워주고 이후에 중복 있으면 안띄움
# print(a[0][0])
# for i in range(1, n):
#     if a[i][0] == a[i-1][0]:
#         continue
#     print(a[i][0])

# 3. 삽입정렬
def insertion_sort1(a):
    n = len(a)

    for i in range(1, n): # 총 n-1번 패스
        j = i

        while j > 0 and len(a[j-1]) > len(a[j]): # 앞에 값이 작아질때까지 계속 바꿈
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1

def insertion_sort2(a):
    n = len(a)

    for i in range(1, n): # 총 n-1번 패스
        j = i

        while j > 0 and a[j-1] > a[j]: # 앞에 값이 작아질때까지 계속 바꿈
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1

n = int(input())
a = []

for _ in range(n):
    a.append(sys.stdin.readline().rstrip())

a = list(set(a))

insertion_sort2(a)
insertion_sort1(a)

for str in a:
    print(str)