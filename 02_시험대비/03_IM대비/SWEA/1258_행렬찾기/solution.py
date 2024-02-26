import sys
sys.stdin = open('input.txt')

def sc_right(x, y):
    for i in range(y, n):
        if arr[x][i] == 0:
            return i

def sc_down(x, y):
    for i in range(x, n):
        if arr[i][y] == 0:
            return i

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    matter = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                ni, nj = sc_down(i, j), sc_right(i, j)
                matter.append([ni-i, nj-j])
                for x in range(i, ni):
                    for y in range(j, nj):
                        arr[x][y] = 0

    sort_mat = sorted(matter, key=lambda x: (x[0]*x[1], x[0]))
    print(f'#{tc} {len(sort_mat)}', end=' ')
    for mat in sort_mat:
        print(*mat, end=' ')
    print()