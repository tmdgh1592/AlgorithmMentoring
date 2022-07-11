num, total = map(int, input().split())
list1 = list(map(int, input().split()))
entry = 0 
tmp_sum = 0
cnt = 0
def permutation(arr, n, m, entry):
    global tmp_sum, cnt
    tmp_sum = 0
    if len(arr) == m:
        for i in arr:
            tmp_sum += list1[i]
        if tmp_sum == total:
            cnt += 1
        return None

    for i in range(entry, n):
        if i in arr: continue

        arr.append(i)
        entry += 1
        permutation(arr, n, m, entry)
        arr.pop()

for i in range(1, num+1):
    entry = 0
    permutation(list(), num, i, entry)

print(cnt)
