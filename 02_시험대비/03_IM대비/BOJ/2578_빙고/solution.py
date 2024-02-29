import sys
sys.stdin = open('input.txt')

def isBingo():
    board_t = list(map(list, zip(*board)))
    cnt = 0
    for b in board:
        if sum(b) == 0:
            cnt += 1
    for b in board_t:
        if sum(b) == 0:
            cnt += 1
    diag1 = 0
    diag2 = 0
    for i in range(5):
        if board[i][i] == 0:
            diag1 += 1
        if board[i][4-i] == 0:
            diag2 += 1
    if diag1 == 5:
        cnt += 1
    if diag2 == 5:
        cnt += 1

    if cnt >= 3:
        return True
    return False


board = [list(map(int, input().split())) for _ in range(5)]
spoke = []
for _ in range(5):
    spoke.extend(list(map(int, input().split())))

flag = False
for cnt, num in enumerate(spoke, 1):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = 0
                if isBingo():
                    flag = True
                    print(cnt)
                    break
        if flag:
            break
    if flag:
        break