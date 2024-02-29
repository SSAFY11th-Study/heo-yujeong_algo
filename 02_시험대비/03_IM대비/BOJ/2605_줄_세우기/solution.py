import sys
sys.stdin = open('input.txt')

N = int(input())
num_list = list(enumerate(list(map(int, input().split())), 1))
order = []

for i in range(N):
    if i == 0:
        order.insert(i, num_list[i][0])
    else:
        order.insert(i-num_list[i][1], num_list[i][0])

print(*order)