# import sys
# sys.stdin = open('input.txt')

N = int(input())
for _ in range(N):
    an, *alst = map(int, input().split())
    ab, *blst = map(int, input().split())

    if alst.count(4) == blst.count(4) and alst.count(3) == blst.count(3) and alst.count(2) == blst.count(2) and alst.count(1) == blst.count(1):
        print('D')
        continue
    if alst.count(4) > blst.count(4):
        print('A')
    elif alst.count(4) < blst.count(4):
        print('B')
    else:
        if alst.count(3) > blst.count(3):
            print('A')
        elif alst.count(3) < blst.count(3):
            print('B')
        else:
            if alst.count(2) > blst.count(2):
                print('A')
            elif alst.count(2) < blst.count(2):
                print('B')
            else:
                if alst.count(1) > blst.count(1):
                    print('A')
                else:
                    print('B')