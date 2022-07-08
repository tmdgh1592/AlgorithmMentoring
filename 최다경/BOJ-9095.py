# def bf(n, cur_sum):
#     if cur_sum > n:
#         return 0
#     if cur_sum == n:
#         return 1
#     ret = 0

#     for i in range(1, 4):
#         ret += bf(n, cur_sum + i)
#     return ret

# for _ in range(int(input())):
#     print(bf(int(input())))

#dp
arr = []
for _ in range(int(input())):
    n = int(input())
    dp = [0 for _ in range(12)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    arr.append(dp[n])
    
print(*arr, sep = '\n')

