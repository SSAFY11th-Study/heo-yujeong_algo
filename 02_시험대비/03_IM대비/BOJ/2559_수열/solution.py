import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
ondo = list(map(int, input().split()))

max_ondo = sum(ondo[:K])
memo = sum(ondo[:K])

for i in range(N-K):
    memo = memo + ondo[i+K] - ondo[i]
    if max_ondo < memo:
        max_ondo = memo

print(max_ondo)