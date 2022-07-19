import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
arr = [input().rstrip() for _ in range(n)]

sum_row = 0 # 행 방향으로 더할 값 임시 저장
sum_col = 0 # 열 방향으로 더할 값 임시 저장
res = 0 # 행 방향 합의 최종 최대 값
total = 0 # 한 행의 최대 값
cnt = 0 # 10진수 단위 덧셈을 위한 변수 - 행 방향
res_col = 0 # 열 방향 합의 최종 최대 값
total_col = 0 # 한 열의 최대 값
cnt_col = 0 # 10진수 단위 덧셈을 위한 변수 - 열 방향
ma = 0 # 최종 출력해야 할 가장 큰 값 저장

#가로로 연속 1, 세로로 연속 0
for i in range(1 << (n * m)): # n, m이 각각 2, 3이라면 가능한 경우의 수는 000000 ~ 111111 까지 총 64 -> 2 ^ (2 * 3)개
    total = 0
    res = 0
    res_col = 0
    total_col = 0
    for j in range(n): # 행 방향 합의 최대값 찾음
        cnt = 0
        sum_row = 0

        for k in range(m):
            if i &(1 << k):
                a = int(arr[j][(m - 1) - k]) * (10 ** cnt)
                sum_row += a
                cnt += 1

            else:
                total += sum_row
                sum_row = 0
                cnt = 0
            if cnt == m: total += sum_row

    res = max(res, total) 

    for j in range(m): # 열 방향 합의 최대값 찾음
        cnt_col = 0
        sum_col = 0

        for k in range(n):
            pos = k * m + j
            if not (i &(1 << pos)):
                sum_col += int(arr[n - k - 1][m - j - 1]) * (10 ** cnt_col)
                cnt_col += 1

            else:
                total_col += sum_col
                sum_col = 0
                cnt_col = 0
            if cnt_col == n: total_col += sum_col

    res_col = max(res_col, total_col)
    ma = max(res + res_col, ma) # 모든 케이스의 (행 방향 최대값 + 열 방향 최대값) 중 가장 큰 값 저장

print(ma)

#틀렸습니다