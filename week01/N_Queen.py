n = int(input())
flag_a = [0] * n
flag_b = [0] * (2 * n - 1)
flag_c = [0] * (2 * n - 1)
count = 0

def recursive(i):
    global count

    if i == n:
        count += 1
        return

    for j in range(n // 2 if i == 0 else n):
        if not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + n - 1]:
            flag_a[j] = flag_b[i + j] = flag_c[i - j + n - 1] = 1
            recursive(i + 1)
            flag_a[j] = flag_b[i + j] = flag_c[i - j + n - 1] = 0

# 가장 첫번째 열 둘때 행을 절반만 시행하기 때문에 2배
recursive(0)
count *= 2

# 홀수면 첫번째 열 둘때 중간 행을 시행하지 않았기 때문에
# 첫번째열 중간 행에 두었다 하고 다음 열부터 시행
if n % 2 != 0:
    flag_a[n // 2] = flag_b[n // 2] = flag_c[n // 2] = 1
    recursive(1)

print(count)

##############################################################################################

# n = int(input())
# flag_a = [0] * n
# flag_b = [0] * (2 * n - 1)
# flag_c = [0] * (2 * n - 1)
# count = 0

# now = []
# next = [(0, 0)]

# if n == 0:
#     print(0)
#     exit()

# while next or now:
#     if len(next) != 0:
#         i, j = next.pop()
#     else:
#         i, j = now.pop()
#         flag_a[j - 1] = flag_b[i + j - 1] = flag_c[i - j + n] = 0

#     if i == n:
#         count += 1
#         continue

#     for k in range(j, n): # j열부터 끝까지 순회
#         if not flag_a[k] and not flag_b[i + k] and not flag_c[i - k + n - 1]:
#             flag_a[k] = flag_b[i + k] = flag_c[i - k + n - 1] = 1
#             next.append((i + 1, 0))  # 다음 행을 스택에 추가
#             now.append((i, k + 1))  # 다음 열을 스택에 추가
#             break
        
# print(count)

#########################################################################################

# n = int(input())
# pos = [-1] * n
# count = 0
# i = j = 0

# def check(i, j):
#     for x in range(i - 1, -1, -1):
#         if pos[x] == j or abs(j - pos[x]) == i - x:
#             return False
#     return True

# if n == 0:
#     print(0)
#     exit()
# if n == 1:
#     print(1)
#     exit()


# while i >= 0:
#     if check(i, j):
#         pos[i] = j
#         j = 0
#         i += 1
#         if i < n: continue
#     else:
#         j += 1
#         if j < n: continue

#     if i >= n:
#         count += 1
#         i -= 1
#         j = pos[i] + 1
#     while j >= n:
#         i -= 1
#         j = pos[i] + 1

# print(count)