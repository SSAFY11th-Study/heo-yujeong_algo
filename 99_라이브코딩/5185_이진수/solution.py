import sys
sys.stdin = open('input.txt')

hex_to_bin = {hex(num)[2:].upper(): f'{num:04b}' for num in range(16)}
# print(hex_to_bin)
hex_to_oct = {hex(num)[2:].upper(): f'{num:02o}' for num in range(16)}
# print(hex_to_oct)

T = int(input())

for tc in range(1, T+1):
    N, N_16 = input().split()
    print(f'#{tc}', end=' ')
    for char in N_16:
        print(hex_to_bin[char], end='')
    print()
    for char in N_16:
        print(hex_to_oct[char], end='')
    print()

# oct_to_bin = {oct(num)[2:].upper(): f'{num:03b}' for num in range(8)}
# print(oct_to_bin)