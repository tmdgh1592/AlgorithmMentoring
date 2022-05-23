n, s = map(int, input().split())
arr = list(map(int, input().split()))
case_arr = []
count = 0

def per(here):
    global count
    if len(case_arr) != 0:
        if sum(case_arr) == s:
            count += 1
        if len(case_arr) == len(arr):
            return None    
    for there in range(here + 1, n):
        case_arr.append(arr[there])
        per(there)
        case_arr.pop()
per(-1)
print(count)