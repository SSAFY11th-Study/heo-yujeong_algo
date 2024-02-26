import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for j in range(N):
        stack = []
        for i in range(N):
            if table[i][j] == 1:
                stack.append(1)
            elif stack and table[i][j] == 2:
                cnt += 1
                stack = []

    print(f'#{tc} {cnt}')