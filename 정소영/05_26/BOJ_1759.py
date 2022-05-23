from itertools import combinations

l, c = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()

moum = ['a', 'e', 'i', 'o', 'u']

for combi in combinations(arr, l):
    m,j = 0, 0
    for i in range(l):
        if combi[i] in moum:
            m +=1
        else: 
            j += 1

    if m >= 1 and j >= 2: 
        print(*combi, sep='')
        