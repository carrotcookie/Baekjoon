# n = int(input())
# pos = [-1] * n
# count = 0

# def put(i):
#     # 위에서 아래로 두니 위쪽만 검사해줌
#     # 위쪽만 봤을때 열이 겹치거나 대각선으로 놓았으면 False
#     for j in range(i):
#         if pos[i] == pos[j] or i-j == abs(pos[i]-pos[j]):
#             return False
#     return True
         
# def set(i):
#     global count

#     if  i > n-1:
#         count += 1 # 모든행에 두는데 성공했으면 카운팅 후 리턴

#         # # 결과 그림으로 보기
#         # arr = [['□'] * n for _ in range(n)]
#         # for j in range(1, n+1):
#         #     arr[j-1][pos[j-1]] = '■'
#         # for j in range(n):
#         #     for k in range(n):
#         #         print(arr[j][k], end = ' ')
#         #     print()
#         # print()

#         return
#     else:
#         for j in range(n):
#             pos[i] = j

#             if put(i): # 두는데 성공하면
#                 set(i+1) # 다음 행 진행

# set(0) # 0행부터 출발
# print(count)

# 1.
n = int(input())
count = 0

def set(row, ld, rd):
    global count
    if row == (1 << n) - 1:
        count += 1
        return
    pos = ((1 << n) - 1) & (~(row | ld | rd))
    while pos:
        p = pos & -pos
        pos -= p
        set(row | p, (ld | p) << 1, (rd | p) >> 1)

set(0, 0, 0)
print(count)