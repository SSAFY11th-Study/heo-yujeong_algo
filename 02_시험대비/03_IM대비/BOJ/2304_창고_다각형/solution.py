import sys
sys.stdin = open('input.txt')

N = int(input())
max_loc = 0
max_height = 0

height = []
for _ in range(N):
    l, h = map(int, input().split())
    height.append([l, h])
    if max_height <= h:
        max_height = h
        max_idx = l
    if max_loc < l:
        max_loc = l

building = [0] * (max_loc + 1)
for l, h in height:
    building[l] = h

area = 0
left = 0
right = 0

for i in range(max_idx+1):
    if left < building[i]:
        left = building[i]
    area += left

for i in range(max_loc, max_idx, -1):
    if right < building[i]:
        right = building[i]
    area += right

print(area)