# 1. 선택정렬 (Slection Sort)
# O(N^2)
def selection_sort(a):
    n = len(a)

    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[j], a[min] = a[min], a[j]

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

    for i in range(1, n): # n-1번 패스를 돌지만 1번 인덱스부터 시작한다
        j = i # 현재 인덱스저장
        tmp = a[i] # 현재값 미리 저장
        while j > 0 and a[j - 1] > tmp: # 미리 저장한 현재값보다 앞에 값이 크면
            a[j] = a[j-1] # 앞에 값을 가져옴
            j -= 1
        a[j] = tmp # 끝나면 적절한 위치에 넣어줌


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
def merge_sort(a, left, right):

    def _merge_sort(a, left, mid, right):
        i = left
        j = mid + 1
        k = left

        while i <= mid and j <= right:
            if a[i] < a[j]:
                sorted[k] = a[i]
                i += 1
            else:
                sorted[k] = a[j]
                j += 1
            k += 1

        if i > mid:
            for t in range(j, right + 1):
                sorted[k] = a[t]
                k += 1
        else:
            for t in range(i, mid + 1):
                sorted[k] = a[t]
                k += 1

        for t in range(left, right + 1):
            a[t] = sorted[t]

    if left < right:
        sorted = [0] * n
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid + 1, right)
        _merge_sort(a, left, mid, right)

# 6. 힙정렬 (Heap Sort)
def heap_sort(a):
    
    def down_heap(a, start, end):
        temp = a[start]
        parent = start

        while parent < (end + 1) // 2:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= end and a[cr] > a[cl] else cl

            if temp >= a[child]:
                break

            a[parent] = a[child]
            parent = child

        a[parent] = temp

    n = len(a)

    for i in range((n-1) // 2, -1, -1):
        down_heap(a, i, n - 1)

    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i - 1)

def counting_sort(a):
    def fsort(a, max):
        n = len(a)
        f = [0] * (max + 1)
        b = [0] * n

        for i in range(n): f[a[i]] += 1
        for i in range(1, max + 1): f[i] += f[i-1]
        for i in range(n-1, -1, -1): f[a[i]] -= 1; b[f[a[i]]] = a[i]
        for i in range(n): a[i] = b[i]

    fsort(a, max(a))

if __name__ == '__main__':
    n = 10
    a = [5, 10, 3, 4, 1, 2, 7, 8, 6, 9]
    sorted = [0] * len(a)
    print(f'정렬 전: {a}')
    # selection_sort(a)
    # bubble_sort(a)
    # insertion_sort(a)
    # quick_sort(a, 0, len(a) - 1)
    # merge_sort(a, 0, len(a) - 1)
    # heap_sort(a)
    # counting_sort(a)
    print(f'정렬 후: {a}')