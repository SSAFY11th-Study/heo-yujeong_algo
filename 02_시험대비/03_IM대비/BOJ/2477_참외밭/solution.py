import sys
sys.stdin = open('input.txt')

K = int(input())
max_garo = max_sero = 0
max_garo_idx = max_sero_idx = 0
length = []
for i in range(6):
    dir, len = map(int, input().split())
    length.append(len)
    if dir == 1 or dir == 2:
        if max_sero < len:
            max_sero = len
            max_sero_idx = i
    else:
        if max_garo < len:
            max_garo = len
            max_garo_idx = i

big_area = max_garo * max_sero
small_area = abs(length[(max_garo_idx-1)%6]-length[(max_garo_idx+1)%6]) * abs(length[(max_sero_idx-1)%6]-length[(max_sero_idx+1)%6])
print((big_area-small_area) * K)