import sys
input = sys.stdin.readline

n = int(input())
curve_info = [list(map(int, input().split())) for _ in range(n)]
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

# (3, 3, 0, 1)이 들어왔다면
# (3, 3) (4, 3)찍고 -> 90도 회전 -> (3, 3) (4, 3) (4, 2) -> 