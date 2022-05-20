from itertools import combinations


N, S = map(int, (input().split()))
arr = list(map(int, input().split()))
count = 0

for i in range (1, N+1):
    for c in combinations (arr,i):
        if (sum(c) == S):
            count += 1

print(count)
