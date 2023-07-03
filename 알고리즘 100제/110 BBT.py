import sys
input = sys.stdin.readline

# def get_height(cur, depth):
#     if cur > 9:
#         return 0
#     if root[cur] == 0:
#         return 0

#     left_h = get_height(cur * 2, depth + 1)
#     right_h = get_height(cur * 2 + 1, depth + 1)
#     h = left_h if left_h > right_h else right_h

#     if depth == 1:
#         return [left_h, right_h]
    
#     return 1 + h

# root = [0] + [1,2,2,3,3,0,0,4,4]

# print(get_height(1, 1))

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isBalanced(self, root):
#         print(rootleft)