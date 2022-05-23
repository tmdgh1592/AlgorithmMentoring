city = int(input())
weight_list = [list(map(int, input().split())) for _ in range(city)]
total_weight = 0 #각각의 case별 비용의 합
final_weight = 9999999999999999999999999999999999 #최종 출력할 비용
tmp_weight = 0
check_sum = 9999999999


def check_weight(arr):
    global tmp_weight, final_weight, city
    tmp_weight = 0
    for i in range(len(arr) - 1):
        tmp_weight += weight_list[arr[i]][arr[i+1]] 
    if check_sum < tmp_weight: 
        return 1
    return 0
    
def permutation(arr, n):
    global total_weight, final_weight, check_sum
    total_weight = 0 #case마다 비용의 합 초기화
    if len(arr) == n:
        for i in range(n - 1):
            if weight_list[arr[i]][arr[i+1]] == 0: return None # 다음 경로의 비용이 0이면 경로 생성 불가 - return
            total_weight += weight_list[arr[i]][arr[i+1]] # 0, 1, 2, 3 순으로 순회한다면 0-1, 1-2, 2-3 비용의 합
        if weight_list[arr[-1]][arr[0]] == 0: return None #처음으로 돌아가는 경로의 비용이 0이면 경로 생성 불가 - return
        total_weight += weight_list[arr[-1]][arr[0]] # 3-0 비용
        if final_weight > total_weight: #최종 출력값과 비교하여 더 작으면 그 값을 final_weight에 저장
            final_weight = total_weight 
            check_sum = final_weight
        return None

    for i in range(n):
        if i in arr: continue
        arr.append(i)
        if check_weight(arr) == 1: continue
        permutation(arr, n)
        arr.pop()

permutation(list(), city)  
print(final_weight)

