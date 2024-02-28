import sys
sys.stdin = open('input.txt')

from itertools import combinations

height = [int(input()) for _ in range(9)]
comb = combinations(height, 7)

for lst in comb:
    if sum(lst) == 100:
        print(*sorted(lst), sep='\n')
        break