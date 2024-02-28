import sys
sys.stdin = open('input.txt')

N = int(input())
paper = [[0]*100 for _ in range(100)]
area = 0

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if paper[i][j] == 0:
                area += 1
                paper[i][j] = 1

print(area)