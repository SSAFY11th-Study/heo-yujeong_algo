import sys
sys.stdin = open('input.txt')

garo, sero = map(int, input().split())
N = int(input())
store = [list(map(int, input().split())) for _ in range(N)]
spot = list(map(int, input().split()))

hap = 0
for i in range(N):
    if spot[0] == 1:
        if store[i][0] == 1:
            hap += abs(spot[1] - store[i][1])
        elif store[i][0] == 2:
            hap += min(spot[1]+store[i][1]+sero, garo-spot[1]+sero+garo-store[i][1])
        elif store[i][0] == 3:
            hap += (spot[1] + store[i][1])
        else:
            hap += (garo-spot[1] + store[i][1])
    elif spot[0] == 2:
        if store[i][0] == 1:
            hap += min(spot[1]+sero+store[i][1], garo-spot[1]+sero+garo-store[i][1])
        elif store[i][0] == 2:
            hap += abs(spot[1] - store[i][1])
        elif store[i][0] == 3:
            hap += (spot[1] + sero-store[i][1])
        else:
            hap += (garo-spot[1] + sero-store[i][1])
    elif spot[0] == 3:
        if store[i][0] == 1:
            hap += (spot[1] + store[i][1])
        elif store[i][0] == 2:
            hap += (sero-spot[1] + store[i][1])
        elif store[i][0] == 3:
            hap += abs(spot[1] - store[i][1])
        else:
            hap += min(spot[1]+garo+store[i][1], sero-spot[1]+garo+sero-store[i][1])
    else:
        if store[i][0] == 1:
            hap += (spot[1] + garo-store[i][1])
        elif store[i][0] == 2:
            hap += (sero-spot[1] + garo-store[i][1])
        elif store[i][0] == 3:
            hap += min(sero-spot[1]+garo+sero-store[i][1], spot[1]+garo+store[i][1])
        else:
            hap += abs(spot[1] - store[i][1])

print(hap)