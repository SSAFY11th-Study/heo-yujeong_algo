import sys
sys.stdin = open('input.txt')

N = int(input())
switch = [None] + list(map(int, input().split()))
M = int(input())

for _ in range(M):
    gen, num = map(int, input().split())

    if gen == 1:
        for i in range(num, len(switch), num):
            switch[i] = 1 - switch[i]

    else:
        switch[num] = 1 - switch[num]
        idx = 1
        while True:
            if num - idx < 1 or num + idx > N:
                break
            if switch[num-idx] == switch[num+idx]:
                switch[num-idx] = 1 - switch[num-idx]
                switch[num+idx] = 1 - switch[num+idx]
                idx += 1
            else:
                break

for i in range(1, len(switch)):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()