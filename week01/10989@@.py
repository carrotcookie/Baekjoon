# 1. 도수정렬 알고리즘
# import sys

# def counting_sort(a, max):
#     n = len(a)
#     f = [0] * (max + 1)     # 입력받을 숫자 범위만큼
#     b = [0] * n             # 입력받을 숫자 개수만큼

#     for i in range(n): 
#         # 해당 숫자를 인덱스로 f 값을 1씩 증가
#         f[a[i]] += 1
#     for i in range(1, max + 1): 
#         # f 배열의 값들을 앞에서 부터 누적
#         f[i] += f[i-1]
#     for i in range(n-1, -1, -1): 
#         # a배열의 끝에서부터의 값을 인덱스로 f 값을 찾고
#         # 값 - 1 을 인덱스로 b 배열에 a 값을 넣어줌
#         f[a[i]] -= 1
#         b[f[a[i]]] = a[i]
#     for i in range(n):
#         # 배열 복사
#         a[i] = b[i]

# n = int(input())
# a = []

# for _ in range(n):
#     a.append(int(sys.stdin.readline()))

# counting_sort(a, max(a))

# for i in a:
#     print(i)

# 2. 
import sys

n = int(input())
a = [0] * 10001         # 최대 10000까지 입력받음

for _ in range(n):
    # 해당수에 해당하는 인덱스를 증가 시켜줌
    a[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    if a[i] != 0:
        # 카운팅된 수만큼 출력
        for j in range(a[i]):
            print(i)