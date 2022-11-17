import sys
from collections import defaultdict
from itertools import combinations
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
data = [list(MIS()) for _ in range(m)]
dic = defaultdict(list)
for i in range(m):
    dic[data[i][0]].append(data[i][1])
cnt = 0
combis = combinations(range(1, n + 1), 3)
for combi in combis:
    print(combi, combi[0], dic[combi[0]])
    if (combi[1] in dic[combi[0]]) or (combi[2] in dic[combi[0]]) or (combi[0] in dic[combi[1]]) or (combi[2] in dic[combi[1]]) or (combi[1] in dic[combi[2]]) or (combi[0] in dic[combi[2]]):
        print("continue")
        continue
    cnt += 1
print(cnt)
    