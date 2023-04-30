# import sys

# input = sys.stdin.readline

# globals()['node'+ i]=Node(data)

# 노드 정렬
class Node:
    def __init__(self,item):
        # Node(x) 가져올때 x를 자기의 값(item으로 설정)
        self.item=item
        # 왼쪽과 오른쪽은 초기 None 선언
        self.left=None
        self.right=None

class BinaryTree():
    # BinaryTree()로 값을 지정할때 ex) BinaryTree(root,left,right)
    def __init__(self, root, left, right):
        # root를 Node(root)로 지정 self.root.item을 사용하면 root의 값 가져올 수 있음.
        self.root = Node(root)
        # left 값이 .이 아니면 왼쪽에 Node(left) 를 넣어준다.
        if left != '.':
            self.root.left = Node(left)
        # right 값이 .이 아니면 오른쪽에 Node(right) 를 넣어준다.
        if right != '.':
            self.root.right = Node(right)

    # 값을 넣어준다.
    def append1(self, parent, left, right):
        # current를 root로 지정
        self.current = self.root
        # 자식 값 확인하기 위해 설정
        stack = []
        # 부모의 오른쪽이 있다면 stack에 오른쪽 값 추가
        if self.current.right:
            stack.append(self.current.right)
        # 부모의 왼쪽이 있다면 stack에 왼쪽 값 추가
        if self.current.left:
            stack.append(self.current.left)
        
        # stack이 있으면 반복
        while stack:
            # 스택에서 pop 하고 그 값을 current에 저장
            self.current = stack.pop()
            # 뺀 값의 item(node.item)이 부모의 값과 같다면 그 노드의 left right 추가.
            if self.current.item == parent:
                if left != '.':
                    self.current.left = Node(left)
                if right != '.':
                    self.current.right = Node(right)
                # 이미 left right를 추가하였으니 다른 노드는 찾지 않고 끝.
                return
            
            # 만약 현재 노드에 오른쪽의 값이 있다면 stack에 추가하여 부모값과 같은 노드 확인
            # ex) 왼쪽 노드를 확인하고 오른쪽 노드와 왼쪽 노드 확인
            # 만약 노드를 모두 방문했는데 없으면 node를 잇지 않는다.
            if self.current.right:
                stack.append(self.current.right)
            if self.current.left:
                stack.append(self.current.left)

    def PreOrder(self, now):
        print(now.item, end='')
        if now.left:
            self.PreOrder(now.left)
        if now.right:
            self.PreOrder(now.right)

    def InOrder(self, now):
        if now.left:
            self.InOrder(now.left)
        print(now.item, end ='')
        if now.right:
            self.InOrder(now.right)

    def PostOrder(self, now):
        if now.left:
            self.PostOrder(now.left)
        if now.right:
            self.PostOrder(now.right)
        print(now.item, end ='')

tree_num = int(input())
root, left, right = input().split()
# BinaryTree 의 __init__이 동작한다.
tree = BinaryTree(root, left, right)

# 첫번째 값은 따로 두었으니 나머지는 num의 -1 수 만큼 반복
for _ in range(tree_num-1):
    parent, left, right = input().split()
    tree.append1(parent, left, right)

tree.PreOrder(tree.root)
print()
tree.InOrder(tree.root)
print()
tree.PostOrder(tree.root)
print()