MIS = lambda : map(int, input().split())
arr = []
case = []

while(True):
    temp = list(MIS())
    if temp[0] == 0:
        break
    arr.append(temp)

def comb(index):
    if len(case) == 6:
        print(*case)
        return None

    temp = arr[index][1:]
    for i in range(arr[index][0]):
        if temp[i] in case:
            continue
        if case and max(case) > temp[i]:
            continue
        case.append(temp[i])
        comb(index)
        case.pop()

def lotto():
    for i in range(len(arr)):
        comb(i)
        if i != len(arr)-1:
            print("")
lotto()
