if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sort_arr = sorted(arr)

    
    second_num = 0
    for num in reversed(sort_arr[:-1]):
        if num < max(sort_arr):
            second_num = num
            break
    if len(sort_arr) < 2:
        print(None)
    else:
        print(second_num)  
    