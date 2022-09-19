import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

# 0-1 kanpsack problem 으로 전환하여 풀이
# 최대 담을 수 있는 무게(= M) 에서 가치를 최소화한 결과 구하기
n, m = map(int, input().rsplit())
memories = list(MIS())
costs = list(MIS())

tc = sum(costs)
result = sys.maxsize

# i번째 앱까지 최대 가용 비용 j로 얻을 수 있는 최대 메모리
# bottom-up
dp = [[0] * (tc) for _ in range(n)]

for i in range(n):
    for j in range(tc):
        # i번째 앱을 종료하는 cost가 최대 가용 비용 j보다 크면
        # 종료할 수 없으므로 이전 값을 가져옴.
        if costs[i] > j:
            dp[i][j] = dp[i-1][j]

        # 1. 앱을 종료시키지 않은 경우
        # 2. i번째 앱을 종료시키고 메모리를 확보하는 경우
        # 1, 2 중에서 같은 비용으로 더 많은 메모리를 확보할 수 있는 경우를 저장
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-costs[i]] + memories[i])

        if dp[i][j] >= m:
            result = min(result, j)

# 메모리 확보 불가인 경우
if result == sys.maxsize:
    print(tc)
else:
    print(result)