import sys
sys.stdin = open('input.txt')

def select(cnt, hap):
    global min_hap
    if hap >= B:
        min_hap = min(min_hap, hap)
        return
    if cnt == N:
        return
    select(cnt+1, hap+Hi[cnt])
    select(cnt+1, hap)


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    Hi = list(map(int, input().split()))

    min_hap = sum(Hi)
    select(0, 0)

    print(f'#{tc} {abs(min_hap-B)}')