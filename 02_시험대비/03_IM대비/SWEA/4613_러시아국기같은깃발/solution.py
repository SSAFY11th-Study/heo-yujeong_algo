import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]

    min_cnt = N * M

    for fir_bar in range(1, N-1):
        for sec_bar in range(fir_bar+1, N):
            cnt = 0
            for i in range(fir_bar):
                for j in range(M):
                    if flag[i][j] != 'W':
                        cnt += 1
            for i in range(fir_bar, sec_bar):
                for j in range(M):
                    if flag[i][j] != 'B':
                        cnt += 1
            for i in range(sec_bar, N):
                for j in range(M):
                    if flag[i][j] != 'R':
                        cnt += 1

            if min_cnt > cnt:
                min_cnt = cnt

    print(f'#{tc} {min_cnt}')