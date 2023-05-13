import sys
input = sys.stdin.readline

# 1. 딕셔너리 이용
# def PreOrder(root):
#     if root != '.':
#         print(root, end='')
#         PreOrder(a[root][0])
#         PreOrder(a[root][1])

# def InOrder(root):
#     if root != '.':
#         InOrder(a[root][0])
#         print(root, end='')
#         InOrder(a[root][1])

# def PostOrder(root):
#     if root != '.':
#         PostOrder(a[root][0])
#         PostOrder(a[root][1])
#         print(root, end='')

# n = int(input())
# a = {}

# for _ in range(n):
#     root, left, right = sys.stdin.readline().split()
#     a[root] = [left, right]

# PreOrder('A')
# print()
# InOrder('A')
# print()
# PostOrder('A')

#########################################################################

# 2. 노트 클래스 이용
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def link(self, left, right):
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def search(self, key):
        node = self.root
        
        # 루트가 존재하지 않으면 None
        if not node:
            return None
        # 현재 노드의 키값이 찾고자 하는 키값과 일치하면 현재 노드 반환
        if key == node.key:
            return node
        
        # 루트를 제외한 모든 곳을 탐색한다
        stack = []
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

        # 모든 곳을 탐색하다 찾는 키값이 나오면 해당 노드를 반환
        while stack:
            node = stack.pop()

            if node.key == key:
                return node
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # 여기까지 오면 찾는 노드가 어디에도 없다는거임
        return None
            
    def add(self, p_key, cl_key, cr_key):
        if not self.root:
            self.root = Node(p_key)

        # cl_key와 cr_key는 p_key를 가지는 노드의 자식임
        # p_key를 가지는 노드를 반환 받음
        # cl_key를 가지는 노드를 반환 받은 노드의 left에 연결
        # cr_key를 가지는 노드를 반환 받은 노드의 right에 연결
        if cl_key != '.':
            self.search(p_key).left = Node(cl_key)
        if cr_key != '.':
            self.search(p_key).right = Node(cr_key)

    def pre_order(self, cur: Node):
        print(cur.key, end = '')
        if cur.left:
            self.pre_order(cur.left)
        if cur.right:
            self.pre_order(cur.right)

    def in_order(self, cur: Node):
        if cur.left:
            self.in_order(cur.left)
        print(cur.key, end = '')
        if cur.right:
            self.in_order(cur.right)

    def post_order(self, cur: Node):
        if cur.left:
            self.post_order(cur.left)
        if cur.right:
            self.post_order(cur.right)
        print(cur.key, end = '')


n = int(input())
bst = BST()

for i in range(n):
    p_key, cl_key, cr_key = input().split()
    bst.add(p_key, cl_key, cr_key)

bst.pre_order(bst.root)
print()
bst.in_order(bst.root)
print()
bst.post_order(bst.root)