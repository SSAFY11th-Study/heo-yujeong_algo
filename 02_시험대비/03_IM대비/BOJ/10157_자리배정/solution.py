# import sys
# sys.stdin = open('input.txt')

C, R = map(int, input().split())
K = int(input())
place = [[0]*R for _ in range(C)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

idx = 0
x = y = 0
num = 1
place[x][y] = num
num += 1

if K > C * R:
    print(0)
else:
    while True:
        if num > K:
            print(x + 1, y + 1)
            break
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < C and 0 <= ny < R and place[nx][ny] == 0:
            place[nx][ny] = num
            x, y = nx, ny
            num += 1
        else:
            idx = (idx + 1) % 4