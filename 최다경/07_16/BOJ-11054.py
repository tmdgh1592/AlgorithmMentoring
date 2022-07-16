#dp[i] := A[i]를 끝으로 하는 가장 긴 증가하는 수열의 길이
#dp2[i] :=  A[i]를 시작으로 하는 가장 긴 감소하는 수열의 길이
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
A = list(MIS())
B = A.copy()
B.reverse()
dp = [1 for _ in range(n)]
dp2 = [1 for _ in range(n)]
dp[0] = 1
dp2[0] = 1
sum = 0
for i in range(n):
    for j in range(i):
        if A[j] < A[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
 #증가하는 가장 긴 수열       
for i in range(n):
    for j in range(i):
        if B[j] < B[i] and dp2[i] < dp2[j] + 1:
            dp2[i] = dp2[j] + 1
#감소하는 가장 긴 수열
dp2.reverse()
for i in range(1, len(dp)):#위에서 구한 두 수열을 인덱스에 따라 합친 뒤 가장 긴 바이토닉 수열을 찾음
    a = dp[i] + dp2[i]
    b = dp[i - 1] + dp2[i - 1]
    sum = max(a, b, sum)
#즉 앞에서부터 증가하는 가장 긴 수열과 뒤에서 부터 증가하는 가장 긴 수열을 합치고 -1 해줌
if len(A) == 1:
    print(1)
else:
    print(sum - 1)


