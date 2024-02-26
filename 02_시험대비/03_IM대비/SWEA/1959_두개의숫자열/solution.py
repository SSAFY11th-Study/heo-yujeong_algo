import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))

    max_hap = 0

    if N >= M:
        for i in range(N-M+1):
            hap = 0
            a = ai[i:i+M]
            for j in range(M):
                hap += (a[j] * bj[j])
            if max_hap < hap:
                max_hap = hap
    else:
        for i in range(M-N+1):
            hap = 0
            b = bj[i:i+N]
            for j in range(N):
                hap += (ai[j] * b[j])
            if max_hap < hap:
                max_hap = hap

    print(f'#{tc} {max_hap}')