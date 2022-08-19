#dp[i] =: cost i 일때 최대로 확보할 수 있는 메모리
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n, m = MIS()
memory = list(MIS())
cost = list(MIS())