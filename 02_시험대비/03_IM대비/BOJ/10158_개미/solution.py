import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

x_change = [_ for _ in range(x, w)] + [_ for _ in range(w, -1, -1)] + [_ for _ in range(1, x)]
y_change = [_ for _ in range(y, h)] + [_ for _ in range(h, -1, -1)] + [_ for _ in range(1, y)]

print(x_change[t % (2*w)], y_change[t % (2*h)])