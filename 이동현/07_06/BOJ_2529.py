n = int(input())
sign = list(input().rstrip().split())
number = list(range(0,10))
max_result = []
min_result = []

for i in range(n):
    min_result.append(i)
    max_result.append(9 - i)
def next():
    i = n -1
    while min_result[i-1] > min_result[i]:
        i -= 1
    if i <= 0:
        print(-1)
        exit()
    temp = n - 1
    while min_result[temp] < min_result[i - 1]:
        temp -= 1
    min_result[temp],min_result[i-1] = min_result[i-1],min_result[temp]
    result = min_result[:i] + sorted(min_result[i:])

def prev():
    i = n -1
    while max_result[i-1] < max_result[i]  :
        i -= 1
    if i == 0:
        print(-1)
        exit()
    temp = n - 1
    while max_result[temp] > max_result[i - 1]:
        temp -= 1
    max_result[temp],max_result[i-1] = max_result[i-1],max_result[temp]
    result = max_result[:i] + list(reversed(max_result[i:]))

def print_min():
    for i in range(n):
            print(1)
            if sign[i] == '>':
                if not min_result[i] > min_result[i + 1]:
                    next()
                    continue
            else:
                if not min_result[i] < min_result[i + 1]:
                    next()
                    continue
    print('ff'.join(map(str,min_result)))

print_min()