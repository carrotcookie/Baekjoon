import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

# 1. 개선 전
# def recur(left, right):
#     if left == right:
#         print(a[left])
#         return
    
#     parent = a[left]

#     for i in range(left + 1, right + 1):
#         # 현재 parent보다 높은 값이 나오면 해당 인덱스 i부터는 우측영역에 들어감
#         if parent < a[i]:
#             recur(left + 1, i - 1)  # 좌측
#             recur(i, right)         # 우측
#             print(parent)           # 루트
#             return

#     # 우측영역이 존재 하지않는다면 parent인 a[left] 는 제외하고 뒷 영역만 실행
#     if left + 1 <= right:
#         recur(left + 1, right)  # 좌측
#         print(a[left])          # 루트

# a = []

# while True:
#     try:
#         a.append(int(sys.stdin.readline()))
#     except:
#         break

# recur(0, len(a) - 1)

########################################################################################

# 2. 개선 후
# def recur(left, right):
#     # left는 시작 인덱스
#     # right는 끝 인덱스
#     if left == right:
#         print(a[left])
#         return
    
#     parent = a[left]

#     # 좌측, 우측 영역 구분이 없을 때
#     # 따로 처리 해줘서 불필요 연산 줄임
#     if a[left] > a[right] or a[left] < a[left + 1]:
#         recur(left + 1, right)
#         print(parent)
#         return

#     # 좌측, 우측 영역 나뉠 때
#     for i in range(left + 2, right + 1):
#         # 현재 parent보다 높은 값이 나오면 해당 인덱스 i부터는 우측영역에 들어감
#         if parent < a[i]:
#             recur(left + 1, i - 1)  # 좌측
#             recur(i, right)         # 우측
#             print(parent)           # 루트
#             return
        
# a = []

# while True:
#     try:
#         a.append(int(sys.stdin.readline()))
#     except:
#         break

# recur(0, len(a) - 1)

########################################################################################

# 3. 노드 이용
class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def add(self, key):
        if not self.root:
            self.root = Node(key, None, None)
            return True
        
        node = self.root
        while True:
            if key == node.key:
                return False
            elif key < node.key:
                if not node.left:
                    node.left = Node(key, None, None)
                    return True
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = Node(key, None, None)
                    return True
                else:
                    node = node.right
    
    def post_order(self, cur_node: Node):
        if cur_node.left:
            self.post_order(cur_node.left)
        if cur_node.right:
            self.post_order(cur_node.right)
        print(cur_node.key)

bst = BST()

while True:
    try:
        n = int(input())
        bst.add(n)
    except:
        break

bst.post_order(bst.root)