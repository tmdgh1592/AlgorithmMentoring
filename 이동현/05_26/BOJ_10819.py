from itertools import permutations

MIS = lambda : map(int, input().split())
n = int(input())
arr = list(MIS())
sum_max = 0

def sum(arr, len_arr):
    sum = 0
    for i in range(len_arr-1):
        sum += abs(arr[i] - arr[i+1])
    return sum

def get_max():
    global sum_max
    for i in permutations(arr, len(arr)):
        sum_max = max(sum_max, sum(i, len(i)))
    return sum_max
get_max()
print(sum_max)
