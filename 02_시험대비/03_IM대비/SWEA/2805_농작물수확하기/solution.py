import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    prof = 0

    for i in range(N//2+1):
        for j in range(N//2-i, N//2+i+1):
            prof += farm[i][j] + farm[N-i-1][j]

    prof -= sum(farm[N//2])

    print(f'#{tc} {prof}')