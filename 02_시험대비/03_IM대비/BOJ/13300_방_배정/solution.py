# import sys
# sys.stdin = open('input.txt')

N, K = map(int, input().split())
man = [0] * 6
wom = [0] * 6

for _ in range(N):
    S, Y = map(int, input().split())

    if S == 0:
        wom[Y-1] += 1
    else:
        man[Y-1] += 1

cnt = 0

for i in range(6):
    if wom[i] % K == 0:
        cnt += (wom[i] // K)
    else:
        cnt += (wom[i] // K + 1)
    if man[i] % K == 0:
        cnt += (man[i] // K)
    else:
        cnt += (man[i] // K + 1)

print(cnt)