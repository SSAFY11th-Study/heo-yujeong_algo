import sys
sys.stdin = open('input.txt')

# 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    # N * M
    N, M = map(int, input().split())
    # 행렬을 받아용
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우 조사할 델타
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 꽃가루의 합 최대값 저장할 변수 초기화
    max_pang = 0

    # 모든 행과 열을 순회하면서
    for i in range(N):
        for j in range(M):
            # 풍선이 터지는 곳의 값으로 꽃가루 초기화
            pang = arr[i][j]
            # 4방향을 조사!
            for k in range(4):
                # 1~풍선이 터지는 곳의 값까지 더해줌
                for l in range(1, arr[i][j]+1):
                    nx = i + dx[k]*l
                    ny = j + dy[k]*l
                    # 범위내에 있으면 더하고 아니면 pass
                    if 0 <= nx < N and 0 <= ny < M:
                        pang += arr[nx][ny]
            # 현재 꽃가루 합계가 최대값보다 크다면 값을 바꿔줌
            if max_pang < pang:
                max_pang = pang

    # 출력할게용
    print(f'#{tc} {max_pang}')