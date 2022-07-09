#dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))
print(num_list)

def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return dp(n-1) + dp(n-2) + dp(n-3)

for i in num_list:
    print(dp(i))
    
