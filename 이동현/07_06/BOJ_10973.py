MIS = lambda: map(int, input().rstrip().split())
n = int(input())
number = list(MIS())
 
def func(n, number):
    i = n -1
    while number[i-1] < number[i]  :
        i -= 1
    if i == 0:
        print(-1)
        exit()
    temp = n - 1
    while number[temp] > number[i - 1]:
        temp -= 1
    number[temp],number[i-1] = number[i-1],number[temp]
    result = number[:i] + list(reversed(number[i:]))
    print(*result)
func(n,number)
