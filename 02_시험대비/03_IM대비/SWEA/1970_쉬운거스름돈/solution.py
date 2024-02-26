import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    chan_cnt = [0] * len(units)

    for i in range(len(units)):
        chan_cnt[i] = N // units[i]
        N %= units[i]

    print(f'#{tc}')
    print(*chan_cnt)