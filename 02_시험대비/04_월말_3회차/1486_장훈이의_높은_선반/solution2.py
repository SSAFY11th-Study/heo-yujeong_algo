import sys
sys.stdin = open('input.txt')
from itertools import combinations

T = int(input())

for test_case in range(1, T+1):
    N, B = map(int, input().split())
    Hi = list(map(int, input().split()))

    min_height = max(Hi)

    for i in range(1, N+1):
        comb = list(combinations(Hi, i))
        for j in range(len(comb)):
            hap = sum(comb[j])
            if hap >= B:
                min_height = min(min_height, abs(hap-B))

    print(f'#{test_case} {min_height}')