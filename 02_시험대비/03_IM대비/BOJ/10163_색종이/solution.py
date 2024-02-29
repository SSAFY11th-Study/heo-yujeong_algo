import sys
sys.stdin = open('input.txt')

N = int(input())
board = [[0]*1001 for _ in range(1001)]

for num in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        board[i][y:y+h] = [num] * h

cnt = [0] * (N+1)
for num in range(1, N+1):
    for b in board:
        cnt[num] += b.count(num)

print(*cnt[1:], sep='\n')