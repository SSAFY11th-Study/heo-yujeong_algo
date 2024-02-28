import sys
sys.stdin = open('input.txt')

N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
dep = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
max_hap = 0

for i in range(6):
    side_hap = []
    can = list(range(1, 7))
    under = dice[0][i]
    top = dice[0][dep[i]]
    can.remove(under)
    can.remove(top)
    side_hap.append(max(can))

    for j in range(1, N):
        can = list(range(1, 7))
        next_under = top
        next_under_idx = dice[j].index(next_under)
        top = dice[j][dep[next_under_idx]]
        can.remove(next_under)
        can.remove(top)
        side_hap.append(max(can))

    if max_hap < sum(side_hap):
        max_hap = sum(side_hap)

print(max_hap)