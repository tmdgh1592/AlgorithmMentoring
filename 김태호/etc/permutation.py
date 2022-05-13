# 동작 과정 숙지

def f(arr):
    if len(arr) == 3:
        print(*arr)
        return None
    
    for i in range(1, 4):
        if i in arr: continue;
        
        arr.append(i)
        f(arr)
        arr.pop()
        
f(list())
