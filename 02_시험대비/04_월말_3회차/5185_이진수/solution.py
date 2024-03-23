import sys
sys.stdin = open("input.txt")

hex_to_bin = {hex(idx)[2:].upper(): f'{idx:04b}' for idx in range(16)}

T = int(input())

for tc in range(1, T+1):
    N, hex = input().split()
    print(f'#{tc}', end=' ')
    for txt in hex:
        print(hex_to_bin[txt], end='')
    print()