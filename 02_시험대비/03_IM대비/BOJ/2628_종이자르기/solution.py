import sys
sys.stdin = open('input.txt')

garo, sero = map(int, input().split())
N = int(input())
garo_cut = [0, garo]
sero_cut = [0, sero]
for _ in range(N):
    dir, spot = map(int, input().split())
    if dir == 0:
        sero_cut.append(spot)
    else:
        garo_cut.append(spot)

garo_cut.sort()
sero_cut.sort()

garo_len = []
sero_len = []

for i in range(len(garo_cut)-1):
    garo_len.append(garo_cut[i+1]-garo_cut[i])
for i in range(len(sero_cut)-1):
    sero_len.append(sero_cut[i+1]-sero_cut[i])

area = []
for i in range(len(garo_len)):
    for j in range(len(sero_len)):
        area.append(garo_len[i] * sero_len[j])

print(max(area))