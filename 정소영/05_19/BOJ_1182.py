from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1, n + 1):
    for combi in combinations(arr, i):
        if sum(combi) == s:
            cnt += 1

print(cnt)