import sys
sys.stdin = open('input.txt')

# 백트래킹 함수
def backtrack(line, hap): # 인자 : 몇번째 라인을 조사하는지, 현재 합
    # 최소합을 저장할 변수
    global min_hap
    # 마지막 라인까지 선택이 끝나면
    if line == N:
        # 최소합과 현재 합계 비교 후 작은 값으로 최소합 결정
        if min_hap > hap:
            min_hap = hap
    # 마지막 줄까지 보지 않았지만 최소합보다 현재 합이 커질 경우 종료
    # 더이상 보지 않습니다
    elif hap > min_hap:
        return
    # 아직 마지막 줄까지 보지 않고, 현재합이 최소합보다 크지 않을때
    else:
        # 한 줄에 있는 N개의 요소 중
        for i in range(N):
            # 아직 선택되지 않은 줄의 요소를 하나 선택해서
            if not line_chk[i]:
                # 현재 줄에 요소가 이용중임을 표시하고
                line_chk[i] = 1
                # 합계에 더해서 다음 줄을 조사하러 감!
                backtrack(line+1, hap+arr[line][i])
                # 끝까지 조사한 후 현재 줄의 해당 요소 이용 체크를 해제한 후
                # 다음 요소를 포함하여 재조사
                line_chk[i] = 0

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 배열 크기
    N = int(input())
    # N * N 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최소합 초기화(N개의 줄에 10보다 작은수 입력 => 보다 큰 수로 초기화)
    min_hap = N * 10
    # 한 줄에 한개씩 포함되는지 체크하는 배열
    line_chk = [0] * N

    # 백트래킹으로 최소합이 되는 조합 찾음
    backtrack(0, 0)

    # 출력
    print(f'#{tc} {min_hap}')