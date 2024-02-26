import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    V, E = map(int, input().split())
    edge = list(map(int, input().split()))
    working = [[] for _ in range(V+1)]
    order = []

    for _ in range(E):
        pre, next = edge.pop(0), edge.pop(0)
        working[next].append(pre)

    while True:
        if len(order) == V:
            break

        start_lst = []
        for i in range(1, len(working)):
            if not working[i] and i not in order:
                start_lst.append(i)

        for start in start_lst:
            order.append(start)
            for next in range(len(working)):
                if start in working[next]:
                    working[next].remove(start)

    print(f'#{tc}', *order)