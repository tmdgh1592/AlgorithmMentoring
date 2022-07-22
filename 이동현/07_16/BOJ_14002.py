# 틀렸습니다. ㅠㅠ
# dp[i][j] =: dp[i][j]는 dp[i]로 끝나는 가장 긴 부분 순열이다.
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
numbers =list(MIS())
temp = 0
m = 1
index = -1
max_index = -1
dp = [[0]*2 for i in range(n)]
memory = [-1] * n
for i in range(n):
    dp[i][0] = numbers[i]
dp[0][1] = 1

for i in range(1, n):
    for j in range(i):
        if dp[i][0] <= dp[j][0]:
            continue
        else:
            if temp < dp[j][1]:
                temp = dp[j][1]
                index = j
    dp[i][1] = temp + 1
    memory[i] = index
    if dp[i][1] > m:
        m = dp[i][1]
        max_index =  i
    temp = 0

print(m)

tp = []
tp.append(dp[max_index][0])
while(max_index > -1):
    if dp[memory[max_index]][0] not in tp and memory[max_index] != -1:
        tp.append(dp[memory[max_index]][0])
    max_index = memory[max_index]
tp.sort()
for i in tp:
    print(i, end = ' ')
print()