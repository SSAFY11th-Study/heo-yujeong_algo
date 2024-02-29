# import sys
# sys.stdin = open('input.txt')

N = int(input())

result = []
for i in range(1, N+1):
    tmp = [N]
    tmp.append(i)

    idx = 0
    while True:
        if tmp[idx] - tmp[idx + 1] >= 0:
            tmp.append(tmp[idx] - tmp[idx+1])
            idx += 1
        else:
            break

        if len(result) < len(tmp):
            result = tmp

print(len(result))
print(*result)