import sys
sys.stdin = open('input.txt')

board = [[0]*100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        board[i][y1:y2] = [1] * (y2-y1)

area = 0
for b in board:
    area += b.count(1)

print(area)