import sys
input = sys.stdin.readline

# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.bottom = None

# class BST:
#     def __init__(self):
#         self.root = None
#         self.count = 0

#     def search(self, key):
#         node = self.root
        
#         # 루트가 존재하지 않으면 None
#         if not node:
#             return None
#         # 현재 노드의 키값이 찾고자 하는 키값과 일치하면 현재 노드 반환
#         if key == node.key:
#             return node
        
#         # 루트를 제외한 모든 곳을 탐색한다
#         stack = []
#         if node.bottom:
#             stack.append(node.bottom)

#         # 모든 곳을 탐색하다 찾는 키값이 나오면 해당 노드를 반환
#         while stack:
#             node = stack.pop()

#             if node.key == key:
#                 return node
            
#             if node.bottom:
#                 stack.append(node.bottom)

#         return None
                
            
#     def add(self, key1, key2):
#         global bst_lst

#         if not self.root:
#             self.root = Node(key1)
#             self.search(key1).bottom = Node(key2)
#             self.count += 2
#             return True

#         node1 = self.search(key1)
#         node2 = self.search(key2)

#         if node1 and node2:
#             return True

#         if node1:
#             while node1:
#                 if node1.bottom:
#                     node1 = node1.bottom
#                 else:
#                     break
#             node1.bottom = Node(key2)
#             self.count += 1
#             return True

#         if node2:
#             while node2:
#                 if node2.bottom:
#                     node2 = node2.bottom
#                 else:
#                     break
#             node2.bottom = Node(key1)
#             self.count += 1
#             return True
        
#         return False

# n = int(input())
# m = int(input())
# bst_lst = [BST()]

# for i in range(m):
#     a, b = map(int, input().split())
#     complete = False

#     for bst in bst_lst:
#         if bst.add(a, b):
#             complete = True
#             break

#     if not complete:
#         new_bst = BST()
#         new_bst.add(a, b)
#         bst_lst.append(new_bst)
        
# for bst in bst_lst:
#     node = bst.search(1)

#     if node:
#         print(bst.count - 1)
#         break

#####################################################################################################################

# 1. 크루스칼

# def find_root(p, x):
#     def find_parent(p, x):
#         if p[x] != x:
#             p[x] = find_parent(p, p[x])
#         return p[x]
    
#     return find_parent(p, x)

# def union_parent(p, a, b):
#     a = find_root(p, a)
#     b = find_root(p, b)

#     if a < b:
#         p[b] = a
#     else:
#         p[a] = b

# n = int(input())
# m = int(input())
# p = [i for i in range(n + 1)]

# # 연결된 노드를 같은 루트로 묶어줌
# for _ in range(m):
#     a, b = map(int, input().split())
#     union_parent(p, a, b)

# # 갱신 안된 부분 때문에 1사이클 돌리는게 낭비인듯...
# for i in range(1, n + 1):
#     find_root(p, i)

# print(p[1:].count(p[1]) - 1)

#####################################################################################################################

# 2. dfs

def dfs(cur):
    global count 
    visit[cur] = 1

    for i in range(1, n + 1):
        if not visit[i] and graph[cur][i]:
            count += 1
            dfs(i)


n, m = int(input()), int(input())
visit = [0] * 101
graph = [[0] * (n + 1) for _ in range(n + 1)]
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(1)
print(count)