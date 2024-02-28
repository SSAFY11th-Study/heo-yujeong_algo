import sys
sys.stdin = open('input.txt')

garo, sero = map(int, input().split())
N = int(input())
store = [list(map(int, input().split())) for _ in range(N)]
spot = list(map(int, input().split()))

