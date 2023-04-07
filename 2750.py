# 1. 내장함수
# arr = []

# for _ in range(int(input())):
#     arr.append(int(input()))

# arr.sort()

# for i in arr:
#     print(i)

# 2. Bubble Sort
# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n-1): # 길이가 n인 경우 n-1번 패스를 돈다
#         for j in range(n-1, i, -1): # 맨 끝에서부터 비교
#             if arr[j-1] > arr[j]:
#                 arr[j-1], arr[j] = arr[j], arr[j-1]

# arr = []

# for _ in range(int(input())):
#     arr.append(int(input()))

# bubble_sort(arr)

# for i in arr:
#     print(i)

# 2-1. Bubble Sort 개선: 현재 진행하는 패스의 교환횟수가 0이면 이후의 패스는 전부 생략
# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n-1): # 길이가 n인 경우 n-1번 패스를 돈다
#         exchng = 0
#         for j in range(n-1, i, -1): # 맨 끝에서부터 비교
#             if arr[j-1] > arr[j]:
#                 arr[j-1], arr[j] = arr[j], arr[j-1]
#                 exchng += 1
#         if exchng == 0:
#             break

# arr = []

# for _ in range(int(input())):
#     arr.append(int(input()))

# bubble_sort(arr)
# print(arr)

# 2-2. Bubble Sort 개선: 스캔범위 제한
# def bubble_sort(arr):
#     n = len(arr)
#     k = 0

#     ccnt = 0
#     scnt = 0

#     while k < n-1:
#         last = n-1
#         for j in range(n-1, k, -1): # 맨 끝에서부터 비교
#             ccnt += 1
#             if arr[j-1] > arr[j]:
#                 scnt += 1
#                 arr[j-1], arr[j] = arr[j], arr[j-1]
#                 last = j
#         k = last
    
#     print(f"비교를 {ccnt}번 했습니다")
#     print(f"교환을 {scnt}번 했습니다")

# arr = []

# for _ in range(int(input())):
#     arr.append(int(input()))

# bubble_sort(arr)
# print(arr)

# 3 Shaker Sort
# def shaker_sort(arr):
#     left = 0
#     right = len(arr) -1
#     last = right

#     ccnt = 0
#     scnt = 0

#     while left < right:
#         for j in range(right, left, -1):
#             ccnt += 1
#             if arr[j-1] > arr[j]:
#                 scnt += 1
#                 arr[j-1], arr[j] = arr[j], arr[j-1]
#                 last = j
#         left = last

#         for j in range(left, right):
#             ccnt += 1
#             if arr[j] > arr[j+1]:
#                 scnt += 1
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 last = j
#         right = last

#     print(f"비교를 {ccnt}번 했습니다")
#     print(f"교환을 {scnt}번 했습니다")

# arr = []

# for _ in range(int(input())):
#     arr.append(int(input()))

# shaker_sort(arr)
# print(arr)

# 4. Selection Sort
# def selection_sort(arr):
#     n = len(arr)
#     ccnt = 0
#     for i in range(n-1):
#         min = i
#         for j in range(i+1, n):
#             ccnt += 1
#             print(arr[j], arr[min])
#             if arr[j] < arr[min]:
#                 min = j
#         arr[i], arr[min] = arr[min], arr[i]

#     print(f'비교를 {(n**2-n) // 2}번 했습니다')
#     print(f"비교를 {ccnt}번 했습니다")

# arr = []

# for _ in range(int(input())):
#     arr.append(int(input()))

# selection_sort(arr)
# print(arr)

# 5. Insertion Sort
# def insertion_sort(arr):
#     n = len(arr)

#     for i in range(1, n):
#         j = i
#         temp = arr[i] # 타겟 원소
#         while j > 0 and arr[j - 1] > temp: # 타겟 원소가 처음으로 이동하거나 이웃보다 작으면 계속
#             arr[j] = arr[j-1]
#             j -= 1
#         arr[j] = temp

# arr = []

# for _ in range(int(input())):
#     arr.append(int(input()))

# insertion_sort(arr)
# print(arr)

# 6. Shell Sort
# def shell_sort(a):
#     n = len(a)
#     h = n // 2

#     while h > 0:
#         for i in range(h, n):
#             j = i - h # j는 1씩 커지는 수
#             tmp = a[i] # 1칸씩 이동하며 비교
#             while j >= 0 and a[j] > tmp:
#                 a[j+h] = a[j]
#                 j -= h
#             a[j+h] = tmp
#         h//=2

# arr = []

# for _ in range(int(input())):
#     arr.append(int(input()))

# shell_sort(arr)
# print(arr)

# 6.1 Shell Sort
# def shell_sort(a):
#     n = len(a)
#     h = n // 2

#     while h < n // 9:
#         h = h * 3 +1

#     while h > 0:
#         for i in range(h, n):
#             j = i - h # j는 1씩 커지는 수
#             tmp = a[i] # 1칸씩 이동하며 비교
#             while j >= 0 and a[j] > tmp:
#                 a[j+h] = a[j]
#                 j -= h
#             a[j+h] = tmp
#         h//=2

# arr = []

# for _ in range(int(input())):
#     arr.append(int(input()))

# shell_sort(arr)
# print(arr)

# 7. Quick Sort
# def quick_sort(a, left, right):
#     pl = left
#     pr = right
#     x = a[(left + right) // 2]

#     while pl <= pr:
#         while a[pl] < x: pl += 1 # 크거나같은 값을 만나면 멈춤
#         while a[pr] > x: pr -= 1 # 작거나같은 값을 만나면 멈춤

#         if pl <= pr: #같은 위치에 있어도 1번뿐이니 바꿔준다
#             a[pl], a[pr] = a[pr], a[pl]
#             pl += 1
#             pr -= 1
    
#     if left < pr: quick_sort(a, left, pr)
#     if pl < right: quick_sort(a, pl, right)

# arr = []

# for _ in range(int(input())):
#     arr.append(int(input()))

# quick_sort(arr, 0, len(arr)-1)
# print(arr)

# 7-1. Quick Sort
def sort3(a, idx1, idx2, idx3):
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2

def insertion_sort(a, left, right):
    for i in range(left+1, right+1):
        j = i 
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

def quick_sort(a, left, right):
    if right - left < 9:
        insertion_sort(a, left, right)
    else:
        pl = left
        pr = right
        m = sort3(a, pl, (pl+pr) // 2, pr)
        x = a[m]

        a[m], a[pr-1] = a[pr-1], a[m]
        pl += 1
        pr -= 2

        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
        
        if left < pr: quick_sort(a, left, pr)
        if pl < right: quick_sort(a, pl, right)

arr = []

for _ in range(int(input())):
    arr.append(int(input()))

quick_sort(arr, 0, len(arr)-1)
print(arr)