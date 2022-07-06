from itertools import permutations

n = int(input())
arr = list(map(int,input().split()))

ans = 0

for perm in permutations(arr, n):
    res = 0
    for i in range(1, len(perm)) :
        res += abs(perm[i - 1] - perm[i])
    ans = max(ans, res)

print(ans)