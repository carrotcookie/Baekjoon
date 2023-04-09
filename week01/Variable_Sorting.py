# 1. 선택정렬 (Slection Sort)
# O(N^2)
def selection_sort(a):
    # .. 가장 작은 값을 찾아서 맨 앞으로 보내주자
    n = len(a)
    index = 0

    for i in range(n): # 리스트 길이만큼의 패스를 돌아야함
        min = 1000000

        for j in range(i, n):
            if min > a[j]: 
                min = a[j]
                index = j

        a[i], a[index] = a[index], a[i]

# 2. 버블정렬 (Bubble Sort)
# O(N^2)
# 하지만 선택정렬보다 느리다. 교환횟수가 많기 때문에.
def bubble_sort(a):
    # .. 옆에 있는 값과 비교해서 작은 값을 앞으로 보내자
    n = len(a)

    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1] 

# 3. 삽입정렬 (Insertion Sort)
# O(N^2) 
# O(N^2)의 복잡도를 가진 정렬 알고리즘 중에 가장 빠르다
# 거의 정렬된 상태라면 while문을 바로빠져나오기 때문에 엄청 빠르다
def insertion_sort(a):
    n = len(a)

    for i in range(1, n): # 총 n-1번 패스
        j = i

        while j > 0 and a[j-1] > a[j]: # 앞에 값이 작아질때까지 계속 바꿈
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1

# 4. 퀵정렬 (Quick Sort)
def quick_sort(a, left, right):
    pl = left
    pr = right
    pivot_val = a[(left + right) // 2]

    while pl <= pr:
        while a[pl] < pivot_val: pl += 1
        while a[pr] > pivot_val: pr -= 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: quick_sort(a, left, pr)
    if pl < right: quick_sort(a, pl, right)

# 5. 병합정렬 (Merge Sort)
def merge(a, m, middle, n):
    i = m
    j = middle + 1
    k = m

    while (i <= middle) and (j <= n):
        if a[i] <= a[j]:
            sorted[k] = a[i]
            i += 1
        else:
            sorted[k] = a[j]
            j += 1
        k += 1

    if i > middle:
        for t in range(j, n+1):
            sorted[k] = a[t]
            k += 1
    else:
        for t in range(i, middle + 1):
            sorted[k] = a[t]
            k += 1

    for t in range(m, n+1):
        a[t] = sorted[t]

def merge_sort(a, m, n):
    if m < n: # 길이가 1보다 클때만
        middle = (m + n) // 2
        merge_sort(a, m, middle)
        merge_sort(a, middle + 1, n)
        merge(a, m, middle, n)


if __name__ == '__main__':
    a = [5, 10, 3, 4, 1, 2, 7, 8, 6, 9]
    sorted = [0] * len(a)
    print(f'정렬 전: {a}')
    # selection_sort(a)
    # bubble_sort(a)
    # insertion_sort(a)
    # quick_sort(a, 0, len(a) - 1)
    merge_sort(a, 0, len(a) - 1)
    print(f'정렬 후: {a}')